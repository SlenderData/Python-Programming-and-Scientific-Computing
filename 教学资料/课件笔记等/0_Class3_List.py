#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ## **第3课 列表字典与元组**

# **§3.1 列表与元素访问  
# §3.2 操作列表元素  
# §3.3 操作列表  
# §3.4 字典  
# §3.5 元组**

# ### **§3.1 列表与元素访问**

# #### **1.简介列表**

# **I. 列表(list) 由一系列按特定顺序排列的元素组成。**  
# 
# **II. 将一组相关数据放在一对方括号“[]”中即定义了一个列表。**
# 
# **III. 方括号中的每个数据称为元素，元素和元素之间用“，”隔开。  
#      元素的个数称为列表的长度。**  
#      
# **IV. 列表也允许当元素。**

# **创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。**

# In[ ]:


## 列表的建立
list1 = ['python', 'ShowMeAI', 1997, 2022]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list1
list2
list3


# #### **2.元素访问 -- 索引和切片**

# **要访问列表元素，可指出列表的名称，再指出元素的索引，并将后者放在方括号内**

# In[ ]:


list2 = [1, 2, 3, 4, 5]
list2[2]


# **列表元素的索引是从0开始，向右依次加1进行编号的。  
# 列表元素也有正向和反向两种索引方式。**

# ||'S'| 'h'| 'o'| 'w'| 'M'| 'e'| 'A'| 'I'|
# |---|---|---|---|---|---|---|---|---|
# |正向索引|0|1|2|3|4|5|6|7|
# |反向索引|-8|-7|-6|-5|-4|-3|-2|-1|

# In[ ]:


list3 = ['S', 'h', 'o', 'w', 'M', 'e', 'A', 'I']
list3[1:3]
list3[:4]
list3[6:]
list3[:]


# ### **动手试一试1 List**

# **练习1：问候语 将一些朋友的姓名存储在一个列表中，并将其命名为names。  
# 依次访问该列表中的每个元素，为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。**

# In[ ]:


names = ['ron', 'tyler', 'dani']
for name in names:
    print(f"{name.title()}, how are you!")


# ####  §3.2 操作列表元素

# **1. 创建列表  
# 2. 添加元素：末尾  append  
#             任意位置  insert(0,'X')**
#             
# **3. 修改列表元素-- 列表[索引]='X'**  
# 
# **4. 删除元素：   
#     I. 任意位置 del 语句  
#     II. 末尾位置 pop()  
#     III. 任意位置 pop(2)  
#     IV.根据值删除元素 remove('XX')** 

# #### **1. 创建  自行车 列表**

# In[ ]:


bicycles = ['捷安特', '永久', '凤凰', '飞鸽', '美利达', '哈啰']
msg = f"我喜欢骑 {bicycles[2].title()} 自行车!"
msg


# #### **2. 添加元素 (1) 末尾  append  (2) 任意位置 insert(0,'')**

# In[ ]:


#bicycles = ['捷安特', '永久', '凤凰', '飞鸽', '美利达', '哈啰']
bicycles.append('喜德盛')
bicycles


# In[ ]:


bicycles.insert(0, '崔克')
bicycles


# #### **3. 修改  自行车列表元素 列表[索引]**

# In[ ]:


#bicycles = ['崔克', '捷安特', '永久', '凤凰', '飞鸽', '美利达', '哈啰', '喜德盛']
bicycles[4] = '迪卡侬' #法国
bicycles


# #### **4. 删除元素： (I) 任意位置 del 语句 (II) 末尾位置pop()**

# In[ ]:


#bicycles = ['崔克', '捷安特', '永久', '凤凰', '迪卡侬', '美利达', '哈啰', '喜德盛']
del bicycles[0]
bicycles


# In[ ]:


poped_bicycles = bicycles.pop()
bicycles
poped_bicycles


# #### **4. 删除元素： (III) 任意位置pop(X) (IV) 根据值删除元素 remove('XX')**

# In[ ]:


#bicycles = ['捷安特', '永久', '凤凰', '迪卡侬', '美利达', '哈啰']
poped_bicycles = bicycles.pop(2)
bicycles
poped_bicycles


