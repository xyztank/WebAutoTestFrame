from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:
    def __init__(self, driver: WebDriver, logger):
        self.logger = logger
        self.driver = driver

    @allure.step('关闭浏览器')
    def driver_quit(self):
        self.logger.info('\n\n' + '*' * 20 + '关闭浏览器' + '*' * 20 + '\n')
        self.logger.stop()
        self.driver.quit()

    # 跳转iframe窗口
    @allure.step('跳转iframe窗口')
    def switch_to_iframe(self, locator):
        self.logger.info(f'跳转iframe窗口，元素定位：{locator}')
        WebDriverWait(self.driver, 10). \
            until(EC.frame_to_be_available_and_switch_to_it(locator))

    # 跳转iframe回到主窗口
    @allure.step('跳转iframe回到主窗口')
    def switch_default_content(self):
        self.logger.info('跳转默认主iframe窗口')
        self.driver.switch_to.default_content()

    # 查找元素
    @allure.step('查找元素')
    def find(self, locator):
        self.show_wait_find_element(locator)
        self.logger.info(f'查找元素：{locator}')
        return self.driver.find_element(*locator)

    # 查找并点击元素
    @allure.step('查找并点击元素')
    def find_and_click(self, locator):
        self.show_wait_find_element(locator)
        self.logger.info(f'查找并点击元素：{locator}')
        return self.driver.find_element(*locator).click()

    # 显示等待元素
    @allure.step('显示等待元素')
    def show_wait_find_element(self, locator):
        try:
            self.logger.info(f'显示等待元素：{locator}')
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except Exception as msg:
            return self.logger.debug(f'显示等待元素出错,出错信息为:{msg}')

    # 添加cookie
    @allure.step('添加cookie')
    def add_cookie_data(self, data):
        self.logger.info('添加cookie')
        return self.driver.add_cookie(data)

    # 刷新浏览器
    @allure.step('刷新浏览器')
    def driver_refresh(self):
        self.logger.info('刷新浏览器')
        self.driver.refresh()

    @allure.step('获得网页源码')
    def get_pagesource(self):
        return self.driver.page_source()

    @allure.step('获取网页url')
    def get_web_url(self):
        self.logger.info('获取网页url')
        return self.driver.current_url
