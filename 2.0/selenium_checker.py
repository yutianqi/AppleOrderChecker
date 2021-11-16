#!/usr/bin/env python
#coding=utf-8

from selenium import webdriver
import time
import os
import requests
from config_utils import ConfigUtils
from log_utils import LogUtils

class SeleniumChecker(object):

    driver = None
    configUtils = None
    seleniumLogEnable = False
    orderPageURL = ''
    username = ""
    password = ""

    def __init__(self):
        self.intiConfig()
        options = webdriver.ChromeOptions()
        if not self.seleniumLogEnable:            
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options)
        self.firstLogin()

    def intiConfig(self):
        self.configUtils = ConfigUtils('conf.ini')
        self.username = self.configUtils.get("iCloud", "username")
        self.password = self.configUtils.get("iCloud", "password")
        self.seleniumLogEnable = self.configUtils.getBoolean("selenium", "logEnable")
        self.orderPageURL = self.configUtils.get("order", "url")
        
    def firstLogin(self):
        LogUtils.info("-> First login. load page:" + self.orderPageURL)
        self.driver.get(self.orderPageURL)
        LogUtils.info("-> sleep 10s")
        time.sleep(10)
        LogUtils.info("-> switch_to aid-auth-widget")
        self.driver.switch_to.frame('aid-auth-widget')
        LogUtils.info("-> send username")
        self.driver.find_element_by_id('account_name_text_field').send_keys(self.username)
        LogUtils.info("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        LogUtils.info("-> click remember-me")
        self.driver.find_element_by_id('remember-me').click()
        LogUtils.info("-> sleep 10s")
        time.sleep(10)
        LogUtils.info("-> send password")
        self.driver.find_element_by_id('password_text_field').send_keys(self.password)
        LogUtils.info("-> sleep 3s")
        time.sleep(3)
        LogUtils.info("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        LogUtils.info("-> sleep 30s")
        time.sleep(30)
        LogUtils.info("finished to login...")

    def relogin(self):
        LogUtils.info("-> Relogin. load page:" + self.orderPageURL)
        self.driver.get(self.orderPageURL)
        LogUtils.info("-> sleep 10s")
        time.sleep(10)
        LogUtils.info("-> switch_to aid-auth-widget")
        self.driver.switch_to.frame('aid-auth-widget')
        # 首次登录后，再次登录时只需要重新输入密码
        LogUtils.info("-> send password")
        self.driver.find_element_by_id('password_text_field').send_keys(self.password)
        LogUtils.info("-> sleep 3s")
        time.sleep(3)
        LogUtils.info("-> click sign-in")
        self.driver.find_element_by_id('sign-in').click()
        LogUtils.info("-> sleep 20s")
        time.sleep(20)
        input("-> 请在浏览器中输入二次认证验证码，并勾选信任当前浏览器，完成后请按回车")
        LogUtils.info("finished to login...")

    def getData(self):
        try:
            LogUtils.info("-> load page:" + self.orderPageURL)
            self.driver.get(self.orderPageURL) 
            LogUtils.info("-> sleep 10s")
            time.sleep(10) 
            LogUtils.info("-> find element by class name: rs-od-itemstatus")
            # 定位当前进展元素
            currentStatusElement = self.driver.find_element_by_class_name('rs-status-current')
            LogUtils.info(currentStatusElement.text)
            # 定位配送信息元素
            itemStatusElement = self.driver.find_element_by_class_name('rs-od-itemstatus')
            LogUtils.info(itemStatusElement.text)

            return currentStatusElement.text + ' ' + itemStatusElement.text
        except Exception as e:
            # 如果发生异常，记录日志并重新登录
            LogUtils.info(e)
            LogUtils.info("begin to relogin...")
            self.relogin()
            return self.getData()
        return ""

# checker = SeleniumChecker()
# print(checker.getData())

