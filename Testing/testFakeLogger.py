__author__ = 'alexandre'

# This file will check the global fake logging process


import unittest

from FakeLogger import singleRequestGenerator


class TestRequestHandlingMethods(unittest.TestCase):

    def test_single_request_generator(self):
        self.assertEqual(singleRequestGenerator.generate_line_request(),
            ['123.213.45.21 - - [08/May/2015:11:43:29 +0200] "GET /cordova/jobcoacherionic/www/js/controllers/menu.js HTTP/1.1" 200 3434'])

    def test_path_generator(self):
        self.assertEqual(singleRequestGenerator.path_generator(1), ["path"])

    def test_ip_generator(self):
        self.assertEqual(singleRequestGenerator.ip_generator(1), "123.123.89.90")


if __name__ == '__main__':
    unittest.main()
