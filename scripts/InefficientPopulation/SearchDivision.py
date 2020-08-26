# coding = utf-8
# @Time    : 2020-08-03
# @Author  : jwy
# @File    : CheckType.py
# @Mode    : 搜索
import sys
from util.util import byId, byXpath, isElementPresent
from config.config import config
from common.login import Login
from selenium import webdriver
from time import sleep
sys.path.append("../..")


class CheckType():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def getUrl(self, url):
        self.driver.get(url)
        byId(self.driver, "J_Quick2Static").click()

    def selectItem(self):
        byId(self.driver, "its00189").click()
        sleep(2)
        byId(self.driver, 'its00257').click()
        sleep(2)

    # 第一次运行
    def firstRun(self, config):
        self.getUrl(config['url'])
        # 登陆
        Login(self.driver).login(config['account'], config['pwd'])
        self.selectItem()

    def SearchDivision(self, list):
        for i in list:
            byXpath(self.driver, "/html/body/div[1]/div[3]/main/div/div[2]/div[2]/div[1]/input").send_keys(i)
            sleep(1)
            if isElementPresent(self.driver, '/html/body/div[1]/div[3]/main/div/div[2]/div[2]/div[1]/dl/dd/a'):
                byXpath(self.driver, "/html/body/div[1]/div[3]/main/div/div[2]/div[2]/div[1]/dl/dd/a").click()
                sleep(1)
                byXpath(self.driver, "/html/body/div[1]/div[3]/main/div/div[2]/div[2]/div[1]/input").clear()
        sleep(1)

    def SearchDepartment(self, list):
        for i in list:
            byXpath(self.driver, "//*[@id='InefficientPopulation']/div[2]/div[2]/div[2]/input").send_keys(i)
            sleep(1)
            if isElementPresent(self.driver, '//*[@id="InefficientPopulation"]/div[2]/div[2]/div[2]/dl/dd/a'):
                byXpath(self.driver, "//*[@id='InefficientPopulation']/div[2]/div[2]/div[2]/dl/dd/a").click()
                sleep(1)
                byXpath(self.driver, "//*[@id='InefficientPopulation']/div[2]/div[2]/div[2]/input").clear()
        sleep(1)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    checkTypeFn = CheckType()
    checkTypeFn.firstRun(config)
    checkTypeFn.SearchDivision(['江苏', '上海', '苏州', '顺德', '北京'])
    checkTypeFn.SearchDepartment(['江苏', '上海', '苏州', '顺德', '北京'])
    checkTypeFn.quit()
