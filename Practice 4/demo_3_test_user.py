# 当前日期：2024-03-19
# 姓名：马云骥
# 测试User类

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


# 创建User实例
user1 = User('李', '雷')
user2 = User('韩', '梅梅')

# 调用方法
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
