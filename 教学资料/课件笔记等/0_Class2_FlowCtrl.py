#!/usr/bin/env python
# coding: utf-8

# In[1]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ### § 0.2 开发环境的安装与配置

# **1.语言解释器安装程序      
# 2.检验Python是否装好   
# 3.配置环境变量  
# 4.示例程序：输出“Hello Python world!”    
# 5.其他IDE简介**

# **1.语言解释器安装程序  
# a. Anaconda的安装**

#  <img style="float:left;" src="File&Figure\0IDE1.jpg" width="33%">

# **b.Python程序的安装(https://www.python.org/)** 

# <img style="float:center;" src="File&Figure\0PythonDown.jpg" width="60%"> 

# <img style="float:left;" src="File&Figure\0Pinstall1.png" width="60%">

# <img style="float:left;" src="File&Figure\0Pinstall2.png" width="60%">

# <img style="float:center;" src="File&Figure\0Pinstall3.png" width="60%">

# **2.检验Python是否装好**

# <img style="float:center;" src="File&Figure\0Pinstall8.jpg" width="65%">

# **3.配置环境变量**

# <img style="float:center;" src="File&Figure\0Pinstall4.jpg" width="80%"> 

# <img style="float:center;" src="File&Figure\0Pinstall5.jpg" width="40%">

# <img style="float:center;" src="File&Figure\0Pinstall6.jpg" width="50%">

# <img style="float:center;" src="File&Figure\0Pinstall7.jpg" width="55%">

# **4.示例程序：输出“Hello Python world!”**

# <img style="float:center;" src="File&Figure\0Pinstall9.jpg" width="75%">

# **5. 其他IDE简介**

# <img style="float:left;" src="File&Figure\0Pinstall10.jpg" width="58%">

# <img style="float:center;" src="File&Figure\0Pinstall11.jpg" width="60%">

# ### 第2课 选择与流程控制

# **§2.1 条件表达式  
# §2.2 选择结构  
# §2.3 循环结构   
# §2.4 random库**

# #### **§2.1 条件表达式**

# **1. 关系运算符  ==, !=, <>, >=, <=, >, <**

# In[52]:


a, b = 10, 50
a, b
a > b,   0 < a < b,  a == b
a >= b,   a <= b


# <img style="float:left;" src="File&Figure\3ASCII.jpg" width="40%">

# In[53]:


#1. 关系运算符 ==, !=, <>, >=, <=, >, <
'a'>"BC"
"ABC" > "ab"
"Python" < "python"


# **2.逻辑运算符 and(并且), or(或者), not(取反)**

# In[54]:


a, b = 10, 50
a > 10 and b < 100 
a > 10 or b < 100
not(a > 10 and b < 100)


# **3. 条件表达式: 使用各种运算符可以构建不同的条件表达式。**

# **假设有整数x，表示x为一个偶数。**

# In[55]:


x = 30
x % 2 == 0


# **假设有整数x，表示x是3的倍数且个位上数字为5。**

# In[56]:


x = 15
x % 3 == 0 and x % 10 == 5


# **3. 条件表达式: 使用各种运算符可以构建不同的条件表达式。**

# **假设有三条线段，长度分别为a、b、c，表示a、b、c能构成一个三角形。**

# In[57]:


a, b, c = 4, 5, 6
(a+b>c)and(b+c>a)and(a+c>b)and(a>0)and(b>0)and(c>0)


# **判断year为闰年的条件是：如果year是4的倍数且不是100的倍数，或者year是400的倍数。**

# In[58]:


