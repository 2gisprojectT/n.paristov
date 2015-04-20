__author__ = 'whitefoxnsk'
from base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '/html/body/div[2]/div[4]/div[3]/div[1]',
        'input': '/html/body/div[2]/div[4]/div[3]/div[1]/form/div/div[2]/label',
        'submit': '/html/body/div[2]/div[4]/div[3]/div[1]/form/div/div[1]/span'
    }

    def search(self, query):
        self.driver.find_element_by_xpath(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_xpath(self.selectors['submit']).submit()