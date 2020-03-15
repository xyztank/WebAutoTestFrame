import allure
import pytest
from page.mainpage import MainPage
from utils.createdata import CreateData

data = CreateData()


@allure.feature('测试发送邮件失败')
class TestSendMail:
    @classmethod
    def setup_class(cls):
        cls.mailpage = MainPage().to_sendmailpage()
        cls.mailpage.logger.info('\n\n' + '*' * 20 + '测试发送邮件失败' + '*' * 20 + '\n')

    @classmethod
    def teardown_class(cls):
        cls.mailpage.quit()

    @pytest.mark.parametrize('user,title,content,expected', [
        (data.create_email(), '', data.create_text(100), '发送成功手机收发邮件更方便'),
        (data.create_email(), data.create_text(10), data.create_text(100), '发送成功手机收发邮件更方便')
    ])
    def test_send_mail_success(self, user, title, content, expected):
        actual = self.mailpage.send_mail_success(user, title, content)
        self.mailpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, "发送邮件成功, 断言失败"


if __name__ == '__main__':
    pytest.main(['--alluredir=' + './report/', 'test_send_mail_success.py', '--clean'])
