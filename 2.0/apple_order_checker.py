#!/usr/bin/env python


import requests
import re
import time
import os

from alarm_publisher import AlarmPublisher
# from post_checker import PostChecker
from selenium_checker import SeleniumChecker
from log_utils import LogUtils


CHECK_PERIOD_IN_SECOND = 5 * 60


def main():
    # checker = PostChecker()
    checker = SeleniumChecker()
    publisher = AlarmPublisher("Apple订单状态变更提醒")
    while True:
        try:
            LogUtils.info("begin to check")
            newStatus = checker.getData()
            # LogUtils.info(" 当前状态：" + newStatus)
            publisher.push(newStatus)
        except Exception as e:
            LogUtils.info(e)
        time.sleep(CHECK_PERIOD_IN_SECOND)


if '__main__' == __name__:
    main()
