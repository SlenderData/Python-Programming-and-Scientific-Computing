#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
plt.rcParams['axes.unicode_minus'] = False       #显示负号


# # **第7课 符号计算：Sympy库**

# ## **§7.1 SymPy 简介**

# ### **1. SymPy 库简介**

# **sympy是一个Python的科学计算库，用一套强大的符号计算体系完成  
# 诸如多项式求值、求极限、解方程、求积分、微分方程、级数展开、矩阵  
# 运算等等计算问题。  
#     符号计算中数学对象是精确表示的，未计算的数学表达式以符号形式  
# 展现的。**

# ### **2. 安装、升级与导入**

# #### **(1). 安装SymPy包**

# ① pip install sympy  
# ② pip install sympy-1.20.3+mkl-cp39-cp39-win_ amd64.whl  
# ③ python.exe setup.py install  

# #### **(2). Python第三方包的升级**

# In[ ]:


pip install --upgrade sympy -i https://pypi.tuna.tsinghua.edu.cn/simple/


# #### **(3). 卸载第三方包**

# In[ ]:


pip uninstall sympy


# #### **(4). 判断 SymPy 版本**

# In[ ]:


import sympy
sympy.__version__


# #### **(5). 使用时，需要导入模块：**

# In[ ]:


from sympy import *


# ## **§ 7.2 sympy的常数**

# <img style="float:left;" src="File&Figure\Advanced\7sympycont1.png" width="35%">

# In[ ]:


#from sympy import *
import sympy
#数学符合
#虚数单位i
sympy.I
#自然对数低e
sympy.E
#无穷大
sympy.oo
#圆周率
sympy.pi
#求n次方根
sympy.root(8, 3)
#求对数
sympy.log(1024, 2)
#求阶乘
sympy.factorial(4)
#三角函数
sympy.sin(sympy.pi)
sympy.tan(sympy.pi/4)
sympy.cos(sympy.pi/2)


# ## **§ 7.3 符号说明语句**

# ### **1. 符号说明语句**

# #### **(1). 使用symbols()函数或Symbol()函数创建符号变量。**

# In[ ]:


from sympy import *
x, y, z, t = symbols('x,y,z,t')
k, m, n = symbols('k,m,n', integer=True)
f, g, h = symbols('f,g,h', cls=Function)
p = Symbol("p", positive=True)


# **说明：  
# 左边的x是一个符号对象，而右边用引号包着的x是符号对象的name属性，    
# 两个x不要求一样，但为了理解，通常将符号对象和name属性显示成一样，   
# name属性是引号包起来的。  
# 从SymPy库载入所有符号，并且定义了四个通用的数学符号x,y,z,t，  
# 三个表示整数的符号k、m、n， 以及三个表示数学函数的符号f、g、h,  
# 这是通过关键字参数指定所创建符号的假设条件。**

# In[ ]:


x.is_Symbol
p.is_positive
x.is_imaginary
x.is_complex


# #### **(2). 变量名和符号名也可以是不一样的：**

# In[ ]:


a, b = symbols("alpha, beta")
a, b


# #### **(3). 若符号对象名和name属性名一致，可以使用var()函数定义**

# In[ ]:


var("x0,y0,x1,y1")
type(x0)
x0.name
type(x0.name)


# ### **2. 欧拉恒等式和欧拉公式：**
# <img style='' src='File&Figure\Advanced\7sympyoula.png' width='15%'>
# <img style='' src='File&Figure\Advanced\7sympyoula2.png' width='25%'>

# In[ ]:


#from sympy import *
from sympy import E, I, pi
E**(I*pi)+1


# In[ ]:


x = Symbol("x", real=True)
expand(exp(I*x), complex=True)


# ### **3. 符号运算中的赋值**
# #### **(1).subs() 替换函数**

# **subs() 可以将算式中的符号进行替换，它有3种调用方式：  
# 1.expression.subs(x, y): 将算式中的x替换成y。  
# 2.expression.subs({x:y,u:v}):使用字典进行多次替换。  
# 3.expression.subs([(x,y),(u,v)]):使用列表进行多次替换。**

# In[ ]:


from sympy import *
x = symbols('x')
expr = cos(x) + 1
expr
expr.subs(x, 0)


# #### **(2). evalf() 赋值**
# **evalf()将表达式表示为浮点数，用SymPy做计算器。**

