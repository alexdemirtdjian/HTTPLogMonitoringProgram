__author__ = 'alexandre'

# This file will check the number of hits from each individual IP address that accessed the machine
# adpted from Oreilly : python cookbook


from collections import defaultdict

def CalculateIpHits(logfile_pathname):
    # we will store the hits in a dictionary
    # d[ip] = numberOfHits
    IpHitDict = defaultdict()
    Logfile = open(logfile_pathname, "r").xreadlines()
    # We go then through each of the logfile
    for line in Logfile:
        # Split the string to isolate the IP address
        Ip = line.split(" ")[0]
        if (6 < len(Ip)) and (len(Ip) <= 15):  # we check the length of the ip adress
            IpHitDict[Ip] += 1
    return IpHitDict