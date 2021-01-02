from selenium.webdriver.common.by import By
from page.basepage import BasePage
import allure


class LoginPage(BasePage):
    # 对象层
    _lbNormal_locator = (By.XPATH, '//*[@id="lbNormal"]')  # 点击密码登录
    _iframe_locator = (By.XPATH, '//div[@id="loginDiv"]/iframe')  # 跳转iframe
    _email_locator = (By.NAME, 'email')  # 输入用户名
    _password_locator = (By.NAME, 'password')  # 输入密码
    _dologin_locator = (By.ID, 'dologin')  # 点击登录
    _error_locator = (By.XPATH, '//div[@class="ferrorhead"]')  # 获取点击登录时的提示信息
    _lbApp_locator = (By.XPATH, '//*[@id="lbApp"]')  # 返回主iframe
    _unlogin = (By.XPATH, '//input[@id="un-login"]')  # 点击十天内免登录
    _userid_locator = (By.XPATH, '//span[@id="spnUid"]')  # 登录成功后用户ID

    # 操作层
    def quit(self):
        self.driver_quit()

    def to_mainpage(self):
        from page.mainpage import MainPage
        return MainPage()

    # 获取登录提示信息
    @allure.step('获取登录提示信息')
    def _get_error_text(self):
        self.logger.info('获取登录提示信息')
        return self.find(self._error_locator).text

    # 获取用户ID信息
    @allure.step('获取用户ID信息')
    def _get_userid(self):
        self.logger.info('获取用户ID信息')
        return self.find(self._userid_locator).text

    @allure.step('获取登录提示信息')
    def _login_by_wexin(self):
        pass

    @allure.step('输入用户名')
    def _input_username(self, username):
        self.logger.info('清空数据')
        self.find(self._email_locator).clear()
        self.logger.info(f'输入用户名称:{username}')
        self.find(self._email_locator).send_keys(username)

    @allure.step('输入密码')
    def _input_password(self, password):
        self.logger.info('清空数据')
        self.find(self._password_locator).clear()
        self.logger.info(f'输入用户密码:{password}')
        self.find(self._password_locator).send_keys(password)

    # 点击登录按钮
    @allure.step('点击登录按钮')
    def _click_login_button(self):
        self.logger.info('点击登录按钮')
        self.find_and_click(self._dologin_locator)
        return self

    # 点击通过密码方式登录
    @allure.step('点击通过密码方式登录')
    def click_login(self):
        self.logger.info('点击通过密码方式登录')
        # self.find_and_click(self._lbNormal_locator)

    # 回到扫描登录页
    @allure.step('回到扫描登录页')
    def return_click_login(self):
        self.logger.info('回到扫描登录页')
        self.find_and_click(self._lbApp_locator)

    # 切换至iframe
    @allure.step('切换至iframe')
    def switch_iframe(self):
        self.logger.info('切换至iframe')
        self.switch_to_iframe(self._iframe_locator)

    # 切换回主iframe
    @allure.step('切换回主iframe')
    def switch_to_content(self):
        self.logger.info('切换回主iframe')
        self.switch_default_content()

    # 业务层
    @allure.story('通过用户名密码登录')
    def login_by_password_fail(self, username, password):
        self._input_username(username)
        self._input_password(password)
        self._click_login_button()
        return self._get_error_text()

    @allure.story('通过用户名密码登录')
    def login_by_password_success(self, username, password):
        self.get_web_url()
        self._input_username(username)
        self._input_password(password)
        self._click_login_button()
        return self._get_userid()
