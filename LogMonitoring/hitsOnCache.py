__author__ = 'alexandre'

# This is a function dedicated to improve the monitoring system
# Not still implemented
# we will monitor how often client requests are refused because the client's cache
# of the page is up to date


def client_cache_percentage(logfile_pathname):
    """
    takes the path of the logfile and return a percentage of hits on cache
    :param logfile_pathname: string
    :return: float
    """
    logfile = open(logfile_pathname, "r").xreadlines()
    # log files can be huge, we use xreadlines instead of readline in order
    # not ot load all the lines in a list
    total_request = 0
    cached_request = 0

    for line in logfile:
        total_request += 1
        if line.split(" ")[8] == "304":  # the server returned 'not modified'
            cached_request += 1

    return 100*(cached_request/total_request)