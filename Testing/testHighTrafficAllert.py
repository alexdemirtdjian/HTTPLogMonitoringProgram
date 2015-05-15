__author__ = 'alexandre'

# This file will perform test to check for high traffic alerts

import unittest
import time

from LogMonitoring import monitoPrint, configMonitoring
from collections import Counter


# we rewrite here the monito_print functions, replacing prints with returns
# to make some unit tests


def monito_test(count, last_120_requests, alert, triggered_time, hits_alert):
    """
    :param count: counter, which contains all the request from the last 10s
    :param last_120_requests: list containing the request from the last 120 s
    :param alert: bool, representing if we are are in alert state
    :return: unit : print on the screen the stats
    """
    if alert:  # we were in alert state : did we recovered ?
        if sum(last_120_requests) > configMonitoring.threshold:  # we have not recovered
            return (hits_alert, triggered_time, "alert")
        else:
            return (time.strftime("%m-%d %H:%M:%S"), "recovery")
    dict_stats = monitoPrint.get_stats(count, last_120_requests)
    most_hits = count.most_common(3)  # we get the most common paths
    return (most_hits, dict_stats['total requests'], dict_stats['total requests 120'])




class TestAlertMethods(unittest.TestCase):

    def test_still_alert(self):
        count = Counter()
        count.update(["path1", "path1", "path2"])
        last_120_requests = [10 for _ in xrange(12)]  # we fot 120 requests from the last 2 minutes
        alert = True
        triggered_time = 0
        hits_alert = 120
        self.assertEqual(monito_test(count, last_120_requests, alert, triggered_time, hits_alert), (120, 0, 'alert'))

    def test_recovery_alert(self):
        count = Counter()
        count.update(["path1", "path1", "path2"])
        last_120_requests = [1 for _ in xrange(12)]  # we fot 12 requests from the last 2 minutes
        alert = True  # we were in alert state
        triggered_time = 0
        hits_alert = 120
        self.assertEqual(monito_test(count, last_120_requests, alert, triggered_time, hits_alert),
                         (time.strftime("%m-%d %H:%M:%S"), 'recovery'))

    def test_top_hits(self):
        count = Counter()
        count.update(["path1", "path1", "path2", "path4", "path4", "path6", "path5"])
        last_120_requests = [1 for _ in xrange(12)]  # we fot 12 requests from the last 2 minutes
        alert = False  # we were in alert state
        triggered_time = 0
        hits_alert = 120
        self.assertEqual(monito_test(count, last_120_requests, alert, triggered_time, hits_alert),
                         ([('path1', 2), ('path4', 2), ('path2', 1)], 7, 12))




if __name__ == '__main__':
    unittest.main()
