# 当前日期：2024-03-19
# 姓名：马云骥
# 梦想的度假胜地调查

# 存储调查结果的字典
dream_vacations = {}

# 开始调查
while True:
    name = input("您的名字是？（输入'quit'结束调查）")
    if name == 'quit':
        break
    place = input("如果您可以访问世界上的任何一个地方，您会选择哪里？")

    # 将调查结果存入字典
    dream_vacations[name] = place

# 打印调查结果
print("\n--- 调查结果 ---")
for name, place in dream_vacations.items():
    print(f"{name} 梦想访问的度假胜地是 {place}。")
