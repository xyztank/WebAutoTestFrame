import time
import pytest
import allure
from page.mainpage import MainPage


@allure.feature('测试用户登录成功')
class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.login_page = MainPage().login_no_cookie()
        cls.login_page.logger.info('\n\n' + '*' * 20 + '测试用户登录成功' + '*' * 20 + '\n')
        cls.login_page.click_login()
        time.sleep(1)
        cls.login_page.switch_iframe()
        time.sleep(1)

    @classmethod
    def teardown_class(cls):
        time.sleep(1)
        cls.login_page.quit()

    @pytest.mark.parametrize("username,password,expected", [
        ('用户名', '密码', '用户ID'),
    ])
    @allure.story('测试用户登录成功')
    def test_login_mail_success(self, username, password, expected):
        actual = self.login_page.login_by_password_success(username, password)
        self.login_page.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, '登录成功，断言失败'


if __name__ == '__main__':
    pytest.main(['-v', 'test_login_success.py'])
