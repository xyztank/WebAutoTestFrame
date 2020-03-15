import allure
from selenium.webdriver.common.by import By
from page.basepage import BasePage


class MailListPage(BasePage):
    _create_contacter = (By.XPATH, '//div[@role="toolbar"]//span[text()="新建联系人"]')  # 新建联系人按钮
    _username_locator = (By.XPATH, '//*[@id="input_N"]')  # 联系人姓名输入框
    _mail_locator = (By.XPATH, '//div[@id="iaddress_MAIL_wrap"]//input[@class="nui-ipt-input"]')  # 电子邮箱输入框
    _phone_locator = (By.XPATH, '//div[@id="iaddress_TEL_wrap"]//input[@class="nui-ipt-input"]')  # 电话输入框
    _sure_locator = (By.XPATH, '//span[text()="确 定"]')  # 确定按钮
    _create_success_tips_locator = (By.XPATH, '//*[text()="您已成功添加联系人"]')  # 删除成功后响应消息

    _delete_locator = (By.XPATH, '//span[text()="删 除"]')  # 删除按钮
    _delete_all_checkbox_locator = (By.XPATH, '//b[@id="fly0"]')  # 选择全部checkbox，删除全部联系人
    _delete_first_checkbox_locator = (
        By.XPATH, '//tbody[@class="nui-table-body"]//tr[1]/td[2]//b')  # 选中第一个checkbox，删除第一个联系人
    _delete_contacter_popup_locator = (By.XPATH, '//*[contains(@id,"_mail_msgbox")]/div[2]/div/div/div')  # 点击删除弹出对话框
    _delete_contacter_sure_locator = (By.XPATH, '//span[text()="确 定"]')  # 确定按钮
    _delete_contacter_tips_locator = (By.XPATH, '//*[text()="您已成功删除联系人"]')  # 删除成功后响应消息

    # 点击创建新建联系人按钮
    @allure.step('点击创建新建联系人按钮')
    def _click_create_contacter_button(self):
        self.logger.info('点击创建新建联系人按钮')
        return self.find_and_click(self._create_contacter)

    # 输入用户名
    @allure.step('输入用户名')
    def _input_username(self, username):
        self.logger.info(f'输入用户名：{username}')
        return self.find(self._username_locator).send_keys(username)

    # 输入邮箱地址
    @allure.step('输入邮箱地址')
    def _input_mail(self, mail):
        self.logger.info(f'输入邮箱地址：{mail}')
        return self.find(self._mail_locator).send_keys(mail)

    # 输入电话
    @allure.step('输入电话')
    def _input_phone(self, phone):
        self.logger.info(f'输入电话：{phone}')
        return self.find(self._phone_locator).send_keys(phone)

    # 点击确认添加联系人
    @allure.step('点击确认添加联系人')
    def _click_create_contacter_sure_button(self):
        self.logger.info('点击确认添加联系人按钮')
        return self.find_and_click(self._sure_locator)

    # 获取成功添加联系人tips
    @allure.step('获取成功添加联系人tips')
    def _get_create_contacter_success_tips(self):
        self.logger.info('获取成功添加联系人tips')
        return self.find(self._create_success_tips_locator).text

    # 点击删除联系人按钮
    @allure.step('点击删除联系人按钮')
    def _click_delete_contacter(self):
        self.logger.info('点击删除联系人按钮')
        return self.find_and_click(self._delete_locator)

    # 选中全部checkbox，选中全部联系人
    @allure.step('选中全部checkbox，选中全部联系人')
    def _select_checkbox_delete_all_contacter(self):
        self.logger.info('选中全部checkbox，选中全部联系人')
        return self.find_and_click(self._delete_all_checkbox_locator)

    # 选中第一个checkbox，选中第一个联系人
    @allure.step('选中第一个checkbox，选中第一个联系人')
    def _select_checkbox_delete_first_contacter(self):
        self.logger.info('选中第一个checkbox，选中第一个联系人')
        return self.find_and_click(self._delete_first_checkbox_locator)

    # 点击确认删除联系人
    @allure.step('点击确认删除联系人')
    def _click_delete_contacter_sure_button(self):
        self.logger.info('点击确认删除联系人')
        return self.find_and_click(self._delete_contacter_sure_locator)

    # 获取成功删除联系人tips
    @allure.step('获取成功删除联系人tips')
    def _get_delete_contacter_success_tips(self):
        self.logger.info('获取成功删除联系人tips')
        return self.find(self._delete_contacter_tips_locator).text

    # 业务层
    # 成功创建联系人
    @allure.story('成功创建联系人')
    def create_contacter_success(self, username, mail, phone):
        self._click_create_contacter_button()
        self._input_username(username)
        self._input_mail(mail)
        self._input_phone(phone)
        self._click_create_contacter_sure_button()
        return self._get_create_contacter_success_tips()

    # 成功删除一个联系人
    @allure.story('成功删除一个联系人')
    def delete_contacter_success_first(self):
        self._select_checkbox_delete_first_contacter()
        self._click_delete_contacter()
        self._click_create_contacter_sure_button()
        return self._get_delete_contacter_success_tips()

    # 成功删除全部联系人
    @allure.story('成功删除全部联系人')
    def delete_contacter_success_all(self):
        self._select_checkbox_delete_all_contacter()
        self._click_delete_contacter()
        self._click_create_contacter_sure_button()
        return self._get_delete_contacter_success_tips()
