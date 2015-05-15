__author__ = 'alexandre'

# this file will print every 10s in the console the sections of the web site with most hits
# and also interesting stats
# monitoPrint will read from the queue the events, analyzing it and then pretty printing on the console

from configMonitoring import threshold
import time


def get_stats(count, queue_two_minutes):
    """
    this function give interesting results from the counter of requests and the queue of requests from last 2 minutes
    :param count: counter, which contains all the request from the last 10s
    :param queue_two_minutes: queue, which contains the number of requests from the last 2 minutes
    :return: dict : a dictionary containing the results
    """
    res = {}  # the dictionay we will render
    res['total requests'] = sum(count.values())  # we count all the requests from the last 10 s
    res['total requests 120'] = sum(queue_two_minutes)
    return res


def monito_print(count, last_120_requests, alert, triggered_time, hits_alert):
    """
    :param count: counter, which contains all the request from the last 10s
    :param last_120_requests: list containing the request from the last 120 s
    :param alert: bool, representing if we are are in alert state
    :param triggered_time: date representing the last time time the alert was triggered
    :param hits_alert: int representing the number of hits that triggered the last alert
    :return: unit : print on the screen the stats
    """
    if alert:  # we were in alert state : did we recovered ?
        if sum(last_120_requests) > threshold:  # we have not recovered
            print "/!\ * * * * * * * * * * * * alert state on * * * * * * * * * * * * /!\\"
            print "High traffic generated an alert - hits = {0}, triggered at {1}".format(hits_alert, triggered_time)
        else:
            print " + + + + + + + + + + + + + + recovery + + + + + + + + + + + + + + "
            print "Alert recovery at {0}".format(time.strftime("%m-%d %H:%M:%S"))
    dict_stats = get_stats(count, last_120_requests)
    print "------------------------------------------------------------------------"
    for i in xrange(2, 6):
        print "hit(s) with status code " + str(i) + "xx : ", count[str(i) + "xx"]
        del count[str(i) + "xx"]  # we then remove it in order to be able to call most_common on paths
    most_hits = count.most_common(3)  # we get the most common paths
    print "most common hits last 10 seconds :"
    for (path, hits) in most_hits:
        print "    ", path, ":", hits, ("hits" if hits > 1 else "hit")
    print "total number of hits last 10 seconds : ", dict_stats['total requests']
    print "total number of hits last 2 minutes : ", dict_stats['total requests 120']
    print "------------------------------------------------------------------------"