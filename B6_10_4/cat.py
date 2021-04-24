class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getName(self):
        return self.name

    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age


class Wallet:
    def __init__(self, client, balanse):
        self.client = client
        self.balanse = balanse

    def get_client(self):
        return self.client

    def get_balanse(self):
        return self.balanse


class Volonter:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status
