__author__ = 'alexandre'

# This file will create a logging file with HTTP W3C-formatted requests
# Once created it will add on the fly some fake requests
# with the configFakeLogger file we will be able to simulate
# high traffic on a certain time

import configFakeLogger
import singleRequestGenerator
import time


def is_peak_time(t, l):
    """
    :param t: float * (float * float) list
    :return: bool
    """
    for elem in l:
        if (t > elem[0]) and (t < elem[1]):
            return True
    return False

# the object containing the configuration
# we generate a new one every single day
cfg = configFakeLogger.ConfigFakeLogger()


# This is the infinite loop of the fakelogger program
# It retrieve a request with help of singleRequestGenerator
# It then appends it to the access_log file and print the request on the screen
# The time between two requests is retrieved from the configFakeLogger file
# There is 2 types of gap time : one normal, and one short when there is high traffic
while True:
    current_time = time.time() % (24*3600)  # we get the number of second of today
    request = singleRequestGenerator.generate_line_request()
    if is_peak_time(current_time, cfg.peak_intervals):  # we are in peak time
        log_file = open('access_log', 'a')
        log_file.write(request + "\n")
        log_file.close()
        print(request + "\n")
        time.sleep(cfg.get_time_on_peak())  # we wait less time
    else:  # we are not in peak time
        log_file = open('access_log', 'a')
        log_file.write(request + "\n")
        log_file.close()
        print(request + "\n")
        time.sleep(cfg.get_time_on_average())