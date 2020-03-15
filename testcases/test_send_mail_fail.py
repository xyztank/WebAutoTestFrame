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
        ('', data.create_text(10), data.create_text(100), '请填写收件人地址后再发送'),
        ('123123', data.create_text(10), data.create_text(100), '以下邮箱地址无效，将无法成功收到邮件'),
        ('#@!123@qq.com', data.create_text(10), data.create_text(100), '请求错误'),
        ('18726024232', data.create_text(10), data.create_text(100), '以下邮箱地址无效，将无法成功收到邮件'),
    ])
    def test_send_mail_fail_container_illegal(self, user, title, content, expected):
        actual = self.mailpage.send_mail_fail(user, title, content, expected)
        self.mailpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, "发送邮件失败, 断言失败"

    @pytest.mark.parametrize('user,title,content,expected,action', [
        (data.create_email(), '', data.create_text(100), '确定真的不需要写主题吗？', '取消')
    ])
    def test_send_mail_fail_title_illegal(self, user, title, content, expected, action):
        actual = self.mailpage.send_mail_fail(user, title, content, expected, action)
        self.mailpage.logger.info(f'\n 断言信息：\n 实际值：{actual} \n 期望值：{expected}')
        with allure.step(f'校验结果：{actual}=={expected}'):
            assert actual == expected, "发送邮件失败, 断言失败"


if __name__ == '__main__':
    pytest.main(['-v', 'test_send_mail_success.py'])
