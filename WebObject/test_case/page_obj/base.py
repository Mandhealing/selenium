class Page(object):

    '''
    基础类or主页类，用于页面对象类的继承
    open打开就是主页
    '''
    login_url = 'https://www.douguo.com/'
    url = ''

    def __init__(self, selenium_driver, base_url=login_url):
        if base_url[-1] !='/':
            base_url += '/'
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == self.base_url
        
    def _open(self, url):

        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on {}'.format(url)

    def open(self):

        self._open(self.url)

    def my_wait(self,timeout):
        return self.driver.implicitly_wait(timeout)

    def find_element(self, *loc):

        return self.driver.find_element(*loc)

    def find_elements(self, *loc):

        return self.driver.find_elements(*loc)