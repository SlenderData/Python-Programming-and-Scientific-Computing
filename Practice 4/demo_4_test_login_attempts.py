# 当前日期：2024-03-19
# 姓名：马云骥
# 测试登录尝试次数

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


# 创建User实例
user = User('张', '三')

# 增加登录尝试次数
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"登录尝试次数: {user.login_attempts}")

# 重置登录尝试次数
user.reset_login_attempts()
print(f"重置后登录尝试次数: {user.login_attempts}")
