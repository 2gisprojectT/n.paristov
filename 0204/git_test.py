__author__ = 'whitefoxnsk'

from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

# driver = webdriver.Remote(
#    command_executor = 'http://localhost:9515',
#    desired_capabilities={
#        "browserName" : 'chrome'
#    })
class git_test(TestCase):

    def test_login(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://github.com/login")

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[1]")
        elem.send_keys("totalflush")

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[2]")
        elem.send_keys("2gistesT")

        elem.submit()

        login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[2]/li[1]/a/span/span")
        span = login.get_attribute("class")
        self.assertEqual("css-truncate-target", span, "Login error!")
        driver.quit()

    def test_search(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("http://github.com/login")

        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[1]").send_keys("totalflush")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[2]").send_keys("2gistesT" + Keys.ENTER)

        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[4]/a").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/h1/a").get_attribute("a")
        self.assertTrue("GitHub Help" in driver.page_source, "Error link")
        driver.quit()

if __name__ == '__main__':
    unittest.main()
