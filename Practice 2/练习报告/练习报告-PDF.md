<!-- 请使用 Typora + LaTeX-theme 来预览、编辑和导出PDF
Typora: https://typora.io/
LaTeX-theme: https://github.com/Keldos-Li/typora-latex-theme
Fonts: https://github.com/Keldos-Li/typora-latex-theme-fonts -->

<div class="cover" style="page-break-after:always;font-family:方正公文仿宋;width:100%;height:100%;border:none;margin: 0 auto;text-align:center;">
    <div style="width:60%;margin: 0 auto;height:0;padding-bottom:10%;">
        </br></br></br></br></br></br>
        <img src="https://raw.githubusercontent.com/SlenderData/img/main/images/%E5%B8%B8%E7%94%A8/%E5%AD%A6%E6%A0%A1%E6%A0%87%E8%AF%86/%E6%B1%9F%E8%8B%8F%E5%A4%A7%E5%AD%A6%E4%BA%AC%E6%B1%9F%E5%AD%A6%E9%99%A2/%E6%96%87%E5%AD%97%E7%BB%84%E5%90%88%E6%A8%AA%E6%8E%92.svg" alt="校名" style="width:100%;"/>
    </div>
    </br></br></br></br></br></br></br></br></br></br>
    <div style="width:40%;margin: 0 auto;height:0;padding-bottom:40%;">
        <img src="https://raw.githubusercontent.com/SlenderData/img/main/images/%E5%B8%B8%E7%94%A8/%E5%AD%A6%E6%A0%A1%E6%A0%87%E8%AF%86/%E6%B1%9F%E8%8B%8F%E5%A4%A7%E5%AD%A6%E4%BA%AC%E6%B1%9F%E5%AD%A6%E9%99%A2/%E6%A0%A1%E5%BE%BD.svg" alt="校徽" style="width:100%;"/>
	</div>
    </br></br></br>
    <span style="font-family:华文黑体Bold;text-align:center;font-size:30pt;margin: 10pt auto;line-height:40pt;">Python编程与科学计算<br>练习报告</span>
    </br>
    </br>
    </br>
    </br>
    <table style="border:none;text-align:center;width:72%;font-family:仿宋;font-size:14px; margin: 0 auto;">
    <tbody style="font-family:方正公文仿宋;font-size:12pt;">
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">题&emsp;&emsp;目</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">第二课&emsp;课后练习</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">授课教师</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">王洪金</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">姓&emsp;&emsp;名</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">马云骥</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">学&emsp;&emsp;号</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">4211153047</td>     </tr>
        <tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">专&emsp;&emsp;业</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">软件工程</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">班&emsp;&emsp;级</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">J软件(嵌入)(专转本)2102</td>     </tr>
    	<tr style="font-weight:normal;"> 
    		<td style="width:5%;text-align:right;">日&emsp;&emsp;期</td>
    		<td style="width:2%">：</td> 
    		<td style="width:40%;font-weight:normal;border-bottom: 1px solid;text-align:center;font-family:华文仿宋">2024.03.26</td>     </tr>
    </tbody>              
    </table>
</div>


<!-- 导出PDF时会在这里分页 -->

# 第二课&emsp;课后练习



## 练习1：餐馆订位

### 题目叙述

&emsp;&emsp;编写一个程序，询问用户有多少人用餐。如果超过 8 位，就打印一条消息，指出没有空桌；否则指出有空桌。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-03-26-12.56.55](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/13-03-19-8b6d070a87655e3f1b9ca2936334798a-截屏2024-03-26-12.56.55-055b04.png)



## 练习2：人生的不同阶段

### 题目叙述

&emsp;&emsp;设置变量 `age` 的值，再编写一个 `if-elif-else` 结构，根据 `age` 的值判断一个人处于人生的哪个阶段。

- 如果年龄小于 2 岁，就打印一条消息，指出这个人是婴儿。
- 如果年龄为 2 (含) ～ 4 岁，就打印一条消息，指出这个人是幼儿。
- 如果年龄为 4 (含) ～ 13 岁，就打印一条消息，指出这个人是儿童。
- 如果年龄为 13 (含) ～ 20 岁，就打印一条消息，指出这个人是青少年。
- 如果年龄为 20 (含) ～ 65 岁，就打印一条消息，指出这个人是成年人。
- 如果年龄超过 65 岁 (含)，就打印一条消息，指出这个人是老年人。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 人生的不同阶段

# 设置年龄
age = 25  # 值可以任意修改

# 判断并打印所处的人生阶段
if age < 2:
    print("这个人是婴儿。")
elif age < 4:
    print("这个人是幼儿。")
elif age < 13:
    print("这个人是儿童。")
elif age < 20:
    print("这个人是青少年。")
elif age < 65:
    print("这个人是成年人。")
else:
    print("这个人是老年人。")

```

### 结果输出

![截屏2024-03-26-12.57.36](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/13-03-43-1f6df6e06029483c304aa0a1d16dbbae-截屏2024-03-26-12.57.36-824a5b.png)



## 练习3：电影票

### 题目叙述

&emsp;&emsp;有家电影院根据观众的年龄收取不同的票价：

- 不到 3 岁的观众免费
- 3～12 岁的观众收费 10 美元
- 超过 12 岁的观众收费 15 美元

&emsp;&emsp;请编写一个循环，在其中询问用户的年龄，并指出其票价。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-03-26-12.58.24](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/13-04-00-b9f718598295c6cd4aded06f77d2f290-截屏2024-03-26-12.58.24-b6d5a4.png)



## 练习4：梦想的度假胜地

### 题目叙述

&emsp;&emsp;编写一个程序，调查用户梦想的度假胜地。使用类似于 “If you could visit one place in the world, where would you go?” 的提示，并编写一个打印调查结果的代码块。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-03-26-13.00.17](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/13-04-18-42cac4db586738b11644c228e27d1da5-截屏2024-03-26-13.00.17-f42896.png)



## 练习5：比萨配料

### 题目叙述

&emsp;&emsp;编写一个循环，提示用户输入一系列比萨配料，并在用户输入`quit` 时结束循环。每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。

### 程序代码

```python
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

```

### 结果输出

![截屏2024-03-26-13.02.22](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/13-04-34-7c3a3cc24c4be87aa7b43301619f1b8d-截屏2024-03-26-13.02.22-48cf78.png)
