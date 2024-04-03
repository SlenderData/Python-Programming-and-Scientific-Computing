# 编写函数，求任意个连续整数的和

def calSum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum


def calSum2(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
    return sum


def calSum3(num1, num2, step):
    sum = 0
    for i in range(num1, num2 + 1, step):
        sum += i
    return sum


while True:
    print("你要模拟哪种加法？")
    print("1. 1+2+3+...+n")
    print("2. n1+n2+...+n")
    print("3. n1+(n1+step)+(n1+2*step)+...+n")
    print("4. 退出")
    choice = input("请选择：")
    if choice == '1':
        num = int(input("请输入n："))
        print(f"1+2+3+...+{num}={calSum(num)}\n")
    elif choice == '2':
        num1 = int(input("请输入n1："))
        num2 = int(input("请输入n2："))
        print(f"{num1}+{num1 + 1}+...+{num2}={calSum2(num1, num2)}\n")
    elif choice == '3':
        num1 = int(input("请输入n1："))
        num2 = int(input("请输入n2："))
        step = int(input("请输入step："))
        print(f"{num1}+{num1 + step}+{num1 + 2 * step}+...+{num2}={calSum3(num1, num2, step)}\n")
    elif choice == '4':
        break
    else:
        print("输入错误，请重新输入！")
