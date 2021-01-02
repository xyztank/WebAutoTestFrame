import json
import os
import time

import allure
from selenium.webdriver.common.by import By
from driver.browser import Browser
from page.basepage import BasePage
from page.inboxpage import InBoxPage
from page.loginpage import LoginPage
from page.sendmailpage import SendMailPage
from page.maillistpage import MailListPage
from utils.mylog import MyLog


class MainPage(BasePage):
    _quit_locator = (By.XPATH, '//*[@id="_mail_component_120_120"]/a')  # 退出邮箱
    _maillist_locator = (By.XPATH, '//*[@id="_mail_tabitem_1_4text"]')  # 通讯录
    _inbox_locator = (By.XPATH, '//*[@id="_mail_tabitem_11_313text"]')  # 收件箱
    _sendmail_locator = (By.XPATH, '//span[text()="写 信"]')  # 写邮件按钮
    _close_label_locator = (By.XPATH, '//a[@title="点击关闭标签"]')

    def __init__(self):
        self._path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\\cookie'
        self.logger = MyLog().mylogger()
        self.open_browser()

    @allure.step('打开浏览器')
    def open_browser(self):
        self.logger.info('\n' + '*' * 20 + '打开浏览器' + '*' * 20 + '\n')
        self.driver = Browser().open_browser()

    # 点击关闭标签
    @allure.step('点击关闭标签')
    def click_close_label(self):
        self.logger.info('点击关闭标签')
        self.find_and_click(self._close_label_locator)
        return self

    # cookie写入文件
    @allure.step('cookie写入文件')
    def write_cookie_to_txt(self):
        try:
            self.logger.info('获取cookie')
            dict_cookies = self.driver.get_cookies()
            self.logger.info('将获取的cookie序列化')
            json_cookies = json.dumps(dict_cookies)
            print(json_cookies)
            with open(self._path, 'w') as f:
                self.logger.info('cookie写入文件')
                f.write(json_cookies)
        except Exception as e:
            self.logger.info(e)

    # 从文件中读cookie
    @allure.step('从文件中读cookie')
    def read_cookie_txt(self):
        try:
            with open(self._path, 'r', encoding='utf8') as f:
                self.logger.info('从文件中读cookie')
                list_cookies = json.loads(f.read())
            return list_cookies
        except Exception as e:
            self.logger.info(e)

    # 通过cookie登录
    @allure.step('通过cookie登录')
    def login_by_cookie(self):
        self.logger.info('通过cookie登录')
        list_cookies = self.read_cookie_txt()
        for cookie in list_cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        time.sleep(2)
        self.logger.info('刷新浏览器')
        self.driver.refresh()
        return self

    @allure.step('去登录页')
    def login_no_cookie(self):
        self.logger.info('去登录页')
        return LoginPage(self.driver, self.logger)

    # 回到登录页
    @allure.step('回到登录页')
    def to_login(self):
        self.login_by_cookie()
        self.find_and_click(self._quit_locator)
        return LoginPage(self.logger)

    # 去通讯录页面
    @allure.step('去通讯录页面')
    def to_maillist(self):
        self.login_by_cookie()
        self.logger.info('点击通讯录页面')
        self.find_and_click(self._maillist_locator)
        return MailListPage(self.driver, self.logger)

    # 去收件箱页面
    @allure.step('去收件箱页面')
    def to_inbox(self):
        self.login_by_cookie()
        self.logger.info('点击收件箱页面')
        self.find_and_click(self._inbox_locator)
        return InBoxPage(self.driver, self.logger)

    # 去写邮件
    @allure.step('去写邮件')
    def to_sendmailpage(self):
        self.login_by_cookie()
        self.logger.info('关闭广告标签')
        self.click_close_label()
        self.logger.info('点击去写邮件')
        self.find_and_click(self._sendmail_locator)
        return SendMailPage(self.driver, self.logger)