# In[ ]:


pi**2
pi.evalf()
(pi+exp(1)).evalf(50)


# #### **(3). 数值**

# In[ ]:


1/2+1/3
S(1)/2 + 1/S(3) #符号运算


# #### **(4). 声明分数**

# In[ ]:


Rational(1, 3)


# ## **§ 7.4 基本操作(Elementary)**

# In[ ]:


x, y, z, a, b, c = symbols('x y z a b c')


# ### **1.数论**

# #### **(1).阶乘**

# In[ ]:


from sympy.ntheory import *
factorial(5)


# #### **(2).分解质因数**

# In[ ]:


factorint(300)
factorint(300, visual=True)


# #### **(3).求因子**

# In[ ]:


divisors(36)


# #### **(4). 二项式**

# In[ ]:


from sympy import *
k, m, n = symbols('k m n')
binomial(n, k)


# ### **2.多项式变换和化简**

# #### **(1). simplify(), radsimp(),combsimp()对数学表达式进行化简**

# In[ ]:


from sympy import *
x, y = symbols('x y')
a, b, n = symbols('a b n')
z, t, c = symbols('z t c')


# In[ ]:


simplify((x+2)**2 - (x+1)**2)
radsimp(1/(y*sqrt(x)+x*sqrt(y)))


# In[ ]:


simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))


# In[ ]:


combsimp(factorial(n)/factorial(n - 3))


# #### **(2). powsimp(): 幂化简**

# In[ ]:


powsimp(x**a*x**b)
powsimp(x**a*y**a)
powsimp(t**c*z**c)
powsimp(t**c*z**c, force=True)


# #### **(3). cancel()：约分, 对表达式的分子分母进行约分运算。**
# **对纯符号的分式表达式及自定义进行约分，不能对内部函数的表达式进行约分。**

# In[ ]:


f, g, h = symbols('f,g,h', cls=Function)
cancel((x**2-1)/(1+x))
cancel(sin((x**2-1)/(1+x))) 
cancel((f(x)**2-1)/(f(x)+1))


# In[ ]:


cancel((x**2 + 2*x + 1)/(x**2 + x))


# #### **(4). factor():提取公因式**

# In[ ]:


factor(x**3 - x**2 + x - 1)


# #### **(5). apart():部分分式展开**

# In[ ]:


expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
expr
apart(expr)


# #### **(6). expand():通用的展开运算**
# **expand_log()、expand mul()、expand_complex()、expand_func   
# 通过将相应的标志参数设置为True,对expand()进行封装()**

# In[ ]:


x, y, z = symbols("x,y,z", positive=True)
expand(log(x*y**2))
expand((x+y)**3)
expand(x**(y+z))
expand(x*log(y*z), mul=False)
expand(x*y, complex=True)
expand(gamma(1+x), func=True)


# #### **(7). factor(): 因式分解**

# In[ ]:


factor(15*x**2+2*y-3*x-10*x*y)
factor(expand((x+y)**20))


# #### **(8). collect():合并同类项。**

# **collect()返回的是一个整理之后的表达式，如果希望得到x的  
# 各次幂的系数，可以设置evaluate参数为False, 让它返回一个以  
# x的幂为键、值为系数的字典。**

# In[ ]:


a, b = symbols('a,b')
eq = (1+a*x)**3 + (1+b*x)**2
eq2 = expand(eq)
eq2
collect(eq2, x)


# In[ ]:


eq2
p = collect(eq2, x, evaluate=False)
p[S(1)] #常数项
p[x**0] #常数项
p[x**2] #x2项的系数


# In[ ]:


collect(a*sin(2*x) + b*sin(2*x), sin(2*x)) #表达式'sin(2x)'的系数


# #### **(9). together(): 分式合并**

# In[ ]:


from sympy import *
x, y, z = symbols("x y z", real=True)
f = symbols("f", cls=Function)
f = (x+2)/(x+1)
ff = apart(f)
ff
#公式折叠用tegother方法
f = (1/x+1/y)
ff = together(f)
ff


# ### **3.序列与级数**

# #### **(1).数列求和**

# **summation(f, (i, a, b)): 求和**
# **计算给定求和变量界限的f 的总和。**

# In[ ]:


