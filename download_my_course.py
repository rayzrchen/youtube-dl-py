import datetime
import itertools
import os
import re
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup, Tag


class DownloadMyCourses:
    website_prefix = 'https://codewithmosh.com'
    req_session = requests.session()
    pool = ThreadPool()

    def __init__(self, course_name: str = '', first_course_url: str = ''):
        self.course_name = course_name
        self.first_course_url = first_course_url

    def start_download(self):
        if not self.prepare_login_session():
            raise ValueError('Fail to login')

        self.prepare_course_folder()
        self.pool.map(self.download_items, self.prepare_download_items())
        self.pool.close()
        self.pool.join()

    def prepare_course_folder(self):
        course_folder = (Path('courses') / self.course_name)
        if not course_folder.exists():
            course_folder.mkdir(exist_ok=True)

    def get_section_title_as_file_prefix(self, str1: str) -> str:
        no_time_info = re.sub(r'\(.+', '', str1)
        return re.sub('[-\']|\n', '', no_time_info).strip()

    def download_items(self, lecture_file_name_with_url: Tuple[str, str]):
        if lecture_file_name_with_url[1] != '':
            print(datetime.datetime.utcnow())
            full_path = Path('courses') / self.course_name / lecture_file_name_with_url[0]
            if not full_path.exists():
                with open(full_path.resolve(), 'wb') as f:
                    f.write(self.req_session.get(lecture_file_name_with_url[1]).content)

    def prepare_download_items(self) -> List[Tuple[str, str]]:
        print('prepare_download_items')
        r = self.req_session.get(self.first_course_url)
        lectures_with_file_name = self.get_lectures_with_file_name(r.text)
        lecture_page_url_prefix = self.get_lecture_page_url_prefix(r.text)

        return [self.map_lecture_file_name_to_download_url(item, lecture_page_url_prefix) for item in
                lectures_with_file_name]

    def prepare_login_session(self) -> bool:
        prefix = 'https://sso.teachable.com/secure/146684/users'
        login_page_url = '%s/sign_in?clean_login=true&reset_purchase_session=1' % prefix
        r = self.req_session.get(login_page_url)
        if not r.ok:
            return False

        soup = BeautifulSoup(r.text, 'html.parser')
        auth_token = soup.find('input', {'name': 'authenticity_token'})['value']

        data = {
            'utf8': '&#x2713;',
            'authenticity_token': auth_token,
            'user[school_id]': '146684',
            'user[email]': os.environ['SITE_USER'],
            'user[password]': os.environ['SITE_PASSWORD'],
            'commit': 'Log In',
        }

        login_url = '%s/sign_in?flow_school_id=146684' % prefix
        r2 = self.req_session.post(login_url, data=data)
        return r2.ok

    def get_all_sections_with_sequence_num_using_html(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'html.parser')
        section_locks = soup.select('span.section-lock')
        return [self.get_section_title_tag(section_lock) for section_lock in section_locks]

    def get_all_sections_with_sequence_num(self, soup: BeautifulSoup) -> List[str]:
        section_locks = soup.select('span.section-lock')
        return [self.get_section_title_tag(section_lock) for section_lock in section_locks]

    def get_section_title_tag(self, section_lock: Tag) -> str:
        return self.get_section_title_as_file_prefix(section_lock.next_sibling)

    def get_all_lectures_pages(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'html.parser')
        link_items = soup.select('a.item')
        return [link_item['href'] for link_item in link_items]

    def get_lectures_with_file_name(self, html: str) -> List[Tuple[str, str]]:
        soup = BeautifulSoup(html, 'html.parser')
        section_locks = soup.select('span.section-lock')

        dual_list = [self.map_to_lecture_list(section_locks[idx], idx) for idx in range(len(section_locks))]
        return list(itertools.chain(*dual_list))

    def map_to_lecture_list(self, section_lock: Tag, index: int) -> List[Tuple[str, str]]:
        section_title_as_file_prefix = '%02d_%s' % (index + 1,
                                                    self.get_section_title_as_file_prefix(section_lock.next_sibling))
        section_items = section_lock.parent.parent.select('li.section-item')

        return [self.map_item_to_lecture(section_items[idx], idx, section_title_as_file_prefix) for idx
                in range(len(section_items))]

    def map_item_to_lecture(self, each_item: Tag, index: int, section_title_as_file_prefix: str) -> Tuple[str, str]:
        lecture_id = each_item['data-lecture-id']
        lecture_name = self.get_section_title_as_file_prefix(each_item.select_one('.lecture-name').get_text())
        return lecture_id, '%s_%02d_%s' % (section_title_as_file_prefix, index + 1, lecture_name)

    def get_lecture_download_url(self, html: str) -> Tuple[str, str]:
        soup = BeautifulSoup(html, 'html.parser')

        download = soup.select_one('a.download')
        if download is not None:
            url = download['href']
            suffix = download['data-x-origin-download-name'][-4:]
        else:
            url = ''
            suffix = ''
        return suffix, url

    def get_lecture_page_url_prefix(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        url = soup.find('meta', property='og:url')['content']
        return re.sub('lectures/.+', 'lectures', url)

    def map_lecture_file_name_to_download_url(self, item: Tuple[str, str], lecture_page_url_prefix: str) \
            -> Tuple[str, str]:
        r = self.req_session.get('%s/%s' % (lecture_page_url_prefix, item[0]))
        if not r.ok:
            print('status code: %s for lecture: %s' % (r.status_code, item[1]))
            return

        download_url = self.get_lecture_download_url(r.text)
        result = item[1] + download_url[0], download_url[1]
        print('%s === %s' % (result[0], result[1]))
        return result
