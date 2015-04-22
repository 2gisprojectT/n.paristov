__author__ = 'whitefoxnsk'

from base_component import BaseComponent


class Login(BaseComponent):

    selectors = {
        'self': '/html/body/div[1]/div[3]/div[1]/div/form/div[3]',
        'field_login': '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[1]',
        'field_password': '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[2]',
        'submit': '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input[3]'
    }

    def login(self, login, password):
        self.driver.find_element_by_xpath(self.selectors['field_login']).send_keys(login)
        self.driver.find_element_by_xpath(self.selectors['field_password']).send_keys(password)
        self.driver.find_element_by_xpath(self.selectors['submit']).submit()