Sum(x ** 2, (x, 1, a))
Sum(x ** 2, (x, 1, a)).doit()
summation(x**2, (x, 1, a))


# In[ ]:


Sum(x, (x, 1, a))
Sum(x, (x, 1, a)).doit()
summation(x, (x, 0, n))


# In[ ]:


i, n, m = symbols('i n m', integer=True)
summation(2*i - 1, (i, 1, n))
summation(1/2**i, (i, 0, oo))
summation(1/log(n)**n, (n, 2, oo))
summation(x**n/factorial(n), (n, 0, oo))


# #### **(2).数列求积**

# In[ ]:


Product(x**2, (x, 1, a))
Product(x**2, (x, 1, a)).doit()


# #### **(3).limit()：极限**

# In[ ]:


from sympy import *
x = Symbol("x")
Limit(sin(x)/x, x, 0)
limit(sin(x)/x, x, 0)
limit(sin(x)/x, x, oo)


# #### **(4).series(var, point, order): 级数展开**

# In[ ]:


e = 1/(x + y)
e
s = e.series(x, 0, 5)
s


# #### **(7).fourier_series(): 傅里叶级数展开**

# <img style='float:left;' src='File&Figure\Advanced\7sympyFourierSeries1.png' width='30%'>

# In[ ]:


from sympy import fourier_series, pi
from sympy.abc import x
f = x**2
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n=3)
s1


# In[ ]:


f = x
s = fourier_series(f, (x, -pi, pi))
s1 = s.truncate(n=3)
s1


# ### **4.微积分**

# #### **(1). 微分Derivative()和 diff()**

# **Derivative是表示导函数的类，它的第一个参数是需要进行求导运算：  
# 也可以直接使用 diff()函数或表达式的 diff()的方法来计算导函数**

# In[71]:


t = Derivative(sin(x), x)
t
t.doit()
diff(sin(x), x)
sin(x).diff(x)


# In[72]:


Derivative(sin(2*x), x)
sin(2*x).diff(x)
diff(sin(2*x), x, 2) #二阶导数
diff(sin(2*x), x, 3) #三阶导数
diff(sin(x*y), x, 2, y, 3) #x的二阶导数和y的三阶导数


# #### **(2). integrate(): 积分**

# **不定积分：integrate(f,x)  
# 定积分：integrate(f,(x,a,b))  
# 双重不定积分：integrate(f,x,y)  
# 双重定积分：integrate(f,(x,a,b),(y,c,d))  
# 由于无法进行符号定积分，可用evalf()和N()对其进行数值运算  
# as_sum()方法可以将定积分转换为近似求和公式，它将积分区域分割成N个小矩形的面积之和**

# In[73]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from sympy import *
x = symbols("x", real=True)
f = Function("f")


# In[74]:


integrate(exp(-x), x)

integrate(exp(-x), (x, 0, oo))

e = Integral(x*sin(x), x)#表达式
e
e.doit()


# In[ ]:


e2 = Integral(x*sin(x), (x, 0, 1))
e2 #表达式
e2.doit() #表达式
e2.evalf() #值
N(e2) #值
N(e2, 4) #值
e2.as_sum(5) #表达式
N(e2.as_sum(5)) #值


# In[75]:


from sympy import sqrt
x, y = symbols("x y", real=True)
### 数值计算的局限
N(Integral(sin(x)/x, (x, 0, oo)))
N(Integral(sin(x)/x, (x, 0, 10000)))
N(Integral(sin(x)/x, (x, 0, 100)))

integrate(sqrt(1 + x), x)
integrate(sqrt(1 + x), (x, 0, x))
integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# ### **5.方程. Eq(), solve()**

# #### **(1).解方程函数. Eq(), solve()**

# **在SymPy中，表达式可以直接表示值为0的方程，也可以使用Eq()创建方程。  
# solve()可以对方程进行符号求解，它的第一个参数是表示方程的表达式，  
# 其后的参数是表示方程中未知变量的符号。**

# In[76]:


from sympy import *
a, b, c, x, y, z = symbols("a, b, c, x, y, z")
solve(a*x**2+b*x+c, x)
my_eq = Eq(a*x**2+b*x+c, 0)
solve(my_eq, x)


# #### **(2). 线性方程组, solve(),linsolve(),nonlinsolve()**
# **用元组将几个方程组成一个方程组。**

