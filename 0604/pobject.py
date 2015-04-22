__author__ = 'whitefoxnsk'
#  -*- coding:UTF-8 -*-

from unittest import TestCase
import unittest
from selenium import webdriver
from page import Page


class SeleniumTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        page = Page(self.driver)
        page.open("http://github.com")

    def tearDown(self):
        self.driver.close()

    def test_login(self):
        page = Page(self.driver)
        page.sign_in().button_click()
        page.login().login("totalflush", "2gistesT")

        login = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[2]/li[1]/a/span/span")
        span = login.get_attribute("class")
        self.assertEqual("css-truncate-target", span, "Login error!")

    def test_help(self):
        page = Page(self.driver)
        page.sign_in().button_click()
        page.login().login("totalflush", "2gistesT")

        page.git_help().help()
        self.assertTrue("GitHub Help" in page.title, "Error link")


if __name__ == '__main__':
    unittest.main()
