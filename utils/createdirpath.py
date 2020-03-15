import os
from datetime import datetime, date


class CreateDirPath:
    _BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    @staticmethod
    def get_current_time():
        """获取当前日期"""
        current_time = datetime.now().strftime(str(date.today()) + '_' + '%H-%M-%S')
        return current_time

    @staticmethod
    def get_current_date():
        """获取当前日期"""
        current_date = datetime.now().strftime(str(date.today()))
        return current_date

    def file_name(self, file_type):
        """日志与HTML报告文件名"""
        current_time = self.get_current_time()
        if 'HTML' == file_type.upper():
            current_time = self.get_current_time()
            file_name = current_time + '.' + file_type
            return file_name
        elif 'LOG' == file_type.upper():
            current_time = self.get_current_date()
            file_name = current_time + 'testing' + '.' + file_type
            return file_name
        else:
            return current_time + '.' + file_type

    @staticmethod
    def create_dir(file_type):
        """创建HTML报告与日志文件存放目录"""
        if not os.path.exists(CreateDirPath._BASE_DIR + '/' + file_type):
            os.makedirs(CreateDirPath._BASE_DIR + '/' + file_type)
        return CreateDirPath._BASE_DIR


if __name__ == '__main__':
    # print(CreateDirPath.create_dir('log'))
    # print(CreateDirPath.create_dir('report'))
    # print(CreateDirPath.file_name('html'))
    # print(CreateDirPath.get_current_time())
    # print(CreateDirPath.get_current_date())
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\\cookie')
