__author__ = 'whitefoxnsk'

from base_component import BaseComponent


class git_help(BaseComponent):

    selectors = {
        'self': '/html/body/div[1]/div[1]/div',
        'click': '/html/body/div[1]/div[1]/div/ul[1]/li[4]/a',
    }

    def help(self):
        self.driver.find_element_by_xpath(self.selectors['click']).click()