year = 2023
(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# #### §2.2 选择结构

# **1. 单分支结构：if语句      2.双分支结构：if-else语句**

# <img style="float: left;" src="File&Figure/3singleswitch.png" width="22%"> 
# <img style="float: left;" src="File&Figure/sspace.png" width="10%">
# <img style="float: left;" src="File&Figure/3doubleswitch.png" width="27%">

# **(1). 选择结构 百分制成绩**

# **输入百分制成绩，输出相应的等级：  
# 90分以上为‘A’；     80-89分为‘B’；     
# 70-79分为‘C’；      60-69分为‘D’；  
# 60分以下为‘E’；     
# 如果分数大于100或者小于0.则输出“成绩有误”。**

# <img style="float: left;" src="File&Figure/3singleswitch.png" width="22%"> 
# <img style="float: left;" src="File&Figure/3doubleswitch.png" width="27%">
# <img style="float: left;" src="File&Figure\3scoeflow1.png" width="51%">

# In[59]:


score = eval(input("请输入百分制成绩："))
if 90 <= score <= 100:
    print('A')
elif 80 <= score <= 89:
    print('B')
elif 70 <= score <= 79:
    print('C')
elif 60 <= score <= 69:
    print('D')
elif 0 <= score <= 59:
    print('E')
else:
    print('成绩有误！')


# **(2). 选择结构的另一种写法**

# In[60]:


score = eval(input("请输入百分制成绩："))
level = ('E' if 0<=score<60 else
         'D' if 60<=score<70 else
         'C' if 70<=score<80 else
         'B' if 80<=score<90 else
         'A' if 90<=score<=100 else       
         "请输入0-100以内的数")
level 


# **(3). 选择结构例题：简单的出租车计费系统**

# **当输入行程的总里程时，输出乘客应该付的车费(车费保留1位小数)。计费标准具体为:  
# 起步价： 11元/3千米，  
# 超过3千米， 每千米的费用为1.3元，  
# 超过10千米以后， 每千米的费用为1.5元。**

# In[63]:


km=float(input("请输入千米数:"))
if km<=0:
    print("千米数输入错误，重新输入")
elif km<=3:
    print("您需要支付11元车费")
elif km<=10:
    cost=11 + (km-3)*1.3
    print("您需要支付{:.1f}元车费".format(cost))
else:
    cost=11 + 1.3*(10-3) + (km-10)*1.5
    print("您需要支付 {:.1f} 元车费".format(cost))


# **(4). 选择结构例题：判断一个三位数中的最大数字**

# <img style="float:left;" src="File&Figure\3maxnumberflow.jpg" width="30%">
# <img style="float:left;" src="File&Figure\3maxnumberprogram.png" width="45%">

# In[64]:


num = input("请输入一个三位的正整数：")
if len(num)<3:
    num = input("输入错误，请重新输入一个三位的正整数：")
a, b, c = num[0], num[1], num[2]
if a>b:
    if a>c:
        max_num = a
    else:
        max_num = c
else:
    if b>c:
        max_num = b
    else:
        max_num = c
print(num + "中最大的数字是:" + max_num) 


# **(5). 选择结构例题：用户身份验证**

# <img style="float:left;" src="File&Figure\3usernamepassword.jpg" width="30%">
# <img style="float:right;" src="File&Figure\3usernamepasswordprog.png" width="60%">

# In[65]:


username = input("please input your username:")
if (username != "admin"):
    print("user name is fail")
else:
    password = input("please input your password:")
    if password != "0000":
        print("password is fail")
    else:
        print("welcome admin!")


# #### 动手试一试1

# **（1）从键盘上输入一个字符，  
# 当输入的是英文字母时，输出“输入的英文字母”；  
# 当输入的是数字，输出“输入的是数字”；  
# 当输入的是其他字符时，输出“输入的是什么？”。  
#     编程实现以上功能。**

# In[2]:


ch = input("请输入一个字符:")
if ch.isdigit() == True:
    print("输入的是数字")
elif ch.isalpha() == True:
    print("输入的是英文字母")
else:
    print("输入的是什么？")


# #### §2.3 循环结构 

# **有限循环结构：for语句   有限无限循环结构：while 语句**

# <img style="float: left;" src="File&Figure/3forloop.png" width="26%"> 
# <img style="float: left;" src="File&Figure/sspace.png" width="15%">
# <img style="float: left;" src="File&Figure/3whileloop.png" width="25%"> 

# **1. for语句  
# 迭代器是字符串、列表或数组**

# In[66]:


for s in "abcde":
    print(s, end='   ')


# In[67]:


for s in [30, 35, 40, 50, 100]:
    print(s, end='   ')


# **迭代器是 range(m,n,d)函数(整数)①②**

# In[68]:


for s in range(10):
    print(s, end='   ')


# In[69]:


for s in range(1,10):
    print(s, end='   ')


# **迭代器是 range(m,n,d)函数(整数)③④**

# In[70]:


for s in range(1, 10, 2):
    print(s, end='   ')


# In[71]:


for s in range(10, 1, -1):
    print(s, end='   ')


# **2. 循环结构例题：循环用户身份验证**

# <img style="float: left;" src="File&Figure/3loopusernamepassword.jpg" width="24%"> 
# <img style="float: center;" src="File&Figure/3loopusernamepasswordprog.png" width="44%"> 

# In[ ]:


yes, yes1 = True, True
username = input("please input your username:")
while yes == True:
    if (username != "admin"):
        print("user name is fail")
        username = input("please input your username:")
    else: 
         yes = False
password = input("please input your password:")
while yes1 == True: 
    if password != "0000":
        print("password is fail")
        password = input("please input your password:")
else:
        yes1 = False
        print("welcome admin!")        


# **3. 循环语句中的break和continue语句**

# <img style="float: left;" src="File&Figure/3loopbreak.png" width="30%"> 
# <img style="float: center;" src="File&Figure/3loopcontinue.png" width="30%">

# **3.I 循环结构例题：找出所有小于等于N的素数。**

# In[73]:


N=100
print("找出所有小于等于"+str(N)+"的素数")
prime=[]
for n in range(N,1,-1): #从大到小遍历
    yes=True
    for i in range(2,n): #遍历[2,n-1]区间的自然数
        if n % i == 0: #如果n有因数，就不是素数
            yes=False
            break 
    if yes==True:
        prime.append(n)
print(prime)


# **3.II 循环结构例题：输出200以内最大的素数**

# In[74]:


N=100
print("输出 "+str(N)+" 以内最大的素数")
for n in range(N,1,-1): #从大到小遍历
    yes=True
    for i in range(2,n): #遍历[2,n-1]区间的自然数
        if n % i == 0:  #如果n有因数，就不是素数
            yes=False
            break 
    if yes==True: 
        print(n)
        break


# #### 动手试一试2

# **2. 编写程序，从键盘上输入若干个整数，求出这些整数中所有奇数之和、偶数之和及所有数的平均值，  
#    当从键盘输入字符‘A’时，程序输出计算结果。    
# 3.编写程序，产生两个0~100之间的随机整数RND1和RND2，求出这两个整数的最大公约数和最小公倍数。** 

# #### §2.4 random库

# <img style="float: left;" src="File&Figure/2random1.png" width="90%"> 

# |函数|描述|
# |---|---|
# |seed(n)| 初始化随机种子个数|
# |random()|产生[0.0, 1.0)之间的随机浮点数|
# |randrange(n)||
# |randrange(m,n)|产生[m,n)之间以d为步长的随机整数|
# |randrange(m,n,d)||
# |randint(m,n)|产生[m,n]之间的随机整数|
# |uniform(m,n)| 产生[m n]之间的随机浮点数|
# |choice(s)| 从目标序列s类型中随机返回一个元素|
# |sample(pop,k)| 从pop类型中随机选取k个元素，以列表类型返回，如果k大于所有元素的个数，则报错|
# |shuffle(s)| 将序列类型中元素随机排列，返回打乱后的序列||

# |函数|描述|
# |---|---|
# |random()|产生[0.0, 1.0)之间的随机浮点数格|
# |seed(n)| 初始化随机种子个数|

# In[76]:


import random
random.seed(10)
random.random()

random.random()


# In[83]:


round(random.random(), 4)


# |函数|描述|
# |---|---|
# |randrange(m,n,d)|产生[m,n)之间以d为步长的随机整数|
# |randint(m,n)|产生[m,n]之间的随机整数|
# |uniform(m,n)| 产生[m n]之间的随机浮点数|

# In[84]:


[random.randrange(0, 10, 1) for i in range(10)]


# In[85]:


[random.randint(1, 10) for i in range(10)]


# In[86]:


[round(random.uniform(2.1, 3.5), 2) for i in range(10)]


# |函数|描述|
# |---|---|
# |choice(s)| 从目标序列s类型中随机返回一个元素|

# In[87]:


random.choice(['win', 'lose', 'draw'])
random.choice("python")


# In[88]:


random.choices(['win', 'lose', 'draw'], k=5)
random.choices(['win', 'lose', 'draw'], [0.1, 0.4, 0.5], k=9)#[0.1, 0.4, 0.5]被抽中概率


# |函数|描述|
# |---|---|
# |sample(pop,k)| 从pop类型中随机选取k个元素，以列表类型返回，如果k大于所有元素的个数，则报错|
# |shuffle(s)| 将序列类型中元素随机排列，返回打乱后的序列||

# In[91]:


number = ['one', 'two', 'three', 'four']
random.shuffle(number)
number
random.sample([10, 20, 30, 40, 50], k=3)


# #### §2.5 综合应用

# #### 动手试一试3
# **例2-1 赌场“幸运7”游戏过程模拟**

# **例2-1 赌场中有一种称为“幸运7”的游戏，游戏规则：  
# 玩家掷两枚骰子，如果其点数和为7，玩家赢4元；  
# 不是7，玩家就输1元。  
# 现玩家有10元，当全部输掉时游戏结束，请你编程模拟之。**

# <img style="float: left;" src="File&Figure/3luck7.jpg" width="25%"> 
# <img style="float: center;" src="File&Figure/3luck7prog1.png" width="31%"> 

# In[93]:


from random import *
money=10
print(money,end=" ")
max=money
while money>0:
    num1=randint(1,6)
    num2=randint(1,6)
    if (num1+num2==7):
        money += 4 
        if money>max: max=money
    else:
        money -=1
    print(money,end=" ")
print("\nmax=",max)


# <img style="float: left;" src="File&Figure/3luck7max3.png" width="55%"> 

# **例2-2 赌场“幸运7”游戏,规则的公平性**

# **例2-2赌场中有一种称为“幸运7”的游戏，游戏规则是玩家掷两枚骰子，如果其点数和为7，
# 玩家赢4元；不是7，玩家就输1元。请你分析一下，这样的规则是否公平。**

# In[95]:


from random import *
probi, j, sum, N = {}, 0, 0, 100000
while j<6:
    count11=0
    for i in range(N):
        num1, num2 = randint(1,6), randint(1,6)
        if (num1+num2==7):
            count11 += 1 
    probi[j]=count11/N
    j+=1
print("幸运7的概率为：",[probi[j] for j in range(len(probi))])
for i in range(len(probi)):
    sum += probi[i]
pro=sum/len(probi)
print("幸运7的概率为：",round(pro,4))

