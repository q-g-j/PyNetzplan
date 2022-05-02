# -*- coding: utf-8 -*-

import timeit


class TimeIt:
    def __init__(self):
        self.__start = 0.0
        self.__stop = 0.0

    def start(self):
        self.__start = timeit.default_timer()

    def stop(self):
        self.__stop = timeit.default_timer()

    def get_dauer(self):
        print("Dauer: {:.10f}".format(self.__stop - self.__start))
