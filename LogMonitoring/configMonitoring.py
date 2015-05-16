__author__ = 'alexandre'

from path import path

# this is the threshold at which the alert will be triggered
# change it for your need
threshold = 40

# this is the path of the access_log file
# change it to the real access_log file
log_path = path('access_log').abspath()