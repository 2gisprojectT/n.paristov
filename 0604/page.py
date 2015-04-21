__author__ = 'whitefoxnsk'


class Page():
    def __init__(self, driver):

        self.driver = driver
        self._git_help = None
        self._sign_in = None
        self._login = None

    def git_help(self):
        from git_help import git_help

        if self._git_help is None:
            self._git_help = git_help(self.driver, self.driver.find_element_by_xpath(git_help.selectors['self']))
        return self._git_help

    def sign_in(self):
        from sign_in import Sign_In

        if self._sign_in is None:
            self._sign_in = Sign_In(self.driver, self.driver.find_element_by_xpath(Sign_In.selectors['self']))  #

        return self._sign_in

    def login(self):
        from login import Login
        if self._login is None:
            self._login = Login(self.driver, self.driver.find_element_by_xpath(Login.selectors['self']))

        return self._login

    @property
    def title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)
