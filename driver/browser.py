from selenium import webdriver


class Browser:

    def open_browser(self):
        url = 'https://mail.163.com/'
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver
