# 当前日期：2024-03-19
# 姓名：马云骥
# 放眼世界

places = ['New Zealand 新西兰 🇳🇿', 'Norway 挪威 🇳🇴', 'Japan 日本 🇯🇵', 'Iceland 冰岛 🇮🇸', 'Canada 加拿大 🇨🇦']
print("原始列表:", places)

print("\n字母顺序:", sorted(places))
print("排序后的原始列表:", places)

print("\n字母逆序:", sorted(places, reverse=True))
print("逆序排序后的原始列表:", places)

places.reverse()
print("\n使用reverse()后的列表:", places)

places.reverse()
print("再次使用reverse()后的列表:", places)

places.sort()
print("\n使用sort()后的列表:", places)

places.sort(reverse=True)
print("使用sort(reverse=True)后的列表:", places)
