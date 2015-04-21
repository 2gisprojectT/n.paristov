__author__ = 'whitefoxnsk'

from base_component import BaseComponent


class Sign_In(BaseComponent):

    selectors = {
        'self': '/html/body/div[1]/div[1]/div/div[1]',
        'button': '/html/body/div[1]/div[1]/div/div[1]/a[2]',
    }

    def button_click(self):
        self.driver.find_element_by_xpath(self.selectors['button']).click()
        # self.driver.click()