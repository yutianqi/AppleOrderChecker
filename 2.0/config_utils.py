#!/usr/bin/env python

import configparser


class ConfigUtils(object):

    config = None

    def __init__(self, configFilePath, encoding="utf-8"):
        self.config = configparser.ConfigParser()
        self.config.read(configFilePath, encoding=encoding)

    def get(self, key1, key2):
        return self.config.get(key1, key2)

    def getBoolean(self, key1, key2):
        return self.config.getboolean(key1, key2)

# configUtils = ConfigUtils('conf.ini')
# print(configUtils.get("pushplus", "token"))
# print(configUtils.getBoolean("selenium", "logEnable"))

