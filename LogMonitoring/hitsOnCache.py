__author__ = 'alexandre'

# we will monitor how often client requests are refused because the client's cache
# of the page is up to date

def ClientCachePercentage(logfile_pathname):
    logfile = open(logfile_pathname, "r").xreadlines()
    # log files can be huge, we use xreadlines instead of readline in order
    # not ot load all the lines in a list
    TotalRequest = 0
    CachedRequest = 0

    for line in logfile:
        TotalRequest += 1
        if line.split(" ")[8] == "304":  # the server returned 'not modified'
            CachedRequest += 1

    return 100*(CachedRequest/TotalRequest)