__author__ = 'alexandre'

# This file will provide some functions to easily process the request
# like getting the path of the request or getting the time of the request

import time
import datetime
import logFileListener


def find_nth(haystack, needle, n):
    """
    find the nth occurrence of needle in haysytack
    :param haystack: string
    :param needle: string
    :param n: int
    :return: int
    """
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def get_path(req):
    """
    return the path of the request
    :param req: string (request)
    :return: string (path of the request)
    """
    path_pos_begin = find_nth(req, '/', 3) + 1  # we find the beginning of the path
    path_pos_end = find_nth(req, '/', 4)  # we find the end of the path
    return str(req[path_pos_begin:path_pos_end])


def get_time(req):
    """
    return the time elapsed since the request was recorded
    :param req: request
    :return: float
    """
    t = int(time.time())
    time_pos = req.find('[') + 1  # we find the position of the date
    date = req[time_pos:(time_pos+20)]   # we extract the date
    date = time.strptime(date, "%d/%b/%Y:%H:%M:%S")
    return t - int(datetime.datetime(*date[:6]).strftime('%s'))


def encode(l):
    """
    encode to utf8 the elem of the list
    :param l:
    :return: list
    """
    res = []
    for i in l:
        res.append(i.encode('utf-8'))
    return res


if __name__ == "__main__":
    print get_time('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -')
    print logFileListener.counter_ten_seconds
    print get_path('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -')
