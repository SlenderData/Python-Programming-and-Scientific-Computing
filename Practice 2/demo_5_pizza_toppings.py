# 当前日期：2024-03-19
# 姓名：马云骥
# 比萨配料

print("请输入比萨配料：")
while True:
    topping = input("配料（输入'quit'结束）：")
    if topping == 'quit':
        break
    else:
        print(f"我们会在比萨中添加{topping}配料。")
