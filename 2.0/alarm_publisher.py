#!/usr/bin/env python

import requests
import re
import time


class AlarmPublisher(object):

    """my first class: FooClass"""

    version = 0.1

    sent_msgs = []

    default_title = ''

    token = "xxx"

    BASE_URL = 'http://pushplus.hxtrip.com/send?token='

    ENABLE_DUPLICATE_MESSAGE = True

    def __init__(self, default_title):
        """constructor"""
        self.default_title = default_title

    def getRequestUrl(self, title, content, template):
        url = self.BASE_URL + self.token + '&title=' + title + '&content=' + \
            content + '&template=html'
        return url

    def push(self, msg):
        # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + msg)
        if not self.ENABLE_DUPLICATE_MESSAGE and msg in self.sent_msgs:
            # print("ignore duplicate message: " + msg)
            return
        self.sent_msgs.append(msg)
        url = self.getRequestUrl(self.default_title, msg, 'html')
        resp = requests.get(url)
        if 200 != resp.status_code:
            print("消息推送失败")
