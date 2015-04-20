__author__ = 'whitefoxnsk'


class Page():
    def __init__(self, driver):

        self.driver = driver
        self._search_bar = None

    @property
    def search_bar(self):
        from search_bar import SearchBar

        if self._search_bar is None:
            self._search_bar = SearchBar(self.driver, self.driver.find_element_by_xpath(SearchBar.selectors['self']))
        return self._search_bar

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def open(self, url):
        self.driver.get(url)