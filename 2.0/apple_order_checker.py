#!/usr/bin/env python


import requests
import re
import time
import os

from alarm_publisher import AlarmPublisher
# from post_checker import PostChecker
from selenium_checker import SeleniumChecker


# SENT_MSG = ['预计送达日期 2021/11/26 - 2021/12/03']
SENT_MSG = []

CURRENT_STATUS = ""

CHECK_PERIOD_IN_SECOND = 5 * 60


def main():
    # checker = PostChecker()
    checker = SeleniumChecker()

    while True:
        try:
            print("begin to check")
            newStatus = checker.getData()
            print(time.strftime("%Y-%m-%d %H:%M:%S",
                  time.localtime()) + " 当前状态：" + newStatus)
            if newStatus not in SENT_MSG:
                requests.get(
                    'http://pushplus.hxtrip.com/send?token=10acadfe5ee744938a0444d2ade9066f&title=订单状态变更提醒&content=' + newStatus + '&template=html')
                SENT_MSG.append(newStatus)
        except Exception as e:
            print("Exception")
        time.sleep(CHECK_PERIOD_IN_SECOND)


if '__main__' == __name__:
    # main()
    publisher = AlarmPublisher("订单状态变更提醒")
    publisher.push("订单状态变更提醒")