# In[ ]:


poped_bicycles = bicycles.remove('美利达')
bicycles
poped_bicycles


# ### **动手试一试2 列表元素 操作**

# **练习2: 假设有列表list_student=[[“001”,”李元芳”，19],[“002”,”刘禅”,20],[“003”,”张三丰“，18]]，  
# 依次存放了每名学生的学号、姓名和年龄。试编写程序，实现以下功能：  
#  (a) 在列表末尾添加学生信息：学号“004”，姓名“柯镇恶”，年龄19；学号“006”，姓名“十三郎”，年龄20。  
#  (b) 在列表的适当位置添加如下的学生信息：学号“005”，姓名“唐涤生”，年龄20。  
#  (c) 输出学号为003的学生信息。  
#  (d) 输出所有学生的姓名。  
#  (e) 输出年龄大于19的所有学生的信息。**

# In[ ]:


lst_student = [["001", "李元芳", 19], ["002", "刘禅", 20], ["003", "张三丰", 18]]
lst_student1 = [["004", "柯镇恶", 19], ["006", "十三郎", 20]]
lst_student.extend(lst_student1)
add = ["005", "唐涤生", 20]
lst_student.insert(4, add)
print(lst_student[2])
print("年龄大于19的所有学生的信息：", [x for x in lst_student if x[2]>19])


# ### **§3.3 操作列表**
# **1.创建新表** 
# 
# **2.列表排序    
#     I. 方法sort()对列表永久排序  
#     II. 函数sorted()对列表临时排序**  
#     
# **3. 列表的统计操作(长度、最小值、最大值等)**  
# 
# **4. 遍历整个列表**

# #### **1.创建新表**  
# **I.不同的数据项使用方括号括起来  
# II.使用range() 创建数字列表  
# III. 利用列表推导式创建新列表  
# IV. 使用列表的一部分---切片  
# V. 使用列表的一部分---遍历切片  
# VI. 使用列表的一部分---复制列表**

# **I.不同的数据项使用方括号括起来**

# In[ ]:


list1 = ['python', 'ShowMeAI', 1997, 2022]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = []
list1
list2
list3
list4


# **II.使用range() 创建数字列表**

# In[ ]:


numbers = list(range(1, 6))
numbers


# **III. 利用列表推导式创建新列表**

# In[ ]:


list1 = [i for i in range(1, 21, 2)]
list1


# In[ ]:


squares1 = [value**2 for value in range(1, 11)]
squares1


# In[ ]:


squares2 = [i**2 for i in list1]
squares2


# **IV. 使用列表的一部分---切片**

# In[ ]:


bicycles = ['捷安特', '永久', '凤凰', '飞鸽', '哈啰']
bicycles[0:3]


# **V. 使用列表的一部分---遍历切片**

# In[ ]:


bicycles = ['捷安特', '永久', '凤凰', '飞鸽', '哈啰']
print("Here are the first three bicycles on my team:")
for bicycle in bicycles[:3]:
    print(bicycle.title())


# **VI. 使用列表的一部分---复制列表**

# In[ ]:


list1 = [i for i in range(1, 11)]
list1
list2 = list1[:]
list2
list2 = list1[3:8]
list2


# #### **2.列表排序**
# **I. 方法sort()对列表永久排序    
# II. 函数sorted()对列表临时排序**  

# In[ ]:


import random
random.seed(10)

list1 = [random.randrange(0, 10, 1) for i in range(10)]
list1
list1.sort()
list1
list1.sort(reverse=True)
list1


# **II. 函数sorted()对列表临时排序**

# In[ ]:


import random
random.seed(10)
list1 = [random.randrange(0, 10, 1) for i in range(10)]

list1
sorted(list1, reverse=True)
list1


# #### **3. 列表的统计操作(长度、最小值、最大值等)**

# In[ ]:


digits = [i for i in range(10)]
digits
len(digits)
min(digits)
max(digits)
sum(digits)


# #### **4. 遍历整个列表**

