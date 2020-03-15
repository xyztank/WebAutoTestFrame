import random
import string
from faker import Faker


class CreateData(object):
    def __init__(self):
        self.faker = Faker('zh_CN')

    def create_pepole_name(self, sex):
        if sex == "female":
            return self.faker.name_female()
        elif sex == "male":
            return self.faker.name_male()
        else:
            print(f"没有这种{sex}性别")

    def create_text(self, num):
        return self.faker.text(max_nb_chars=num, ext_word_list=None)

    def create_phone_num(self):
        return self.faker.phone_number()

    def create_email(self):
        return self.faker.email()


if __name__ == '__main__':
    data = CreateData()
    print(data.create_text(100))
    print(data.create_phone_num())
    print(data.create_pepole_name('female'))
    print(data.create_email())
