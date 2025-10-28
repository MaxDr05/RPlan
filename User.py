# 编写一个User🥱
class User(object):
    #定义用户属性
    __slots__ = ['_name', '_email', '_password','_gender','_city']

    #初始化
    def __init__(self,name,email,password,gender,city):
        self._name = name
        self._email = email
        self._password = password
        self._gender = gender
        self._city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    def printUser(self):
        print(self._name)
        print(self._email)
        print(self._password)
        print(self._gender)
        print(self._city)
