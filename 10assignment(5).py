class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        if self.password == input_password:
            return True
        else:
            return False
u = User("admin", "1234")
pwd = input("Enter Password: ")
if u.check_password(pwd):
    print("Password Correct")
else:
    print("Password Incorrect")