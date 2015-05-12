__author__ = 'alexandre'

# This file will contain config param to the fakeLogging
# we will thus be able to generate high traffic on certain period

import random


class ConfigFakeLogger():
    # this class will give : the average time separating two requests
    # the average time separating request during peak time
    # the period of the day when there will be peak time

    def __init__(self):
        # times of the day when high traffic will be generated
        self.peak_times = [random.randrange(0, 24*3600) for _ in xrange(random.randint(2, 10))]
        # we define g as an interval maker
        g = lambda x: (x-random.gauss(150, 30), x+random.gauss(150, 30))
        # intervals of the day when high traffic will be generated
        self.peak_intervals = map(g, self.peak_times)

    def get_time_on_peak(self):
        return random.uniform(0, 1)  # the time separating two request on peak time

    def get_time_on_average(self):
        return random.uniform(1, 10)  # the average time separating two requests


if __name__ == "__main__":
    cfg = ConfigFakeLogger()

    print cfg.get_time_on_average()
    print cfg.get_time_on_peak()
    print cfg.peak_times
    print cfg.peak_intervals

    print cfg.get_time_on_average()
    print cfg.get_time_on_peak()
    print cfg.peak_times
    print cfg.peak_intervals


