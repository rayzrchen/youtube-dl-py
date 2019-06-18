import unittest
from multiprocessing.dummy import Pool as ThreadPool
from unittest.mock import MagicMock

from download_my_course import DownloadMyCourses


class TestDownloadMyCourses(unittest.TestCase):

    def setUp(self) -> None:
        self.download_my_courses = DownloadMyCourses()

    def test_range(self):
        aaa = ['a', 'b']
        [print('%02d %s' % (idx, aaa[idx])) for idx in range(len(aaa))]

    def test_get_all_sections_with_sequence_num(self):
        with open('test_html_file_1.html', encoding='utf8') as f:
            text = f.read()

        actual = self.download_my_courses.get_all_sections_with_sequence_num_using_html(text)
        expect = [
            'Getting Started',
            'Node Module System',
            'Node Package Manager',
            'Building RESTful APIs Using Express',
            'Express Advanced Topics',
            'Asynchronous JavaScript',
            'CRUD Operations Using Mongoose',
            'Mongo  Data Validation',
            'Mongoose Modeling Relationships between Connected Data',
            'Authentication and Authorization',
            'Handling and Logging Errors',
            'Unit Testing',
            'Integration Testing',
            'TestDriven Development',
            'Deployment'
        ]
        self.assertEqual(expect, actual)

    def test_get_lectures_with_file_name(self):
        with open('test_html_file_2.html', encoding='utf8') as f:
            text = f.read()

        actual = self.download_my_courses.get_lectures_with_file_name(text)

        expect = [
            ('4509750', '01_Getting Started_01_Welcome'),
            ('4509035', '01_Getting Started_02_What is Node'),
            ('4509036', '01_Getting Started_03_Node Architecture'),
            ('4509169', '02_Node Module System_01_Introduction'),
            ('4509174', '02_Node Module System_02_Global Object'),
        ]

        self.assertEqual(expect, actual)

    def test_strip_except_alphanumeric(self):
        actual = self.download_my_courses.get_section_title_as_file_prefix('Getting Started (00:20)')
        expect = 'Getting Started'
        self.assertEqual(expect, actual)

        actual = self.download_my_courses.get_section_title_as_file_prefix(
            'Building RESTful API\'s Using Express (00:56)')
        expect = 'Building RESTful APIs Using Express'
        self.assertEqual(expect, actual)

        actual = self.download_my_courses.get_section_title_as_file_prefix(
            'Mongoose- Modeling Relationships between Connected Data (00:51)')
        expect = 'Mongoose Modeling Relationships between Connected Data'
        self.assertEqual(expect, actual)

    def test_get_lecture_page_url_prefix(self):
        with open('test_html_file_1.html', encoding='utf8') as f:
            text = f.read()

        actual = self.download_my_courses.get_lecture_page_url_prefix(text)
        expect = 'https://codewithmosh.com/courses/293204/lectures'
        self.assertEqual(expect, actual)

    def test_get_each_lecture_download_info(self):
        with open('test_html_file_1.html', encoding='utf8') as f:
            text = f.read()

        actual = self.download_my_courses.get_lecture_download_url(text)
        expect = ('.mp4', 'https://www.filepicker.io/api/file/1N9dD3plRdGGdB9N2hId')
        self.assertEqual(expect, actual)

    def test_download_items(self):
        self.download_my_courses.course_name = 'sql'
        self.download_my_courses.prepare_login_session()
        self.download_my_courses.download_items('01_Getting Started_01_Welcome.mp4',
                                                'https://www.filepicker.io/api/file/1N9dD3plRdGGdB9N2hId')

    def test_thread_pool(self):
        pool = ThreadPool()
        pool.map(self.temp1, [(1, 2), (3, 4)])
        pool.close()
        pool.join()

    def temp1(self, a):
        print('1- Welcome.mp4'[-4])

    def test_e2e_without_download(self):
        self.download_my_courses = DownloadMyCourses('nodejs',
                                                     'https://codewithmosh.com/courses/293204/lectures/4509750')
        self.download_my_courses.download_items = MagicMock(side_effect=print('download_items mock'))
        self.download_my_courses.start_download()

    def test_last_characters(self):
        print('1- Welcome.mp4'[-4:])

    def test_magic_mock(self):
        self.download_my_courses.download_items = MagicMock(side_effect=print('mock'))
        self.download_my_courses.download_items((1, 1))

    def test_main(self):
        self.download_my_courses = DownloadMyCourses('python',
                                                     'https://codewithmosh.com/courses/423295/lectures/6781718')
        self.download_my_courses.start_download()

