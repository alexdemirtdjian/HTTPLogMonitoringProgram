__author__ = 'alexandre'

# All the log events will come into the queue to be processed
# There will be two queues : one containing entries from the last 10 s
# the other containing the entries with only the datetime, from the last two minutes

import time
import datetime


def get_time(req):
    """
    return the time elapsed since the request was recorded
    :param req: request
    :return: float
    """
    t = int(time.time())
    time_pos = req.find('[') + 1  # we find the position of the date
    date = req[time_pos:(time_pos+19)]   # we extract the date
    date = time.strptime(date, "%d/%b/%Y:%H:%M:%S")
    return t - int(datetime.datetime(*date[:6]).strftime('%s'))



if __name__ == "__main__":
    print get_time('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -')
    print counter_ten_seconds
    print get_path('::1 - - [12/May/2015:11:40:06 +0200] "GET /angular/WeatherAngular/app/partials/forecast.html HTTP/1.1" 304 -')
