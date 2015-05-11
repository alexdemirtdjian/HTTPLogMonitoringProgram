__author__ = 'alexandre'

# This file will contain config param to the fakeLogging
# we will thus be able to generate high traffic on certain period

import random


class config_fake_logger():
    # this class will give : the average time separating two requests
    # the average time separating request during peak time
    # the period of the day when there will be peak time

    def __init__(self):
        # times of the day when high traffic will be generated
        self.peakTimes = [random.randrange(0, 24*3600) for _ in xrange(random.randint(2, 10))]
        # we define g as an interval maker
        g = lambda x: (x-random.gauss(150, 30), x+random.gauss(150, 30))
        # interals of the day when high traffic will be generated
        self.peakIntervals = map(g, self.peakTimes)

    def getTimeOnPeak(self):
        return random.uniform(0, 1)  # the time separating two request on peak time

    def getTimeOnAverage(self):
        return random.uniform(1, 10)  # the average time separating two requests


if __name__ == "__main__":
    cfg = config_fake_logger()

    print cfg.getTimeOnAverage()
    print cfg.getTimeOnPeak()
    print cfg.peakTimes
    print cfg.peakIntervals

    print cfg.getTimeOnAverage()
    print cfg.getTimeOnPeak()
    print cfg.peakTimes
    print cfg.peakIntervals


