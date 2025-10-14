class User:

    def __init__(self, first_name,last_name,age,sex):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f"Our user is {self.first_name} {self.last_name} and they are {self.age} years old and they are a {self.sex}")

    def greet_user(self):
        print(f"Hello {self.first_name}!! We are glad you joined our site ")

    def increment_login_attempts(self):
        self.login_attempts +=1
    def reset_login_attempts(self):
        self.login_attempts = 0





user_1= User("Oise","Omoijuanfo", 29, "male")
user_2 = User("Joe", 'smith',46,"male")
user_3 = User("Bobert","smithius",35,"male")

user_1.greet_user()
user_1.describe_user()

user_3.describe_user()

user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.reset_login_attempts()
print(user_2.login_attempts)