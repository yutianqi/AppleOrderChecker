#!/usr/bin/env python

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
import json
from log_utils import LogUtils
from config_utils import ConfigUtils


class RestChecker(object):

    HEADER_STR = '''Host: www.sf-express.com
Connection: keep-alive
sec-ch-ua: "Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"
Accept: */*
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
sec-ch-ua-platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.sf-express.com/CN/ZH/dynamic_function/waybill/
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d3290ce30821-0a0a72d936636e-57b1a33-2073600-17d3290ce31e80%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217d3290ce30821-0a0a72d936636e-57b1a33-2073600-17d3290ce31e80%22%7D; SESSION=7c9d2814a64f47a6a741a1da56d030eb; remember-me=MWM4ZDI5Yjc3OGNjNDI5OGIxYzAyZWJkYmRlMWFjYTQ6OGEyYTllNzczMjNhNGRjYTg0ZjJkMjY3ZjUxZjA2MDY=; loginUser=18566665217'''

    proxies = {}

    url = 'https://www.sf-express.com/sf-service-core-web/service/waybillRoute/SF9600279142812/routesForInput?lang=sc&region=cn&translate=&app=route&subMobile=5217&answer=&mediaSource=PC.OWF'

    configUtils = None

    proxyEnable = False

    def __init__(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.intiConfig()
        pass

    def intiConfig(self):
        self.configUtils = ConfigUtils('conf.ini')
        self.proxies = {
            "http": self.configUtils.get("proxies", "http"),
            "https": self.configUtils.get("proxies", "https")
        }
        self.proxyEnable = self.configUtils.getBoolean("proxies", "enable")

    def getData(self):
        headers = self.loadHeader(self.HEADER_STR)
        # print(headers)
        LogUtils.info("-> send request")

        if self.proxyEnable:
            resp = requests.get(self.url, headers=headers,
                                proxies=self.proxies, verify=False)
        else:
            resp = requests.get(self.url, headers=headers, verify=False)
        # print(resp.status_code)

        if 200 != resp.status_code:
            return (-1, "", "请求执行失败，状态码：" + str(resp.status_code))

        contentStr = str(resp.content, encoding="utf-8")
        # print(contentStr)

        respJson = json.loads(contentStr)
        if not respJson.get("success"):
            LogUtils.info("-> 当前状态：" + respJson.get("message"))
            return respJson.get("message")
        recentStatus = respJson.get("result").get("routes")[
            0].get("routes")[-1]
        # print(recentStatus)

        LogUtils.info("-> 当前状态：" + recentStatus.get("scanDateTime") +
                      " " + recentStatus.get("remark"))

        return recentStatus.get("scanDateTime") + " " + recentStatus.get("remark")

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


# checker = RestChecker()
# print(checker.getData())
