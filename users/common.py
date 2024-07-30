import hashlib
from enum import Enum
from month_4.lesson_4.file_manager import data_manager
from month_4.lesson_4.users.logs import log_decorator

Admin_login = "Admin"
Admin_password = "admin"


class UserTypes(str, Enum):
    ADMIN = "Admin"
    USER = "user"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_login = False

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_username(username):
        all_users = data_manager.read()
        for user in all_users:
            if user['username'] == username:
                return username


def register() -> bool:
    try:
        username = input("Enter username: ").capitalize().strip()
        if User.check_username(username):
            print("Username already exists")
            return register()
        password = input("Enter your password: ").strip()
        confirm_password = input("Enter your confirm password: ")

        student = User(username, password)
        if not student.check_password(confirm_password):
            print("Passwords do not match")
            return register()

        student.password = User.hash_password(password)
        data_manager.add_data(data=student.__dict__)
        print("🎉Successfully registered🎉")
        return True

    except Exception as e:
        print(f"Something went wrong {e}")
    return False


def find_user(username, password):
    all_users = data_manager.read()
    for user in all_users:
        if user['username'] == username and user['password'] == password:
            return True
    return False


@log_decorator
def login() -> dict[str, str] | bool:
    username = input("Enter username: ").capitalize().strip()
    password = input("Enter your password: ").strip()
    hashed_password = User.hash_password(password)
    if username == Admin_login and password == Admin_password:
        print("Welcome to Admin👮‍♂️")
        return {'user_type': UserTypes.ADMIN.value}
    elif find_user(username, hashed_password):
        data = data_manager.read()
        for user in data:
            if user['username'] == username and user['password'] == hashed_password:
                user['is_login'] = True
                data_manager.write(data)
                print(f'Welcome to the user menu: {username}🎉')
        return {'user_type': UserTypes.USER.value}
    else:
        return False


def logout():
    try:
        txt = """
Are you sure you want to exit😱? Yes or No
        """
        print(txt)
        choice = (input("Enter your answer: ").lower())
        if choice == "yes":
            read = data_manager.read()
            for user in read:
                user["is_login"] = False
                data_manager.write(read)
            return True
        else:
            print("Exit cancelled.")
            return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
