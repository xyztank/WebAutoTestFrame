import time

import allure
import pytest
from page.mainpage import MainPage


@allure.feature('测试登录失败')
class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.login_page = MainPage().login_no_cookie()
        cls.login_page.logger.info('\n\n' + '*' * 20 + '测试登录失败' + '*' * 20 + '\n')

    @classmethod
    def teardown_class(cls):
        cls.login_page.quit()

    def setup(self):
        self.login_page.click_login()
        time.sleep(1)
        self.login_page.switch_iframe()
        time.sleep(1)

    def teardown(self):
        self.login_page.switch_default_content()
        time.sleep(1)
        self.login_page.return_click_login()
        time.sleep(1)

    @pytest.mark.parametrize("username,password,expected", [
        ('123123', '', '请输入密码'),
        ('', '123123', '请输入密码'),
        ('', '', '请输入帐号'),
        ('!@#123123', '123123', '请输入帐号'),
        ('18829021432', '12345678', '帐号格式错误'),
    ])
    def test_login_mail_fail(self, username, password, expected):
        actual = self.login_page.login_by_password_fail(username, password)
        self.login_page.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, "登录失败, 断言失败"
