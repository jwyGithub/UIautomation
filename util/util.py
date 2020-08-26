# coding = utf-8
from selenium.common.exceptions import NoSuchElementException


def byId(self, el):
    return self.find_element_by_id(el)


def byXpath(self, el):
    return self.find_element_by_xpath(el)


def byClassname(self, el):
    return self.find_elements_by_class_name(el)[0]


def byText(self, el):
    return self.find_element_by_link_text(el)


def isElementPresent(self, path):
    try:
        self.find_element_by_xpath(path)
    # 原文是except NoSuchElementException, e:
    except NoSuchElementException as e:
        # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
        print(e)
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True
