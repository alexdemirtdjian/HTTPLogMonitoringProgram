__author__ = 'alexandre'

# this file will print every 10s in the console the sections of the web site with most hits
# and also interesting stats
# monitoPrint will read from the queue the events, analyzing it and then pretty printing on the console

from configMonitoring import threshold


def print_stats(count):
    """
    :param count: counter, which contains all the request from the last 10s
    :return: unit : print stats from the requests
    """
    print count.most_common(3)  # we get the most common paths
    print sum(count.values())  # we count all the requests from the last 10 s


def monito_print(count, last_120_requests, alert):
    """
    :param count: counter, which contains all the request from the last 10s
    :param last_120_requests: list containing the request from the last 120 s
    :param alert: bool, representing if we are are in alert state
    :return: unit : print on the screen the logs
    """
    if alert:  # we were in alert state : did we recovered ?
        if sum(last_120_requests) > threshold:  # we have not recovered
            print "alert state on"
        else:
            print "recovery"
    print "most common hits last 10 seconds"
    print_stats(count)  # we print the most common requests from the last 120s