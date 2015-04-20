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
        page.open("http://mail.ru")

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        page = Page(self.driver)
        self.assertEqual("Mail.Ru: почта, поиск в интернете, новости, игры", page.title, "Ошибка загрузки страницы")
        page.search_bar.search(u"2гис")
        self.assertEqual("2гис - 2 млн результатов. Поиск Mail.Ru", page.title,  "Ошибка поиска")
        result = self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[1]/div/section/div/ul/li[2]/h3/a')
        res = result.get_attribute("class")
        self.assertEqual("light-link", res, "Ошибка отображения результатов")

    def test_zodiak(self):
        page = Page(self.driver)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[3]/div[2]/div[1]/div/table[1]/tbody/tr/td[3]/div/a/span').click()
        self.assertNotEqual("Mail.ru", page.current_url, "Некорректная ссылка")

if __name__ == '__main__':
    unittest.main()