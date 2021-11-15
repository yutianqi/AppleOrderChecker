#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
import time
import os
import requests

class SeleniumChecker(object):
    URL = 'https://secure2.www.apple.com.cn/shop/order/detail/506586/W885971562?_si=000010'

    driver = None

    userName = "xxx@icloud.com"
    password = "xxxxxxxxxxxxxx"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.firstLogin()

    def firstLogin(self):
        self.printLog("-> load page:" + self.URL)
        self.driver.get(self.URL)
        self.printLog("-> sleep 10s")
        time.sleep(10)
        self.printLog("-> switch_to aid-auth-widget")
        self.driver.switch_to.frame('aid-auth-widget')
        self.printLog("-> send userName")
        self.driver.find_element_by_id('account_name_text_field').send_keys(self.userName)
        self.printLog("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        self.printLog("-> click remember-me")
        self.driver.find_element_by_id('remember-me').click()
        self.printLog("-> sleep 10s")
        time.sleep(10)
        self.printLog("-> send password")
        self.driver.find_element_by_id('password_text_field').send_keys(self.password)
        self.printLog("-> sleep 3s")
        time.sleep(3)
        self.printLog("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        self.printLog("-> sleep 30s")
        time.sleep(30)
        self.printLog("finished to login...")

    def relogin(self):
        self.printLog("-> load page:" + self.URL)
        self.driver.get(self.URL)
        self.printLog("-> sleep 10s")
        time.sleep(10)
        self.printLog("-> switch_to aid-auth-widget")
        self.driver.switch_to.frame('aid-auth-widget')
        # self.printLog("-> send userName")
        # self.driver.find_element_by_id('account_name_text_field').send_keys(self.userName)
        # self.printLog("-> click sign-in")
        # self.driver.find_element_by_id('sign-in').click()
        # self.printLog("-> click remember-me")
        # self.driver.find_element_by_id('remember-me').click()
        # self.printLog("-> sleep 10s")
        # time.sleep(10)
        self.printLog("-> send password")
        self.driver.find_element_by_id('password_text_field').send_keys(self.password)
        self.printLog("-> sleep 3s")
        time.sleep(3)
        self.printLog("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        self.printLog("-> sleep 30s")
        time.sleep(30)
        self.printLog("finished to login...")

    def getData(self):
        try:
            self.printLog("-> load page:" + self.URL)
            self.driver.get(self.URL) 
            self.printLog("-> sleep 10s")
            time.sleep(10) 
            self.printLog("-> find element by class name: rs-od-itemstatus")

            currentStatusElement = self.driver.find_element_by_class_name('rs-status-current')
            self.printLog(currentStatusElement.text)

            itemStatusElement = self.driver.find_element_by_class_name('rs-od-itemstatus')
            self.printLog(itemStatusElement.text)

            return currentStatusElement.text + ' ' + itemStatusElement.text
        except Exception as e:
            # requests.get('http://pushplus.hxtrip.com/send?token=10acadfe5ee744938a0444d2ade9066f&title=订单状态变更提醒&content=' + '任务异常1Exception' + '&template=html')
            self.printLog("1Exception")
            print(e)
            self.printLog("begin to relogin...")
            self.relogin()
            return self.getData()
        return ""

    def printLog(self, logMsg):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + logMsg)


# checker = SeleniumChecker()
# print(checker.getData())
# os.system("pause")

