# 当前日期：2024-03-19
# 姓名：马云骥
# 电影票价格

while True:
    age = input("请输入您的年龄（输入'quit'退出）：")
    if age.lower() == 'quit':
        break
    age = int(age)

    # 确定票价并打印
    if age < 3:
        print("您的票价是：免费。")
    elif age <= 12:
        print("您的票价是：10美元。")
    else:
        print("您的票价是：15美元。")
