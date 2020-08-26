# coding = utf-8
# @Time    : 2020-08-03
# @Author  : jwy
# @File    : Login.py
# @Mode    : 登陆
import sys
from util.util import byId, byClassname
# from selenium import webdriver
from time import sleep
sys.path.append("..")


class Login():
    def __init__(self, driver):
        self.driver = driver

    def login(self, account, pwd):
        byId(self.driver, "username").send_keys(account)
        byId(self.driver, "pass-word").send_keys(pwd)
        byClassname(self.driver, "login-button").click()
        sleep(2)
