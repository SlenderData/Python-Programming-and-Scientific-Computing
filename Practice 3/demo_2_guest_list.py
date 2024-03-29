# 当前日期：2024-03-19
# 姓名：马云骥
# 嘉宾名单

# 初始名单
guests = ['居里夫人', '爱因斯坦', '牛顿']
for guest in guests:
    print(f"{guest}，诚挚邀请您参加晚宴。")

# 修改嘉宾名单
print(f"\n遗憾地得知{guests[2]}无法赴约。")
guests[2] = '特斯拉'
for guest in guests:
    print(f"{guest}，诚挚邀请您参加晚宴。")

# 添加嘉宾
print("\n好消息！我们找到了一个更大的餐桌。")
guests.insert(0, '爱迪生')
guests.insert(2, '阿达·洛夫莱斯')
guests.append('达尔文')
for guest in guests:
    print(f"{guest}，诚挚邀请您参加晚宴。")

# 缩减名单
print("\n非常抱歉，新的餐桌无法及时送达，只能邀请两位嘉宾。")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"{removed_guest}，很遗憾无法邀请您参加本次晚宴。")
for guest in guests:
    print(f"{guest}，您依然在邀请名单中。")

# 删除剩余嘉宾
del guests[0:2]
print(guests)
