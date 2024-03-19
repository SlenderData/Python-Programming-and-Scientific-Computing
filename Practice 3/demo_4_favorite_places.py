# 当前日期：2024-03-19
# 姓名：马云骥
# 喜欢的地方

favorite_places = {
    '小明': ['巴黎', '纽约'],
    '小红': ['伦敦'],
    '小刚': ['东京', '京都', '大阪']
}

for name, places in favorite_places.items():
    print(f"\n{name} 喜欢的地方有：")
    for place in places:
        print(f"- {place}")
