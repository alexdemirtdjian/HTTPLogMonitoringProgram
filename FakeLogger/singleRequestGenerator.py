__author__ = 'alexandre'

# This file will generate single client request to the machine
# It will add one line to the log file containing a random request

import random
from collections import defaultdict
import datetime


# this list contains most common status code request
common_status_code_list = [200, 300, 301, 302, 304, 307, 400, 401, 403, 404, 410, 500, 501, 503, 505]

# this list contain HTTP methods
http_methods = ["GET", "POST", "PUT", "DELETE"]

# we define here an random ip addresses generator
def ip_generator(n):
    """
    int -> ip list : return a random ip adress
    """
    ip_list = []  # a list containing some random ip adresses
    for i in xrange(n):
        ip = ".".join(map(str, (random.randint(0, 255) for _ in xrange(4))))
        ip_list.append(ip)
    return ip_list

# this list contains some random ip
ip_list = ip_generator(100)

# this list contains some random bytes numbers,
# dedicated to mean the content-length of the document transferred
mu, sigma = 3000, 800  # we will generate random numbers according a gaussian distribution
bytes_list = [int(random.gauss(mu, sigma)) for _ in xrange(100)]

# we will define some random request from the client
# we assume we are on the website : http://my.site.com/
base_level = ["http://my.site1.com", "http://my.site2.com", "http://my.site3.com"]
first_level = ["music", "guests", "message", "video", "marks", "notifications", "photos"]
second_level = ["stats", "best", "recent", "popular"]
third_level = [("id" + str(i)) for i in xrange(30)]

dico_site = defaultdict()
# this dictionary will contains previous lists (k, v) = (depth, list)
dico_site[0] = first_level
dico_site[1] = second_level
dico_site[2] = third_level


def path_generator(n):
    """
    :param n: int : number of url
    :return: url list : list of random url from the website
    """
    res = []  # the list containing random urls
    for _ in xrange(n):
        depth = random.randint(1, 5)  # we generate the depth of the request
        # we increase the probability of deep request
        url = "/".join([random.choice(dico_site[i]) for i in xrange(min(3, depth))])
        method = random.choice(http_methods)
        res.append(method + " " + url)
    return res

# the list containing random requests from client
path_list = path_generator(100)


class Request():
    # This class will create Request Object which will
    # represent a single request from a client

    def __init__(self, client_ip = None, date_request = None, path = None, status_code = None, bytes = None):
        self.client_ip = client_ip
        self.date_request = date_request
        self.path = path
        self.status_code = status_code
        self.bytes = bytes

    def hydrate_client_ip(self, client_ip):
        self.client_ip = client_ip

    def hydrate_date_request(self, date_request):
        self.date_request = date_request

    def hydrate_path(self, path):
        # we add moreover the " "
        self.path = '"' + path + '"'

    def hydrate_status_code(self, status_code):
        self.status_code = status_code

    def hydrate_bytes(self, bytes):
        self.bytes = bytes


def generate_line_request():
    """
    generate on the fly request, we generate on the fly because we want
    to be consistent with the date
    :return: request
    """
    now = datetime.datetime.now()
    # we define the current time
    request = Request()
    request.hydrate_client_ip(random.choice(ip_list))
    request.hydrate_date_request(now.strftime("[%d/%b/%Y:%H:%M:%S +0200]"))
    request.hydrate_path(random.choice(path_list))
    request.hydrate_bytes(random.choice(bytes_list))

    request.hydrate_status_code(random.choice(common_status_code_list))
    return " ".join([request.client_ip, "-", "-", request.date_request, request.path, str(request.status_code), str(request.bytes)])


if __name__ == "__main__":
    print common_status_code_list
    print bytes_list
    print ip_list
    print path_list

    print generate_line_request()

# We will generate a line like that
# 123.213.45.21 - - [08/May/2015:11:43:29 +0200] "GET /cordova/jobcoacherionic/www/js/controllers/menu.js HTTP/1.1" 200 3434
