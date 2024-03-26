# 第一课&emsp;课后练习

## 练习1：多条简单消息

### 题目叙述

&emsp;&emsp;将一条消息赋给变量，并将其打印出来；然后将变量的值修改为一条新消息，并将其打印出来。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 多条消息的打印

# 初始消息
message = "Hello world!"
print(message)

# 修改消息内容
message = "Python is fun!"
print(message)

```

### 结果输出

![](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/12-44-43-bc8e758b73ca16bc575b7179ca8a1df7-截屏2024-03-26-12.43.22-0974d5.png)

## 练习2：个性化消息

### 题目叙述

&emsp;&emsp;用变量表示一个人的名字，并向其显示一条消息。显示的消息应非常简单，例如：

> Hello Eric, would you like to learn some Python today?

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 个性化消息

# 名字变量
name = "Eric"
# 显示的消息
print(f"Hello {name}, would you like to learn some Python today?")

```

### 结果输出

![](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/12-44-43-56cf6b8ea9fa23dfb09daedbbdec6486-截屏2024-03-26-12.43.30-176e67.png)

## 练习3：调整名字的大小写

### 题目叙述

&emsp;&emsp;用变量表示一个人的名字，然后以小写、大写和首字母大写的方式显示这个人名。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 名字的不同大小写形式

# 名字变量
name = "eric"
# 小写
print(name.lower())
# 大写
print(name.upper())
# 首字母大写
print(name.capitalize())

```

### 结果输出

![](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/12-44-43-36c37d4e4cd4e0730ef02d82fe4c4b1f-截屏2024-03-26-12.44.07-7df2b4.png)

## 练习4：名言

### 题目叙述

&emsp;&emsp;找一句你钦佩的名人说的名言，用变量`famous_person`表示名人的姓名，再创建要显示的消息并将其赋给变量`message`，然后打印这条消息；并在其开头和末尾都包含一些空白字符。务必至少使用字符组合`\t`和`\n`各一次。

&emsp;&emsp;示例消息：

> Albert Einstein once said, “A person who never made a mistake never tried anything new.”

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 名人名言

# 名人姓名
famous_person = "Albert Einstein"
# 消息内容
message = f"\t{famous_person} once said, “A person who never made a mistake\nnever tried anything new.”"
# 打印消息
print(message)

```

### 结果输出

![](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/12-44-43-08fd0d46c743651959e24521f254bf5d-截屏2024-03-26-12.44.16-0f4279.png)

## 练习5：数字8

### 题目叙述

&emsp;&emsp;编写四个表达式，分别使用加法、减法、乘法和除法运算，但结果都是数字8。使用函数调用`print()`来显示结果，务必将这些表达式用圆括号括起来。也就是说，你应该编写四行类似于下面的代码：

```python
print(5+3)
```

&emsp;&emsp;输出应为四行，其中每行都只包含数字8。

### 程序代码

```python
# 当前日期：2024-03-19
# 姓名：马云骥
# 通过不同的数学运算得到数字8

# 加法
print(5+3)
# 减法
print(10-2)
# 乘法
print(2*4)
# 除法
print(16/2)

```

### 结果输出

![](https://raw.githubusercontent.com/SlenderData/img/main/images/2024/03/26/12-44-43-c6ae4ff71ee1fcede00a7136d3193f77-截屏2024-03-26-12.44.24-5d775b.png)