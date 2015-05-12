__author__ = 'alexandre'

# this file will print every 10s in the console the sections of the web site with most hits
# and also interesting stats
# monitoPrint will read from the queue the events, analyzing it and then pretty printing on the console

from collections import Counter


threshold = 100  # this is the threshold at which the alert will be triggered


def print_stats(count):
    """
    :param count: counter, which contains all the request from the last 10s
    :return: unit : print stats from the requests
    """
    print count.most_common(3)  # we get the most common paths
    print sum(count.values())  # we count all the requests from the last 10 s



def monito_print(count, last_120_requests, alert_state):
    """
    :param count: counter, which contains all the request from the last 10s
    :param last_120_request: list containing the request from the last 120 s
    :param alert_state: bool, representing if we are are notin alert state
    :return: unit : print on the screen the loggins
    """
    if alert_state:  # we were in alert state : did we recovered ?
        if len(last_120_requests) > threshold:  # still alert state
            print "alert state still on"
        else:  # we recovered
            print "alert recovery"
    else:  # (no alert state)
        if len(last_120_requests) > threshold:
            print "alert state on"
    print_stats(count)
