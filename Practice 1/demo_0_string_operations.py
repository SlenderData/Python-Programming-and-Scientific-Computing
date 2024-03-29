# 当前日期：2024-03-19
# 姓名：马云骥
# 处理字符串 "www.moe.gov.cn"

# 定义字符串变量
url = "www.moe.gov.cn"

# 1. 输出第一个字符
print("第一个字符:", url[0])

# 2. 输出第三个字符
print("第三个字符:", url[2])

# 3. 输出后三个字符
print("后三个字符:", url[-3:])

# 4. 输出字符串的总长度
print("字符串总长度:", len(url))

# 5. 输出字符 'o' 在字符串中第一个位置的索引值
print("字符 'o' 第一次出现的位置:", url.index("o"))

# 6. 输出字符 'o' 出现的总次数
print("字符 'o' 出现的总次数:", url.count("o"))

# 7. 将字符串中所有的 '.' 替换成 '-' 并输出
print("替换 '.' 为 '-' 后的字符串:", url.replace(".", "-"))

# 8. 将字符串中所有的字母全部替换为大写字母并输出
print("全部大写的字符串:", url.upper())

# 9. 删除字符串中的标点符号，把字符串拆分为四个字符串
print("分割后的字符串列表:", url.split("."))

# 10. 再次输出该字符串，观察字符串有没有变化
print("原始字符串:", url)
