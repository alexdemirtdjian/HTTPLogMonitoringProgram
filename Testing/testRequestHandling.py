__author__ = 'alexandre'

# This file will perform test to check for high traffic alerts

import unittest

from LogMonitoring import requestHandling
import time
import datetime


class TestRequestHandlingMethods(unittest.TestCase):

    def test_find_nth(self):
        self.assertEqual(requestHandling.find_nth("test/test/test/test", "/", 2), 9)

    def test_get_path(self):
        self.assertEqual(requestHandling.get_path('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -'), "angular")

    def test_get_time(self):
        self.assertEqual(requestHandling.get_time('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -'),
                         int(time.time()) - int(datetime.datetime(2015, 05, 12, 11, 40, 06).strftime('%s')))



if __name__ == '__main__':
    unittest.main()

