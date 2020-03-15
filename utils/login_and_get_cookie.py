import json
import time
from loguru import logger
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginAndGetCookie:
    _lbNormal_locator = (By.XPATH, '//*[@id="lbNormal"]')  # 点击密码登录
    _iframe_locator = (By.XPATH, '//div[@id="loginDiv"]/iframe')  # 跳转iframe
    _email_locator = (By.NAME, 'email')  # 输入用户名
    _password_locator = (By.NAME, 'password')  # 输入密码
    _dologin_locator = (By.ID, 'dologin')  # 点击登录
    _error_locator = (By.XPATH, '//div[@class="ferrorhead"]')  # 获取点击登录时的提示信息
    _lbApp_locator = (By.XPATH, '//*[@id="lbApp"]')  # 返回主iframe
    _unlogin = (By.XPATH, '//input[@id="un-login"]')  # 点击十天内免登录

    _send_locator = (By.XPATH, '//header//span[text()="发送"]')  # 发送按钮
    _cancel_locator = (By.XPATH, '//span[text()="取 消"]')  # 取消按钮
    _save_locator = (By.XPATH, '//span[text()="存草稿"]')  # 保存按钮
    _container_locator = (By.XPATH, "//input[contains(@class,'nui-editableAddr-ipt')]")  # 收件人框
    _title_locator = (By.XPATH, "//input[contains(@id,'_subjectInput')]")  # 邮件主题
    _mailiframe_locator = (By.XPATH, '//div[@class="APP-editor-edtr"]/iframe')  # 邮件内容iframe
    _emailcontent_locator = (By.XPATH, '/html/body')  # 写邮件内容

    _sendmail_locator = (By.XPATH, '//span[text()="写 信"]')  # 写邮件按钮

    # 打开浏览器
    def __init__(self):
        self._dirpath = '../data/cookie'
        self._url = 'https://mail.163.com/'
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.get(self._url)

    # 关闭浏览器
    def _quit(self):
        self._driver.quit()

    # 显示等待
    def _show_wait_find_element(self, locator):
        try:
            return WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located(*locator))
        except Exception as msg:
            return self.logger.debug(msg)

    # 跳转iframe
    def _switch_to_iframe(self, locator):
        WebDriverWait(self._driver, 10). \
            until(EC.frame_to_be_available_and_switch_to_it(locator))

    # 定位元素
    def _find(self, locator):
        self._show_wait_find_element(locator)
        time.sleep(1)
        return self._driver.find_element(*locator)

    # 登录
    def _login(self, username, password):
        self._find(self._lbNormal_locator).click()
        self._switch_to_iframe(self._iframe_locator)
        self._find(self._email_locator).send_keys(username)
        self._find(self._password_locator).send_keys(password)
        self._find(self._unlogin).click()
        self._find(self._dologin_locator).click()
        time.sleep(3)

    # cookie写入文件
    def _write_cookie_to_txt(self):
        dictCookies = self._driver.get_cookies()
        jsonCookies = json.dumps(dictCookies)
        print(jsonCookies)
        with open(self._dirpath, 'w') as f:
            f.write(jsonCookies)

    # 从文件中读cookie
    def _read_cookie_txt(self):
        with open(self._dirpath, 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())
        return listCookies

    # 登录并获取cookie
    def login_get_cookie(self):
        self._login('用户名', '密码')
        self._write_cookie_to_txt()
        self._quit()

    # 通过cookie登录
    def login_by_cookie(self):
        listCookies = self._read_cookie_txt()
        for cookie in listCookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self._driver.add_cookie(cookie)
        time.sleep(3)
        self._driver.refresh()

    # 点击发送邮件按钮
    def _click_send_email(self):
        from page.mainpage import MainPage
        self._find(self._send_locator).click()
        return MainPage()

    def focus(self, locator):
        element = self._find(locator)
        self._driver.execute_script("arguments[0].focus();", element)

    # 输入邮件联系人
    def _input_mail_container(self, user):
        self._find(self._container_locator).send_keys(user)
        return self

    # 输入邮件标题
    def _input_mail_title(self, title):
        self._find(self._title_locator).send_keys(title)
        return self

    # 输入邮件内容
    def _input_mail_content(self, content):
        self._find(self._emailcontent_locator).send_keys(content)
        return self

    # 业务层
    # 邮件发送成功
    def send_mail_success(self, user, title, content):
        """
        1、输入邮箱联系人
        2、输入邮件标题
        3、切换至邮件内容iframe
        4、输入邮件内容
        5、点击发送邮件
        :param user:邮件联系人
        :param title: 邮件标题
        :param content: 邮件内容
        :return: 邮箱主页面
        """
        self._find(self._sendmail_locator).click()
        self._input_mail_container(user)
        self._input_mail_title(title)
        self._switch_to_iframe(self._mailiframe_locator)
        self._input_mail_content(content)
        self._click_send_email()


if __name__ == '__main__':
    gologin = LoginAndGetCookie()
    # gologin.login_get_cookie()
    gologin.login_by_cookie()
    gologin.send_mail_success('123', '123', '123123')
