import allure
import pytest
from page.mainpage import MainPage
from utils.createdata import CreateData

data = CreateData()


@allure.feature('测试创建联系人成功')
class TestCreateContacter:

    @classmethod
    def setup_class(cls):
        cls.maillistpage = MainPage().to_maillist()
        cls.maillistpage.logger.info('\n\n' + '*' * 20 + '测试创建联系人成功' + '*' * 20 + '\n')

    @classmethod
    def teardown_class(cls):
        cls.maillistpage.driver_quit()

    @pytest.mark.parametrize('username,mail,phone,expected', [
        (data.create_pepole_name('male'), data.create_email(), data.create_phone_num(), '您已成功添加联系人'),
        (data.create_pepole_name('female'), data.create_email(), data.create_phone_num(), '您已成功添加联系人'),
        (data.create_pepole_name('female'), data.create_email(), data.create_phone_num(), '您已成功添加联系人'),
        (data.create_pepole_name('male'), data.create_email(), data.create_phone_num(), '您已成功添加联系人'),
    ])
    def test_create_contacter_success(self, username, mail, phone, expected):
        actual = self.maillistpage.create_contacter_success(username, mail, phone)
        self.maillistpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, "创建联系人成功, 断言失败"


if __name__ == '__main__':
    pytest.main(['-v', 'test_create_contacter_success.py'])