# In[ ]:


cars = ['bmw', 'audi', '比亚迪', '沃尔沃']
for car in cars:
    print(car)


# In[ ]:


cars = ['bmw', 'audi', '比亚迪', '沃尔沃']
for car in cars:
    print(f"{car.title()}, 是一辆好车!\n")


# ### **动手试一试3 列表操作**

# **练习3: 编写程序，实现以下功能：创建一个列表，依次存放每个月对应的天数。
# 假设2月份的天数固定为28天。根据用户输入的月份查询该月的天数并输出。**

# In[ ]:


month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a = int(input("请输入查询的月份："))
if a <= 12 and a>0 :
    print("这个月有", month[a-1], "天")
else:
    print("输入数字出错")


# ### **§3.4 字典**

# **字典是一种通过名字或者关键字引用的数据结构，  
#     其键可以是数字、字符串、元组，这种结构类型也称之为映射。  
# 字典格式：{键1：值1，键2：值2，…}**

# #### **1. 字典的概述**

# In[ ]:


d = {'one': 1, 'two': 2, 'three': 3}


# **使用键读取字典的值**

# In[ ]:


d['one']
d['two']
d['three']


# #### **2. 使用字典**
#   **I.创建字典  
#  II.添加键值对  
# III.访问字典中的值  
#  IV.修改字典中的值  
#   V.删除键值对  
#  VI.使用get() 来访问值**  

# ##### **I.创建字典**

# In[ ]:


#### 内置函数dict()创建字典
tuplekey = ('n1', 'n2', 'n3', 'n4', 'n5')
listvalue = ['一', '二', '三', '四', '五']
dict2 = dict(zip(tuplekey, listvalue))
dict2


# In[ ]:


#### 直接创建字典
dicAreas = {}
dicAreas


# ##### **II.添加键值对**

# In[ ]:


dicAreas['China'] = 960.1
dicAreas['Canada'] = 991.7
dicAreas['Russia'] = 1707.5
dicAreas['Brazil'] = 856.7
dicAreas


# ##### **III.访问字典中的值**

# In[ ]:


dicAreas['China']
dicAreas['Canada']
dicAreas['Russia']
dicAreas['Brazil']


# ##### **IV.修改字典中的值**

# In[ ]:


dicAreas['Brazil'] = 888.8
dicAreas


# ##### **V.删除键值对**

# In[ ]:


del dicAreas['Brazil']
dicAreas


# ##### **VI.使用get() 来访问值**

# In[ ]:


'China' in dicAreas
dicAreas.get('China')


# ### **动手试一试4**

# **练习4: 已知字符串s=”Whether the weather be fine, or whether the weather be not. Whether the weather be cold, or whether the weather be hot.We will weather the whether we like it or not.”,  
# 存放了一个英文绕口令。试编写程序，统计该字符串中英文单词的个数（不区分大小写且不能重复）。**

# In[ ]:


s = '''Whether the weather be fine, or whether the weather be not. 
     Whether the weather be cold, or whether the weather be hot. 
     We will weather the weather whether we like it or not.'''
s = s.lower().replace(',','').replace('.','')
lst = s.split(' ')
wordSet = set(lst)
print(wordSet)
print("一共出现了{}个单词。".format(len(wordSet)))


# **练习5: 编写程序，完成以下功能：  
# （a) 设计一个空字典，用于存放用户的通信录（包括姓名和电话号码）。  
# （b)程序运行后，显示用户选项：  
# ①　新增联系人    
# ②　查询联系人   
# ③　删除联系人  
# ④　退出程序  
# （c) 根据用户的选择，进入下一步，执行相应的功能，完成通信录的增加、查询、删除以及退出系统的功能。**

# In[ ]:


phone = {}
while 1:
    choose = int(input("1.新增联系人  2. 查询联系人 3. 删除联系人 4.退出程序"))
    if choose == 1:
        name = str(input("请输入姓名"))
        num = int(input("请输入电话号码"))
        phone[name] = num
        print("添加成功当前通讯录", phone)
    elif choose == 2:
        name = str(input("请输入姓名"))
        if name in phone:
            print(phone[name])
        else:
            print("查无此人")
    elif choose == 3:
        name = str(input("请输入姓名"))
        del phone[name]
        print("删除成功当前通讯录", phone)
    elif choose == 4:
        break
    else:
        print("请按要求输入操作数")


