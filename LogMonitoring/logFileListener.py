__author__ = 'alexandre'

# This class will constantly look at the log file to check new line of log
# It will constantly look at change of the file size
# If changes, it will read new lines and add them to the queue

import os
import io
import time

from requestHandling import *
from collections import deque, Counter

import monitoPrint
import configMonitoring


# we define here two global variables
counter_ten_seconds = Counter()  # a counter containing the last 10s requests
queue_two_minutes = deque()  # a queue containing the last 120s requests


def get_size(logfile_path):
    """
    return the size of a file
    :param logfile_path: string
    :return: int
    """
    return os.stat(logfile_path).st_size


# This is the core of the program - contain an infinite loop
# after defining some starting variables
# (the size of the log_file, a buffer that will contain requests, alert_state and time)
# we also place the cursor at the end of the log_file
#
# we start the loop :
#   if there is line to be read, we read them and add them to the buff
#   else if the file has changed of size we close the stream and reopen it
#
#   if 10s has elapsed since the last print, we log with monito_print function
# we reset some variables, like l_buffer or count_ten_seconds

def listen_to_log_file(log_file_path):
    """
    The core function : contain an infinite loop that will print continuously logs an alert on the screen
    :param log_file_path: string
    :return: unit, print logs and alerts
    """

    # we initialize some variables
    current_size = get_size(log_file_path)  # the size of the log file
    logfile = io.open(log_file_path, 'r')
    logfile.seek(0, 2)  # we go at the eof
    l_buffer = []  # list containing all requests acting as a buffer
    alert_state = False  # the alert state of the program (We start with False)
    trigger_time = time.strftime("%m-%d %H:%M:%S")  # the last time we entered an alert state (set to now for now)
    hits_alert = 0  # the number of hits that trigger an alert (set to 0 for now)
    timer = time.time()
    while 1:

        lines = logfile.readlines()
        if lines:  # lines not empty, there is new line to read
            lines = encode(lines)  # we encode to utf8 in case it is unicode
            l_buffer = l_buffer + lines  # we add all the requests to the list

        elif current_size != get_size(log_file_path):
            # no more lines to read
            # the size has changed, new lines were written
            # print "changed size"
            left_position = logfile.tell()
            logfile.close()  # we close and reopen the file
            logfile = io.open(log_file_path, 'r')
            logfile.seek(left_position)  # we go to the position we left
            current_size = get_size(log_file_path)

        if time.time() - timer > 10.0:  # we haven't informed for 10s

            # update counter - this counter has the last 10s requests
            counter_ten_seconds.update(map(get_path, l_buffer))  # we update the 10s path requests
            # we retrieve and count also the status code requests
            status_code_lst = map(str, map(get_status_code, l_buffer))
            for i in range(2, 6):
                counter_ten_seconds[str(i) + "xx"] = len([elem for elem in status_code_lst if elem.startswith(str(i))])

            # we update the 120s queue - that has the total requests from the last 120s
            queue_two_minutes.appendleft(len(l_buffer))
            if len(queue_two_minutes) > 12:  # we have the last 130s requests
                queue_two_minutes.pop()  # we remove the last element = (the number of requests from 130 and 120s)

            if sum(queue_two_minutes) > monitoPrint.threshold and (not alert_state):  # we enter in an alert state
                alert_state = True
                trigger_time = time.strftime("%m-%d %H:%M:%S")
                hits_alert = sum(queue_two_minutes)  # the number of hits that triggered the alert

            monitoPrint.monito_print(counter_ten_seconds, queue_two_minutes, alert_state, trigger_time, hits_alert)

            # we need to put this condition after the print in order to get the recovery message
            if sum(queue_two_minutes) <= monitoPrint.threshold:  # we recovered from alert state
                alert_state = False

            # we reset the buffer and the counter for the next print
            counter_ten_seconds.clear()  # we clear the counter
            l_buffer = []  # we go to an empty list for the buffer
            timer = time.time()  # we reset timer to 0



if __name__ == "__main__":
    print listen_to_log_file(configMonitoring.log_path)
