# (1)找出2—100中所有的素数。
# (2)找出2—100中所有的孪生素数。孪生素数是指相差2的素数对，如3和5、5和7、11和13等。
# (3)将4—20中所有的偶数分解成两个素数的和。例如，6＝3+3、8=3+5、10=3+7。

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 找出2—100中所有的素数。
print("2—100中所有的素数：")
for i in range(2, 101):
    if isPrime(i):
        print(i, end=' ')

# 找出2—100中所有的孪生素数。孪生素数是指相差2的素数对，如3和5、5和7、11和13等。
print("\n\n2—100中所有的孪生素数：")
for i in range(2, 99):
    if isPrime(i) and isPrime(i + 2):
        print(f"({i}, {i + 2})", end=' ')

# 将4—20中所有的偶数分解成两个素数的和。例如，6＝3+3、8=3+5、10=3+7。
print("\n\n4—20中所有的偶数分解成两个素数的和：")
for i in range(4, 21, 2):
    flag = False
    for j in range(2, i // 2 + 1):
        if isPrime(j) and isPrime(i - j):
            print(f"{i}={j}+{i - j}")
            flag = True
    if not flag:
        print(f"{i}无法分解成两个素数的和")