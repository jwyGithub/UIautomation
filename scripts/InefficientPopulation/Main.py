# coding = utf-8
# @Time    : 2020-08-03
# @Author  : jwy
# @File    : main.py
# @Mode    : 主流程

import sys
from util.util import byId, byXpath
from config.config import config
from common.login import Login
from selenium import webdriver
from time import sleep
sys.path.append("../..")


class Main():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def getUrl(self, url):
        self.driver.get(url)
        byId(self.driver, "J_Quick2Static").click()

    def selectItem(self):
        byXpath(self.driver, "//*[@id='its00189']").click()
        byXpath(self.driver, "//*[@id='its00257']").click()
        sleep(2)

    # 第一次运行
    def firstRun(self, config):
        self.getUrl(config['url'])
        # 登陆
        Login(self.driver).login(config['account'], config['pwd'])
        self.selectItem()

    def checkType(self):
        for i in range(10):
            byXpath(self.driver, "//*[@id='InefficientPopulation']/div[2]/nav/span[2]").click()
            sleep(1)
            byXpath(self.driver, "//*[@id='InefficientPopulation']/div[2]/nav/span[1]").click()
            sleep(1)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    MainFn = Main()
    MainFn.firstRun(config)
    MainFn.checkType()
    MainFn.quit()
