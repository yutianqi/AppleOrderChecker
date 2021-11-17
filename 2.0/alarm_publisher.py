#!/usr/bin/env python

import requests
import re
import time
from config_utils import ConfigUtils
from log_utils import LogUtils

class AlarmPublisher(object):

    configUtils = None

    sent_msgs = []

    default_title = ''

    token = ""

    BASE_URL = 'http://pushplus.hxtrip.com/send?token='

    def __init__(self, default_title):
        self.configUtils = ConfigUtils('conf.ini')
        self.token = self.configUtils.get("pushplus", "token")
        self.default_title = default_title

    def getRequestUrl(self, title, content, template):
        url = self.BASE_URL + self.token + '&title=' + title + '&content=' + \
            content + '&template=html'
        return url

    def push(self, msg):
        if msg in self.sent_msgs:
            # 不推送重复消息
            return
        url = self.getRequestUrl(self.default_title, msg, 'html')
        resp = requests.get(url)
        if 200 != resp.status_code:
            LogUtils.info("消息推送失败 STATUS_CODE:" + resp.status_code + " URL:" + url)
            return
        self.sent_msgs.append(msg)


# alarmPublisher = AlarmPublisher("Apple订单状态变更提醒")
# alarmPublisher.push('test')
