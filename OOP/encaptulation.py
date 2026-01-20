class User:
    def __init__(self,username, password):
        self.username = username
        self.__password = password

    def check_password(self, checkPassword):
        return self.__password == checkPassword
    
    def change_password(self, oldPassword, newPassword):
        if self.__password == oldPassword:
            self.__password = newPassword


u = User("saurav", "12345")

print(u.check_password("12345"))
u.change_password("12345","abcd")
print(u.check_password("abcd"))