# #### **3. 遍历字典**
#   **I. 遍历所有键值对  
#  II. 遍历所有键  
# III. 遍历所有值  
#  IV. 对遍历返回的键进行排序  
#   V. 遍历字典中的所有值且排序**

# In[ ]:


dicAreas = {}
dicAreas['China'] = 960.1
dicAreas['Canada'] = 991.7
dicAreas['Russia'] = 1707.5
dicAreas['Brazil'] = 856.7
dicAreas


# **I. 遍历所有键值对**

# In[ ]:


for item in dicAreas.items():
    print(item)


# **II. 遍历所有键**

# In[ ]:


for key in dicAreas.keys():
    key


# **III. 遍历所有值**

# In[ ]:


for value in dicAreas.values():
    f"{value}" ##字符串
value ##数值


# **IV. 对返回的键进行排序**

# In[ ]:


for name in sorted(dicAreas.keys(), reverse=True):
    f"{name.title()}"


# **V. 遍历字典中的所有值且排序**

# In[ ]:


for value in sorted(dicAreas.values()):
    f"{value}"


# #### **4. 字典嵌套**

# **将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套  
# I. 字典列表  
# II. 在字典中存储列表  
# III. 在字典中存储字典**

#  **I. 字典列表**

# In[ ]:


#### 字典alien_X 包含一个外星人的各种信息
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
#### 管理成群结队的外星人
aliens = [alien_0, alien_1, alien_2]


# In[ ]:


aliens
for alien in aliens:
    print(alien)
'''  '''
for alien in aliens[:2]:
    print(alien)


# **II. 在字典中存储列表**

# In[ ]:


favorite_languages = {
    '王': ['python', 'c++'],
    '张': ['c'],
    '李': ['ruby', 'go'],
    '赵': ['python', 'C#', 'JAVA'],
    }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


# **III. 在字典中存储字典**

# In[ ]:


users = {'aeinstein': {
            'first': 'albert',   'last': 'einstein',  'location': 'princeton', },
         'mcurie': {
            'first': 'marie',    'last': 'curie',   'location': 'paris',},
}
for username, user_info in users.items():
    print(f"\nUsername:  {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name:  {full_name.title()}")
    print(f"\tLocation:  {location.title()}")


# ### **动手试一试5**

# **练习6：喜欢的地方  
#    创建一个名为avorite_places 的字典。在这个字典中，  
# 将三个人的名字用作键，并存储每个人喜欢的1～3个地方。  
# 为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的  
# 几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。**

# In[ ]:


favorite_places = {'张三': ['北京长城', '张家界', '黄果树'], 
                   '李四': ['夏威夷', '冰岛'], 
                   '王五': ['黄山', '峨眉山', '乐册大佛'] 
                  }

for name, places in favorite_places.items(): 
    print(f"\n{name.title()} likes the following places:") 
    for place in places: 
        print(f"- {place.title()}")


# ### **§3.5 元组**

# **元组也是用来存放一组相关的数据。**

# **元组与列表的区别：  
# (1)元组使用圆括号()。列表使用方括号[]。  
# (2)元组的元素不能修改。**

# #### **1. 定义元组**

# In[ ]:


tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple1[0]
tuple1[1]


# #### **2. 遍历元组中的所有值**

# In[ ]:


## 修改整个元组值
tuple1 = ('a', 'b', 'c', 'd', 'e')
for tuple2 in tuple1:
    print(tuple2)


# #### **3. 修改整个元组值**

# In[ ]:


## 修改整个元组值
tuple1 = ('a', 'b', 'c', 'd', 'e')
tuple1
    
tuple1 = ('a1', 'b1', 'c1', 'd1')
tuple1


# ### **动手试一试6**

