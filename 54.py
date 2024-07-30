import getpass


def user():
    return getpass.getuser()



user_name = user()
print(f"Username: {user_name}")