# In[77]:


### 方程组2
f1 = x+y-3
f2 = x-y+5
solve([f1, f2], [x, y])

linsolve([x + y + z - 1, x + y + 2*z - 3], (x, y, z))
linsolve(Matrix(([1, 1, 1, 1], [1, 1, 2, 3])), (x, y, z))


# In[ ]:


## 方程组的另种写法
def solve_function():
    return [
        x**2+y**2-10,
        y**2+z**2-34,
        x**2+z**2-26,]

solved_value = solve(solve_function(), [x, y, z])
solved_value


# #### **(3). 求解一元n次方程, solveset(),roots(()**

# **一元二次方程** 

# In[ ]:


solveset(Eq(x**2 - x, 0), x, domain=S.Reals)
solveset(Eq(x**2 - x, 0))
solveset(x**2 - x)
solve(Eq(x**2 - x, 0))
roots(x**2 - x, x)#后一个x是表示自变量是x
roots(x**2 - x)


# **一元n次方程**

# In[ ]:


solve(x**3 - 4*x**2 - 3*x + 18)
roots(x**3 - 4*x**2 - 3*x + 18)  #如果要求多重根重复次数可以用roots
roots(x**3 - 6*x**2 + 9*x, x)#后一个x是表示自变量是x


# **n元n次方程** 

# In[ ]:


solve((x**2+x*y+1, y**2+x*y+2), x, y)


# #### **(5). dsolve()： 微分方程求解**
# **dsolve() 可以对微分方程进行符号求解。它的第一个参数是一个  
# 带未知函数的表达式，第二个参数是需要进行求解的未知函数。**   
# <img style='float:left;' src='File&Figure\Advanced\7sympydsolve1.png' width='30%'>

# In[ ]:


from sympy import *
x = Symbol("x")
f = Function("f")
dsolve(Derivative(f(x), x) + f(x), f(x))


# **微分方程2**  
# <img style='float:left;' src='File&Figure\Advanced\7sympydsolve2.png' width='40%'>

# In[ ]:


x = symbols("x", real=True)
eq1 = dsolve(f(x).diff(x) + f(x)**2 + f(x), f(x))
eq1


# **微分方程3**  
# <img style='float:left;' src='File&Figure\Advanced\7sympydsolve4.png' width='40%'>

# In[ ]:


from sympy import *
x = symbols("x", real=True)
f = symbols('f', cls=Function)
diffeq = Eq(f(x).diff(x, 2) - 2*f(x).diff(x) + f(x), sin(x))
diffeq
dsolve(diffeq, f(x))


# ### **6. 三角函数**

# #### **(1). 三角函数化简**

# In[ ]:


from sympy import *
from sympy.abc import x

trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)
trigsimp(cosh(x)**2 + sinh(x)**2)


# #### **(2). 三角函数展开**

# In[ ]:


from sympy import *
from sympy.abc import x,y
expand_trig(sin(x + y))
expand_trig(tan(2*x))
expand(sin(x+y), trig=True)


# #### **(3).变换形式**

# In[ ]:


tan(x).rewrite(sin)


# ### **7.矩阵操作**

# #### **(1). 矩阵的创建**

# In[ ]:


eye(3)
zeros(2, 3)
ones(3, 2)


# #### **(3). 矩阵与矩阵的幂, 对角阵**

# In[ ]:


from sympy import *
#from sympy.abc import x,y
x = Symbol('x')
y = Symbol('y')
A = Matrix([[1,x], [y,1]])
A
A**2


# **矩阵与矩阵的对角阵**

# In[ ]:


M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
M
P, D = M.diagonalize() #对角化
P ## 特征向量
D  ## 特征值的对角阵


# #### **(4). 矩阵的行列式**

# In[ ]:


M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
M
shape(M)
M.det()


# #### **(5). 矩阵的逆、转置**

# In[ ]:


M = Matrix([[1, 2, 3], [4, 5, 6], [4, 7, 8]])
M
M.T #矩阵的转置
M**-1 #矩阵的逆


# #### **(6). 矩阵的特征值和特征多项式、特征向量**

# In[ ]:


M = Matrix([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
#M
M.eigenvals() # {3: 1, -2: 1, 5: 2} 特征值分别为：3, -2, 5，个数为1，1，2
print(M.eigenvects())


# # **End**
