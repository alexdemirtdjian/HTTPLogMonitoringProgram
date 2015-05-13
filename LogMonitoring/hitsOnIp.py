__author__ = 'alexandre'

# This is a function dedicated to improve the monitoring system
# Not still implemented
# This file will check the number of hits from each individual IP address that accessed the machine
# adapted from Oreilly : python cookbook


from collections import defaultdict


def calculate_ip_hits(logfile_pathname):
    """
    takes the path of the logfile and return a dict counting the hits par ip
    :param logfile_pathname: string
    :return: dict
    """
    # we will store the hits in a dictionary
    # d[ip] = numberOfHits
    ip_hit_dict = defaultdict()
    log_file = open(logfile_pathname, "r").xreadlines()
    # We go then through each of the logfile
    for line in log_file:
        # Split the string to isolate the IP address
        ip = line.split(" ")[0]
        if (6 < len(ip)) and (len(ip) <= 15):  # we check the length of the ip address
            ip_hit_dict[ip] += 1
    return ip_hit_dict