__author__ = 'alexandre'

# This file will check the number of hits from each individual IP address that accessed the machine
# adapted from Oreilly : python cookbook


from collections import defaultdict


def calculate_ip_hits(logfile_pathname):
    # we will store the hits in a dictionary
    # d[ip] = numberOfHits
    ip_hit_dict = defaultdict()
    log_file = open(logfile_pathname, "r").xreadlines()
    # We go then through each of the logfile
    for line in log_file:
        # Split the string to isolate the IP address
        ip = line.split(" ")[0]
        if (6 < len(ip)) and (len(ip) <= 15):  # we check the length of the ip adress
            ip_hit_dict[ip] += 1
    return ip_hit_dict