import allure
import pytest
from page.mainpage import MainPage


@allure.feature('测试删除联系人成功')
class TestDeleteContacter:
    @classmethod
    def setup_class(cls):
        cls.maillistpage = MainPage().to_maillist()
        cls.maillistpage.logger.info('\n\n' + '*' * 20 + '测试删除联系人成功' + '*' * 20 + '\n')

    @classmethod
    def teardown_class(cls):
        cls.maillistpage.driver_quit()

    def test_delete_first_contacter_success(self):
        actual = self.maillistpage.delete_contacter_success_first()
        self.maillistpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：您已成功删除联系人')
        with allure.step(f'校验结果：{actual}=="您已成功删除联系人"'):
            assert actual == '您已成功删除联系人', "删除一个联系人成功, 断言失败"

    def test_delete_all_contacter_success(self):
        actual = self.maillistpage.delete_contacter_success_all()
        self.maillistpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：您已成功删除联系人')
        with allure.step(f'校验结果：{actual}=="您已成功删除联系人"'):
            assert actual == '您已成功删除联系人', "测试删除所有联系人成功, 断言失败"


if __name__ == '__main__':
    pytest.main(['-v', 'test_delete_contacter_success.py'])
