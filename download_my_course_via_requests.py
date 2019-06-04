import datetime
import re
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

import requests
from bs4 import BeautifulSoup

website_prefix = 'https://codewithmosh.com'
req_session = requests.session()
pool = ThreadPool()


def get_download_url(item):
    section_title = str(item.parent.parent.parent.select_one('.section-title').get_text()).strip()
    section_title_prefix = re.sub(r'\(.+', '', section_title)

    r = req_session.get(website_prefix + item['href'])

    soup = BeautifulSoup(r.text, 'html.parser')

    download = soup.select_one('.download')
    if download is not None:
        print(datetime.datetime.utcnow())
        downloaded_name = section_title_prefix + download['data-x-origin-download-name']
        print(downloaded_name + ': ' + download['href'])
        full_path = Path('courses') / 'nodejs' / downloaded_name
        if not full_path.exists():
            open(full_path.resolve(), 'wb').write(
                requests.get(download['href']).content)


def main():
    r = req_session.get(
        'https://sso.teachable.com/secure/146684/users/sign_in?clean_login=true&reset_purchase_session=1')
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    auth_token = soup.find('input', {'name': 'authenticity_token'})['value']

    data = {
        'utf8': '&#x2713;',
        'authenticity_token': auth_token,
        'user[school_id]': '146684',
        'user[email]': 'rayzrchen@gmail.com',
        'user[password]': 'Hsbc1234',
        'commit': 'Log In',

    }

    r = req_session.post('https://sso.teachable.com/secure/146684/users/sign_in?flow_school_id=146684', data=data)
    print(r.status_code)

    r = req_session.get('https://codewithmosh.com/courses/293204/lectures/4509750')
    print(r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    items = soup.select('.section-list a.item')
    pool.map(get_download_url, items)
    pool.close()
    pool.join()


main()
