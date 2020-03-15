import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.basepage import BasePage


class SendMailPage(BasePage):
    _mainpage_locator = (By.XPATH, '//div[text()="首页"]')  # 发送按钮
    _writemail_locator = (By.XPATH, '//span[text()="写 信"]')  # 写邮件按钮
    _send_locator = (By.XPATH, '//header//span[text()="发送"]')  # 发送按钮
    _cancel_locator = (By.XPATH, '//span[text()="取 消"]')  # 取消按钮
    _save_locator = (By.XPATH, '//span[text()="存草稿"]')  # 保存按钮
    _container_locator = (By.XPATH, "//input[contains(@class,'nui-editableAddr-ipt')]")  # 收件人框
    _title_locator = (By.XPATH, "//input[contains(@id,'_subjectInput')]")  # 邮件主题
    _mailiframe_locator = (By.XPATH, '//div[@class="APP-editor-edtr"]/iframe')  # 邮件内容iframe
    _emailcontent_locator = (By.XPATH, '/html/body')  # 写邮件内容
    _send_mail_success_response_locator = (By.XPATH, '//*[contains(@id,"_succInfo")]')  # 发送后系统返回消息
    _no_container_response_locator = (By.XPATH, '//span[text()="请填写收件人地址后再发送"]')  # 无发件人发送后系统返回消息
    _no_title_response_locator = (By.XPATH, '//div[contains(@class,"nui-msgbox-title")]')  # 无标题发送后系统返回消息
    _container_illegal_response_locator = (By.XPATH, '//div[contains(@class,"nui-msgbox-title")]')  # 邮件地址非法发送后系统返回消息
    _container_illegal_return_locator = (By.XPATH, '//span[text()="返回编辑"]')  # 返回编辑
    _request_error_sure_locator = (By.XPATH, '//span[text()="确 定"]')
    _request_error_cancel_locator = (By.XPATH, '//div[@class="nui-msgbox-ft-btns"]//span[text()="取 消"]')
    _close_label_locator = (By.XPATH, '//a[@title="点击关闭标签"]')

    def quit(self):
        self.logger.info('关闭浏览器')
        self.driver_quit()

    # 点击关闭标签
    @allure.step('点击关闭标签')
    def click_close_label(self):
        self.logger.info('点击关闭标签')
        self.find_and_click(self._close_label_locator)
        return self

    # 点击写邮件按钮
    @allure.step('点击写邮件按钮')
    def click_write_mail(self):
        self.logger.info('点击写邮件按钮')
        self.find_and_click(self._writemail_locator)

    # 点击首页按钮
    @allure.step('点击首页按钮')
    def click_mainpage(self):
        self.logger.info('点击首页按钮')
        return self.find_and_click(self._mainpage_locator)

    # 点击发送邮件按钮
    @allure.step('点击发送邮件按钮')
    def _click_send_email(self):
        self.logger.info('点击发送邮件按钮')
        return self.find_and_click(self._send_locator)

    # 点击确认按钮
    @allure.step('点击确认按钮')
    def _click_request_error_sure_button(self):
        self.logger.info('点击确认按钮')
        return self.find_and_click(self._request_error_sure_locator)

    # 点击取消按钮
    @allure.step('点击取消按钮')
    def _click_request_error_cancel_button(self):
        self.logger.info('点击取消按钮')
        return self.find_and_click(self._request_error_cancel_locator)

    # 点击保存邮件按钮
    @allure.step('点击保存邮件按钮')
    def _click_save_email(self):
        self.logger.info('点击保存邮件按钮')
        return self.find_and_click(self._save_locator)

    # 点击取消发送邮件按钮
    @allure.step('点击取消发送邮件按钮')
    def _click_cancel_send_email(self):
        self.logger.info('点击取消发送邮件按钮')
        return self.find_and_click(self._cancel_locator)

    # 返回编辑
    @allure.step('返回编辑')
    def _click_return_and_edit(self):
        self.logger.info('返回编辑')
        return self.find_and_click(self._container_illegal_return_locator)

    # 输入邮件联系人
    @allure.step('输入邮件联系人')
    def _input_mail_container(self, user):
        self.logger.info('输入邮件联系人')
        self.find(self._container_locator).send_keys(user)
        return self

    # 删除邮件联系人
    @allure.step('删除邮件联系人')
    def _backspce_mail_container(self):
        self.logger.info('删除邮件联系人')
        self.find(self._container_locator).send_keys(Keys.BACKSPACE)
        return self

    # 输入邮件标题
    @allure.step('输入邮件标题')
    def _input_mail_title(self, title):
        self.logger.info('清除内容')
        self.find(self._title_locator).clear()
        self.logger.info(f'输入邮件标题:{title}')
        self.find(self._title_locator).send_keys(title)
        return self

    # 输入邮件内容
    @allure.step('输入邮件内容')
    def _input_mail_content(self, content):
        self.logger.info('清除内容')
        self.find(self._emailcontent_locator).clear()
        self.logger.info(f'输入邮件内容:{content}')
        self.find(self._emailcontent_locator).send_keys(content)
        return self

    # 获取无发件人时的响应
    @allure.step('获取无发件人时的响应')
    def _get_no_container_response(self):
        self.logger.info('获取无发件人时的响应')
        return self.find(self._no_container_response_locator).text

    # 获取输入错误格式发件人时的响应
    @allure.step('获取输入错误格式发件人时的响应')
    def _get_container_illegal_response(self):
        self.logger.info('获取输入错误格式发件人时的响应')
        return self.find(self._container_illegal_response_locator).text

    # 获取无邮件标题时的响应
    @allure.step('获取无邮件标题时的响应')
    def _get_no_title_response(self):
        self.logger.info('获取无邮件标题时的响应')
        return self.find(self._no_title_response_locator).text

    # 业务层
    # 邮件发送成功
    @allure.story('邮件发送成功')
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
        self._input_mail_container(user)
        self._input_mail_title(title)
        self.switch_to_iframe(self._mailiframe_locator)
        self._input_mail_content(content)
        self.switch_default_content()
        self._click_send_email()
        if title == "":
            self._click_request_error_sure_button()
            actual = self.find(self._send_mail_success_response_locator).text
            self.click_close_label()
            self.click_mainpage()
            self.click_write_mail()
            return actual
        else:
            return self.find(self._send_mail_success_response_locator).text

    # 邮件发送失败
    @allure.story('邮件发送失败')
    def send_mail_fail(self, user, title, content, expected, action=None):
        self._backspce_mail_container()
        self._input_mail_container(user)
        self._input_mail_title(title)
        self.switch_to_iframe(self._mailiframe_locator)
        self._input_mail_content(content)
        self.switch_default_content()
        self._click_send_email()
        if user == "":
            return self._get_no_container_response()
        elif title == "" and action == None:
            actual = self._get_no_title_response()
            self._click_return_and_edit()
            return actual
        elif title == "" and action == "取消":
            actual = self._get_no_title_response()
            self._click_request_error_cancel_button()
            return actual
        elif expected == "请求错误":
            actual = self._get_container_illegal_response()
            self._click_request_error_sure_button()
            return actual
        else:
            actual = self._get_container_illegal_response()
            self._click_return_and_edit()
            return actual

    # 邮件保存成功
    @allure.story('邮件保存成功')
    def save_send_mail_success(self, user, title, content):
        self._input_mail_container(user)
        self._input_mail_title(title)
        self.switch_to_iframe(self._mailiframe_locator)
        self._input_mail_content(content)
        self._click_save_email()

    # 取消发送
    @allure.story('取消发送')
    def cancel_send_mail_success(self, user, title, content):
        self._input_mail_container(user)
        self._input_mail_title(title)
        self.switch_to_iframe(self._mailiframe_locator)
        self._input_mail_content(content)
        self._click_cancel_send_email()
