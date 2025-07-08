class User:
    users = []

    def __init__(self, name, birthday, age, blood_type, address, gender):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.blood_type = blood_type
        self.address = address
        self.gender = gender
        self.users.append(self)

    @classmethod
    def find_by_name(cls, name):
        for user in cls.users:
            if user.name == name:
                return user
        return None