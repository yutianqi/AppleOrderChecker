#!/usr/bin/env python

import requests
import re

class PostChecker(object):
    SENT_MSG = ['状态更新：预计送达日期 2021/11/26 - 2021/12/03']

    HEADER_STR = ''''''
    
    url = 'https://secure2.www.apple.com.cn/shop/order/detail/506586/W885971562?_si=000010'

    def __init__(self):
        """constructor"""
        pass

    def getData(self):
        headers = self.loadHeader(self.HEADER_STR)
        print(headers)
        resp = requests.get(self.url, headers=headers, verify=False)

        print(resp.status_code)
        if 200 != resp.status_code:
            return (-1, "", "请求执行失败，状态码：" + str(resp.status_code))

        contentStr = str(resp.content, encoding="utf-8")
        # print(contentStr)

        m = re.search('"deliveryDate":"(.+?)"', contentStr)
        if not m:
            return (-1, "", "报文格式变更，请处理")

        newStatus = m.group(1)
        # print(newStatus)
        return (0, newStatus,)

    def loadHeader(self, headerStr):
        header = {}
        for line in headerStr.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("GET") or line.startswith("POST"):
                continue
            tempArray = line.split(": ")
            header[tempArray[0]] = tempArray[1]

        return header


checker = PostChecker()
print(checker.getData())
