#!/usr/bin/env python

import requests
import re
import time


class TimeUtils(object):


    def __init__(self, default_title):
        """constructor"""
        pass

    def getDataTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime() 