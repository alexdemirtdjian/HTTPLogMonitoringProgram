__author__ = 'alexandre'

# this file will print every 10s in the console the sections of the web site with most hits
# and also interesting stats
# monitoPrint will read from the queue the events, analyzing it and then pretty printing on the console

from configMonitoring import threshold


def get_stats(count):
    """
    this function give interesting results from the counter of requests
    :param count: counter, which contains all the request from the last 10s
    :return: dict : a dictionary containing the results
    """
    res = {}  # the dictionay we will render
    res['total requests'] = sum(count.values())  # we count all the requests from the last 10 s
    return res


def monito_print(count, last_120_requests, alert):
    """
    :param count: counter, which contains all the request from the last 10s
    :param last_120_requests: list containing the request from the last 120 s
    :param alert: bool, representing if we are are in alert state
    :return: unit : print on the screen the stats
    """
    if alert:  # we were in alert state : did we recovered ?
        if sum(last_120_requests) > threshold:  # we have not recovered
            print "/!\ * * * * * * * * * * alert state on * * * * * * * * * * /!\\"
        else:
            print " + + + + + + + + + + + + recovery + + + + + + + + + + + + "
    dict_stats = get_stats(count)
    most_hits = count.most_common(3)  # we get the most common paths
    print "--------------------------------------------------------------"
    print "most common hits last 10 seconds :"
    for (path, hits) in most_hits:
        print "    ", path, ":", hits, ("hits" if hits > 1 else "hit")
    print "total number of hits last 10 seconds : ", dict_stats['total requests']
    print "--------------------------------------------------------------"