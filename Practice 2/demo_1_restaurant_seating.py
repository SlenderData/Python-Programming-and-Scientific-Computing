# 当前日期：2024-03-19
# 姓名：马云骥
# 餐馆订位

# 询问用户用餐人数
number_of_guests = input("您有多少人用餐？")
number_of_guests = int(number_of_guests)

# 判断是否有空桌
if number_of_guests > 8:
    print("非常抱歉，目前没有空桌。")
else:
    print("有空桌，欢迎用餐。")
