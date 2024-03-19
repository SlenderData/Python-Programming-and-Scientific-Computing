# 当前日期：2024-03-19
# 姓名：马云骥
# 定义User、Privileges和Admin类，包括登录尝试和显示权限

class User:
    # 表示一个用户
    def __init__(self, first_name, last_name):
        # 初始化用户
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        # 打印用户信息摘要
        print(f"\nName: {self.first_name} {self.last_name}")

    def greet_user(self):
        # 向用户发出问候
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        # 将登录尝试次数增加1
        self.login_attempts += 1

    def reset_login_attempts(self):
        # 将登录尝试次数重置为0
        self.login_attempts = 0

class Privileges:
    # 表示管理员权限的类

    def __init__(self, privileges=[]):
        # 初始化权限
        self.privileges = privileges

    def show_privileges(self):
        # 显示管理员的权限
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    # 表示管理员的类

    def __init__(self, first_name, last_name):
        # 初始化管理员
        super().__init__(first_name, last_name)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])
