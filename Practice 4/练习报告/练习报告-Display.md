# 第四课&emsp;课后练习

## 练习1：消息

### 题目叙述

&emsp;&emsp;创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为 `show_messages()` 的函数，这个函数会打印列表中的每条文本消息。编写一个名为 `send_messages()` 的函数，将每条消息都打印出来并移到一个名为 `sent_messages` 的列表中。调用函数 `send_messages()`，再将两个列表都打印出来，确认正确地移动了消息。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 显示和发送消息

def show_messages(messages):
    # 显示列表中的所有消息
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    # 打印每条消息，并将其移到新列表中
    while messages:
        current_message = messages.pop(0)  # 发送队首消息
        print(f"发送消息: {current_message}")
        sent_messages.append(current_message)


messages = ["Hello there!", "How are you?", "Welcome to Python programming."]
sent_messages = []

print("发送前原始消息列表:")
show_messages(messages)
print("")
send_messages(messages, sent_messages)
print("\n发送后原始消息列表:")
show_messages(messages)
print("\n已发送消息列表:")
show_messages(sent_messages)

```

### 结果输出

![截屏2024-04-09-13.47.32](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-51-26-50f36a5ae5e2206daa4fa041c795189d-截屏2024-04-09-13.47.32-f0fb65.png)

## 练习2：文件读写操作

### 题目叙述

&emsp;&emsp;编写程序将下列内容保存在文件 `score.txt` 中。

```
学号,平时成绩,期末成绩
9999180101,77,88
9999180102,91,85
9999180103,87,96
9999180104,70,68
9999180105,86,72
```

&emsp;&emsp;编写程序读取所有成绩，计算总评成绩（四舍五入到整数），其中

$$
总评成绩 = 平时成绩 \times 40 \% + 期末成绩 \times 60 \%
$$

&emsp;&emsp;最后按总评成绩降序排列后保存至一个新的文件内。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 处理学生的成绩数据

# 将学生学号及其总评成绩存储为对象
class StudentScore:
    def __init__(self, student_id, total_score):
        self.student_id = student_id
        self.total_score = total_score

    def __repr__(self):
        return f"StudentScore(student_id='{self.student_id}', total_score={self.total_score})"


# 将数据保存到文件中，使用utf-8编码
with open('score.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("学号,平时成绩,期末成绩\n")
    file_object.write("9999180101,77,88\n")
    file_object.write("9999180102,91,85\n")
    file_object.write("9999180103,87,96\n")
    file_object.write("9999180104,70,68\n")
    file_object.write("9999180105,86,72\n")
print()

# 读取数据并计算总评成绩，同样指定utf-8编码
students_scores = []
with open('score.txt', encoding='utf-8') as file_object:
    lines = file_object.readlines()

for line in lines[1:]:  # 跳过标题行
    student_id, regular_score, final_score = line.strip().split(',')
    total_score = round(int(regular_score) * 0.4 + int(final_score) * 0.6)
    students_scores.append(StudentScore(student_id, total_score))

# 按总评成绩降序排列
students_scores.sort(key=lambda x: x.total_score, reverse=True)

# 将排名后的成绩保存到新文件，再次使用utf-8编码
with open('sorted_scores.txt', 'w', encoding='utf-8') as file_object:
    file_object.write("学号,总评成绩\n")
    for student_score in students_scores:
        file_object.write(f"{student_score.student_id},{student_score.total_score}\n")

```

### 结果输出

![截屏2024-04-09-13.48.19](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-52-13-6666e8fca46d2580771f8ae263557a5a-截屏2024-04-09-13.48.19-42bf7d.png)

![截屏2024-04-09-13.48.53](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-52-34-1cb19218e746057a0772c53a32f6ce41-截屏2024-04-09-13.48.53-b603a2.png)

## 练习3：用户

### 题目叙述

&emsp;&emsp;创建一个名为 `User` 的类，其中包含属性 `first_name` 和 `last_name`，以及用户简介通常会存储的其他几个属性。在类 `User` 中定义一个名为 `describe_user()` 的方法，用于打印用户信息摘要。再定义一个名为 `greet_user()` 的方法，用于向用户发出个性化的问候。创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-04-09-13.49.19](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-53-12-9bd370d0b46dc24083fdab9f16b009e2-截屏2024-04-09-13.49.19-affeaf.png)

## 练习4：尝试登录次数

### 题目叙述

&emsp;&emsp;在为完成练习4-3而编写的 `User` 类中，添加一个名为 `login_attempts` 的属性。编写一个名为 `increment_login_attempts()` 的方法，将属性 `login_attempts` 的值加1。再编写一个名为 `reset_login_attempts()` 的方法，将属性 `login_attempts` 的值重置为0。根据 `User` 类创建一个实例，再调用方法 `increment_login_attempts()` 多次。打印属性 `login_attempts` 的值，确认它被正确地递增。然后，调用方法 `reset_login_attempts()`，并再次打印属性 `login_attempts` 的值，确认它被重置为0。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-04-09-13.49.33](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-54-52-356bc19f119604f3002cf671bea717f0-截屏2024-04-09-13.49.33-0a4c65.png)

## 练习5：管理员

### 题目叙述

&emsp;&emsp;管理员是一种特殊的用户。编写一个名为 `Admin` 的类，让它继承为完成练习4-3或练习4-4而编写的 `User` 类。添加一个名为 `privileges` 的属性，用于存储一个由字符串（如 "can add post"、"can delete post"、"can ban user" 等）组成的列表。编写一个名为 `show_privileges()` 的方法，显示管理员的权限。创建一个 `Admin` 实例，并调用这个方法。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 测试Admin类和权限

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


class Admin(User):
    # 表示管理员的类

    def __init__(self, first_name, last_name):
        # 初始化管理员
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        # 显示管理员的权限
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# 创建Admin实例
admin = Admin('李', '四')

# 显示权限
admin.show_privileges()

```

### 结果输出

![截屏2024-04-09-13.49.51](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-55-26-908145db1067963a806ee1718d891c5a-截屏2024-04-09-13.49.51-57bdda.png)

## 练习6：权限

### 题目叙述

&emsp;&emsp;编写一个名为 `Privileges` 的类，它只有一个属性 `privileges`，其中存储了练习4-5所述的字符串列表。将方法 `show_privileges()` 移到这个类中。在 `Admin` 类中，将一个 `Privileges` 实例用作其属性。创建一个 `Admin` 实例，并使用方法 `show_privileges()` 来显示其权限。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 测试Privileges类

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


# 创建Admin实例
admin = Admin('李', '四')

# 显示权限
admin.privileges.show_privileges()

```

### 结果输出

![截屏2024-04-09-13.50.01](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-55-40-5786015b467a6cdf05abcf00424dff09-截屏2024-04-09-13.50.01-8ac6e2.png)

## 练习7：导入Admin类

### 题目叙述

&emsp;&emsp;以为完成练习4-6而做的工作为基础。将 `User` 类、`Privileges` 类和 `Admin` 类存储在一个模块中，再创建一个文件，在其中创建一个 `Admin` 实例并对其调用方法 `show_privileges()`，以确认一切都能正确运行。

### 程序代码

**`users/__init__.py`：**

```python
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

```

**`demo_7_test_module_users.py`：**

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 从users模块导入Admin类，并测试其功能

from users import Admin

# 创建一个Admin实例
admin = Admin('王', '五')
# 显示管理员权限
admin.privileges.show_privileges()

```

### 结果输出

![截屏2024-04-09-13.50.17](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/04/09/13-56-34-bea8eeff365546fad2c12483b555b834-截屏2024-04-09-13.50.17-48d01c.png)
