# class question:
#
#     def __init__(self, text, answer):
#
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001","joe")
#
# user_2 = User("002","bob")
#
#
#
# user_1.follow(user_2)
#
#
# print(user_1.followers)





class User:

    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1



user_1 = User("001","angela")



user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.followers)