# **练习6：喜欢的地方  
#    创建一个名为avorite_places 的字典。在这个字典中，  
# 将三个人的名字用作键，并存储每个人喜欢的1～3个地方。  
# 为了让这个练习更有趣些，可以让一些朋友说出他们喜欢的  
# 几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。**

# In[ ]:


favorite_places = {'张三': ['北京长城', '张家界', '黄果树'], 
                   '李四': ['夏威夷', '冰岛'], 
                   '王五': ['黄山', '峨眉山', '乐册大佛'] 
                  }

for name, places in favorite_places.items(): 
    print(f"\n{name.title()} likes the following places:") 
    for place in places: 
        print(f"- {place.title()}")


# ### **§3.6 集合**

# **集合用来存放一组无序且互不相同的元素。  
#    组成集合的元素必须是不可变类型。**  
# **(1). 无序: 集合内的元素数据没有顺序  
# (2). 不可更改: 集合内的元素不可更改  
# (3). 无类型要求: 集合内的元素可以是各种类型的  
# (4). 唯一性: 集合不允许有重复的元素**

# **1. 集合的创建与访问  
# 2. 集合的操作  
# I.添加元素  
# II.删除元素  
# III.集合的运算**

# #### **1. 集合的创建与访问**

# ##### **I.集合的创建**

# **(1). 元素必是不可变的，元素与元素间也要保证互不相同。  
# (2). set()函数在序列转换成集合时会自动去掉重复项。  
# (3). 不带参数的set()函数才能创建空集合**

# In[ ]:


#### 直接创建
set1 = {'春', '夏', '秋', '冬', '春', '夏', '秋'}
set1
#### 使用set()函数创建集合
s1=set('hello,world!')
s1
#### 创建空集合
s1={}
s1


# ##### **II.集合的访问**

# In[ ]:


import random
ls = []
for i in range(20):
    ls.append(random.randint(0, 20))

s = set(ls)
s1 = sorted(s)
print("生成的20个0-20随机数为：\n", ls)
print("\n出现在集合中的数有：\n", s)
print("\n排序后的集合：\n", s1)


# #### **2. 集合的基本操作**

# In[ ]:


set1 = {'春', '夏', '秋', '冬'}

set2 = {3, 2, 1, 4, 5}

list1 = ['东', '南', '西', '北']
set3 = set(list1)

set4 = set3
###### set3和set4是指向同一地址的对象

print('set1: ', set1)
print('set2: ', set2)
print('set3: ', set3)
print('set4: ', set4)


# ##### **I.添加元素 (1)S.add(item)  (2) S.update(items)**

# In[ ]:


set4.add('中')
print('添加元素的set3:', set3)
print('添加元素的set4:', set4)
set4.update(set1)
print('update的set4(set1):', set4)


# ##### **II.删除元素**
# **S.remove(items)， S.discard(item)，  S.pop()，  S.clear()**

# In[ ]:


set3.remove('中')
print('删除元素的set3:', set3)
set3.discard('南')
print('discard的set3:', set3)
set3.pop()
print('pop的set3:', set3)
set3.clear()
print('clear的set3:', set3)


# ##### **III.成员判断**
# **Item in S**

# In[ ]:


set2 = {3, 2, 1, 4, 5}
3 in set2


# #### **3. 集合的数学运算**
# **&  |  -**

# In[ ]:


set3 = {'西', '南', '北', '东', '左', '右'}
set4 = {'上', '下', '东', '西', '北', '南'}
print('set3 & set4: ', set3 & set4)
print('set3 | set4: ', set3 | set4)
print('set3 - set4: ', set3 - set4)
print('set4 - set3: ', set4 - set3)


# **(1) 交集: A.union(B)  
# (2) 并集; A.intersection(B)  
# (3) 差集:  A.difference(B)  
# (4) 对称差集:  A.symmetric_difference(B)**

# In[ ]:


print("set4 Before append: ", set4)
print('set4.difference(set3): ', set4.difference(set3))
print('set4.intersection(set3): ', set4.intersection(set3))
print('set4.union(set3): ', set4.union(set3))

