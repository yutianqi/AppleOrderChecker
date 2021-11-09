#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
import time
import os


class SeleniumChecker(object):
    URL = 'https://secure2.www.apple.com.cn/shop/order/detail/506586/W885971562?_si=000010'

    driver = None

    userName = "xxx@icloud.com"
    password = "xxxxxxxxxxxxxx"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.firstLogin()

    def firstLogin(self):
        self.driver.get(self.URL)
        time.sleep(10)

        self.driver.switch_to.frame('aid-auth-widget')
        self.driver.find_element_by_id('account_name_text_field').send_keys(self.userName)
        self.driver.find_element_by_id('sign-in').click()
        self.driver.find_element_by_id('remember-me').click()
        time.sleep(10)
        self.driver.find_element_by_id('password_text_field').send_keys(self.password)
        time.sleep(3)
        self.driver.find_element_by_id('sign-in').click()
        time.sleep(30)
        print("finished to login...")

    def getData(self):
        try:
            self.driver.get(self.URL) # ask url
            time.sleep(10) #waiting for web loading
            element = self.driver.find_element_by_class_name('rs-od-itemstatus')
            print(element.text)
            return element.text
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            print(e)
        return ""


# checker = SeleniumChecker()
# print(checker.getData())
# os.system("pause")

