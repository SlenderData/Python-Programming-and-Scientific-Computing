#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#添加以下代码以显示单元格中的所有输出
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
plt.rcParams['axes.unicode_minus']=False       #显示负号


# # **第6课 matplotlib库的使用**

# **Matplotlib 的安装、升级、卸载和导入**

# <img style='float:left;' src='File&Figure\Advanced\6pltfig01.png' width='40%'>

# **常用的图表类型及其应用场景如下图所示**

# <img style='float:left;' src='File&Figure\Advanced\6pltfig02.png' width='40%'>

# ## **§6.1 pyplot模块的使用** 

# In[ ]:


from mpl_toolkits.axisartist.axislines import AxesZero
import numpy as np 
from matplotlib import pyplot as plt
#plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
#plt.rcParams['axes.unicode_minus'] = False   #显示负号

x = np.linspace(0, 10, 100)
y = np.sin(x)
fig = plt.figure(figsize=(3, 3))
plt.plot(y, "r")
plt.title("我是图标题")
plt.xlabel("我是x轴标签")
plt.ylabel("我是y轴标签")
plt.text(np.pi, 0.6, "我是图文字")
plt.ylim(-1.2, 1.3)
plt.legend(labels=["我是图例"])
plt.grid()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig110.png' width='40%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig111.png' width='35%'>

# <img style='float:left;' src='File&Figure\Advanced\6pltfig10.png' width='40%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig11.png' width='35%'>

# ## **§6.2 plot()绘图函数的使用** 

# **绘图函数语法格式: plot(x, y, s, linewidth)  
# s:  控制线型的格式字符串，可选，省略时，绘制的线型采用默认格式；  
# linewidth: 线的宽度** 

# <center><font face="黑体" color=red>表9-6颜色字符 -------  表9-7 点风格字符  -------  表9-8 线风格字符</font></center>

# |字符|描述|  --------------  |字符|描述|  -------------   |字符|描述|
# |---|---| --- |---|---| --- |---|---|
# |r|红色| |.|小的实心点| |-|实线|
# |g|绿色| |o|大的实心点| |--|破折线|
# |b|蓝色| |v|倒三角| |:|虚线|
# |y|黄色| |^|上三角| |-.|点横线|
# |k|黑色| |+|十字| |None|没有线|
# |w|白色| |x|叉号| 
# |c|蓝绿色| |d|菱形|
# |m|品红色| |+|十字|
# |#00FF11|RGB颜色| |s|正方形|

# ### **plot()画图示例**

# In[ ]:


from mpl_toolkits.axisartist.axislines import AxesZero
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = x
y2 = 2*x
y3 = 3*x
nymax = 30
fig = plt.figure(figsize=(4, 4))
plt.plot(x, y1, 'ro--', linewidth=0.6)
plt.plot(x, y2, 'gv:', linewidth=1)
plt.plot(x, y3, 'bs-', linewidth=3)
#plt.axis('scaled')
plt.xlim(0, 10)
plt.ylim(0, nymax)
xmin, xmax, ymin, ymax = plt.axis() 
print("x-axis[{}, {}],y-axis[{}, {}]".format(xmin, xmax, ymin, ymax))
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.yticks([0,5,10,15,20,25,30], ['0','a', 'b', 'c', 'd', 'e', 'f'])

plt.xlabel("xlabel---x-axis")
plt.ylabel("ylabel---y-axis")
plt.legend(["y1=x", "y2=2x", "y3=3x"])
plt.text(4, 2, "text--TEXT")
plt.title('title--我是图例')
plt.grid()
plt.show();


# <img style='float:left;' src='File&Figure\Advanced\6pltfig20.png' width='35%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig21.png' width='40%'>

# ## **§6.3 pyplot模块中坐标轴及标签等属性设置**
(1) axis()函数： 获取或设置坐标轴属性
(2) xlim()函数： 设置或者返回x轴的取值区间
(3) ylim()函数
(4) xticks()函数： 设置或者返回x轴的刻度值或标签
(5) ytick()函数
(6) xlabel()函数
(7) ylabel()函数
(8) legend()函数: 图例
(9) text()函数: 在指定的坐标位置显示相应的文本
(10) title()函数: 标题及显示的位置
# <img style='float:left;' src='File&Figure\Advanced\6pltfig30.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig31.png' width='35%'>

# In[ ]:


xmin, xmax, ymin, ymax = plt.axis(options) 
xmin, xmax, ymin, ymax = plt.axis() 
axis(xmin, xmax, ymin, ymax) 


# ## **§6.4 pyplot模块中的绘图函数示例**

# |函数名称|描述|
# |---|---|
# |Bar|绘制条形图|
# |Barh|绘制水平条形图|
# |Boxplot|绘制箱型图|
# |Hist|绘制直方图|
# |his2d|绘制2D直方图|
# |Pie|绘制饼状图|
# |Plot|在坐标轴上画线或者标记|
# |Polar|绘制极坐标图|
# |Scatter|绘制x与y的散点图|
# |Stackplot|绘制堆叠图|
# |stem|用来绘制二维离散数据绘制(又称为“火柴图”)|
# |Step|绘制阶梯图|
# |Quiver|绘制一个二维按箭头|

# In[ ]:


plt.subplot(3, 3, 1)
plt.plot(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 2)
plt.stem(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 3)
plt.scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 4)
plt.barh(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 5)
plt.boxplot(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 6)
plt.quiver(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 7)
plt.stackplot(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(3, 3, 8)
Labels = 'C_A', 'C_B', 'C_C', 'C_D', 'C_E', 'C_F', 'C_G'
data = [3, 4, 7, 6, 2, 8, 9]
Explode = (0, 0, 0.1, 0, 0, 0, 0)
plt.pie(data, explode=Explode, labels=Labels)
plt.subplot(3, 3, 9)
plt.step(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig40.png' width='40%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig41.png' width='50%'>

# ## **动手试一试 1**

# ### **(1)绘制下列函数的图像：**  
# <img style="float:left;" src="File&Figure\Advanced\5nplinalgpoly09.png" width="35%">

# In[ ]:





# ### **(2)利用matplotlib库中的pyplot模块，绘制x在[10,10]取值区间上的f(x)函数**  
# **f(x)的一阶导数和二阶导数的图形。要求：  
# 绘制三幅图，分别放置上述的三个图形。  
# ①第一幅图，标题为Polynomial,使用红色实线绘制。  
# ②第二幅图，标题为FirstDerivative,使用蓝色虚线绘制。  
# ③第三幅图，标题为SecondDerivative,使用绿色实心圆点绘制。**

# In[ ]:





# In[ ]:





# ## **§6.5 子图绘制----subplot()函数**

# **1. plt.subplot(2, 2, 1)  
# 2. ax4 = fig.add_subplot(221)  
# 3. ax1 = fig.add_axes([0.0, 0.0, 0.42, 0.42])  
# 4. fig, ax = plt.subplots(2, 2)**

# ### **1. plt.subplot(nrows, ncols, index)**

# In[ ]:


plt.subplot(2, 2, 1)
plt.plot(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(2, 2, 2)
plt.stem(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(2, 2, 3)
plt.scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
plt.subplot(2, 2, 4)
plt.barh(range(7), [3, 4, 7, 6, 2, 8, 9])


# <img style='float:left;' src='File&Figure\Advanced\6pltfig591.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig592.png' width='45%'>

# <img style='float:left;' src='File&Figure\Advanced\6pltfig593.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig594.png' width='45%'>

# <img style='float:left;' src='File&Figure\Advanced\6pltfig50.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig51.png' width='45%'>

# ### **2. ax4 = fig.add_subplot()**

# In[ ]:


fig=plt.figure()
ax4 = fig.add_subplot(221)
ax5 = fig.add_subplot(222)
ax6 = fig.add_subplot(223)
ax7 = fig.add_subplot(224)

ax4.plot(range(7), [3, 4, 7, 6, 2, 8, 9])
ax5.stem(range(7), [3, 4, 7, 6, 2, 8, 9])
ax6.scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
ax7.barh(range(7), [3, 4, 7, 6, 2, 8, 9])


# ### **3. ax1 = fig.add_axes()**

# In[ ]:


fig=plt.figure(figsize=(5,3))
ax4 = fig.add_axes([0.0, 0.0, 0.42, 0.42]) 
ax5 = fig.add_axes([0.5, 0.5, 0.42, 0.42]) 
ax6 = fig.add_axes([0.0, 0.5, 0.42, 0.42]) 
ax7 = fig.add_axes([0.5, 0.0, 0.42, 0.42]) 

ax6.plot(range(7), [3, 4, 7, 6, 2, 8, 9])
ax5.stem(range(7), [3, 4, 7, 6, 2, 8, 9])
ax4.scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
ax7.barh(range(7), [3, 4, 7, 6, 2, 8, 9])


# ### **4. fig, ax = plt.subplots(2, 2)**

# In[ ]:


fig, ax = plt.subplots(2, 2, figsize=(5,3))
ax[0][0].plot(range(7), [3, 4, 7, 6, 2, 8, 9])
ax[0][1].stem(range(7), [3, 4, 7, 6, 2, 8, 9])
ax[1][0].scatter(range(7), [3, 4, 7, 6, 2, 8, 9])
ax[1][1].barh(range(7), [3, 4, 7, 6, 2, 8, 9])


# ### **5. 不规则图1**

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 3.0, 0.01)

fig = plt.figure(figsize=(5,3.5))
ax1 = plt.subplot(212)
ax1.margins(0.05) 
ax1.plot(t1, f(t1))

ax2 = plt.subplot(221)
ax2.margins(2, 2) 
ax2.plot(t1, f(t1))
ax2.set_title('Zoomed out')

ax3 = plt.subplot(222)
ax3.margins(x=0.1, y=-0.25) 
ax3.plot(t1, f(t1))
ax3.set_title('Zoomed in')
plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig54.png' width='35%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig52.png' width='50%'>

# ### **6. 不规则图2**

# In[ ]:


import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(constrained_layout=True, figsize=(4,3))

gs = GridSpec(3, 3, figure=fig)
ax1 = fig.add_subplot(gs[0, :])
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])

fig.suptitle("GridSpec")
format_axes(fig)
ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig55.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig53.png' width='50%'>

# ## **§6.6 matplotlib库的中文显示问题**

# <img style="float:left;" src="File&Figure\Advanced\5nplinalgpoly09.png" width="35%">

# ### **利用matplotlib库中的pyplot模块，绘制x在[10,10]取值区间上的f(x)函数**  
# **f(x)的一阶导数和二阶导数的图形。要求：  
# 绘制六个子图，分别放置上述的六个图形。  
# 第一个函数放在第1列：  
# ①第一个子图区域，标题为Polynomial,使用红色实线绘制。  
# ②第二个子图区域，标题为FirstDerivative,使用蓝色虚线绘制。  
# ③第三个子图区域，标题为SecondDerivative,使用绿色实心圆点绘制。  
# 第二个函数放在第2列：  
# ①第一个子图区域，标题为Polynomial,使用红色实线绘制。  
# ②第二个子图区域，标题为FirstDerivative,使用蓝色虚线绘制。  
# ③第三个子图区域，标题为SecondDerivative,使用绿色实心圆点绘制。**

# In[ ]:





# ## **§6.6 matplotlib库的中文显示问题**

# ### **1.绘制文本**

# In[ ]:


import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #正常显示负号
fig = plt.figure(figsize=(5,3))
#添加绘图区域
ax = fig.add_axes([0,0,1,1])
#设置格式
ax.set_title('axes title')
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
# 3,8 表示x，y的坐标点；style设置字体样式为斜体；bbox用来设置盒子的属性，比如背景色
ax.text(1.5, 8, 'C语言中网网，编程爱好者都喜欢的网站', \
        style='italic',bbox = {'facecolor': 'yellow'},fontsize=13)
#绘制数学表达式,用$符包裹
ax.text(2, 6, r'an equation: $E = mc^2$', fontsize = 15)
#添加文字，并设置样式
ax.text(4, 0.05, '网址：c.biancheng.net',verticalalignment = \
        'bottom', color = 'green', fontsize = 15)
ax.plot([2], [1], 'o')
#xy为点的坐标；xytext为注释内容坐标；arrowprops设置箭头的属性
ax.annotate('C语言中文网', xy = (2, 1), xytext = (3, 4),\
            arrowprops = dict(facecolor = 'blue', shrink = 0.1))
#设置坐标轴x,y
ax.axis([0, 8, 0, 9])
plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig60.png' width='50%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig61.png' width='50%'>

# ### **2. 数学表达式(r'$\alpha > \beta$')**

# In[ ]:


#绘制表达式 r'$\alpha_i> \beta_i$'
import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2*np.pi*t)
#绘制函数图像
fig = plt.figure(figsize=(4,3))
plt.plot(t,s)
#设置标题
plt.title(r'$\alpha_i> \beta_i$', fontsize=12)
#设置数学表达式
plt.text(0.6, 0.6, r'$\mathcal{A}\mathrm{sin}(2 \omega t)$', fontsize=12)
#设置数学表达式
plt.text(0.1, -0.5, r'$\sqrt{2}$', fontsize=10)
plt.xlabel('time (s)')
plt.ylabel('volts (mV)')
plt.show()


# In[ ]:





# <img style='float:left;' src='File&Figure\Advanced\6pltfig63.png' width='45%'>
# <img style='float:left;' src='File&Figure\Advanced\6pltfig62.png' width='45%'>

# ## **§6.7 3D绘图与动画**

# ### **1. 3D绘图1--colorhat$line3D**

# In[ ]:


import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

# 1. set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

# 2. set up the axes for the second plot
ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig71.png' width='70%'>

# ### **2. 3D绘图2--steamedbread**

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

ax = plt.figure().add_subplot(projection='3d')

X, Y = np.mgrid[0:6*np.pi:0.25, 0:4*np.pi:0.25]
Z = np.sqrt(np.abs(np.cos(X) + np.cos(Y)))

ax.plot_surface(X + 1e5, Y + 1e5, Z, cmap='autumn', cstride=2, rstride=2)

ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")
ax.set_zlim(0, 2)

plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig72.png' width='45%'>

# ### **3. 3D绘图3--colorhat**

# In[ ]:


import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


# <img style='float:left;' src='File&Figure\Advanced\6pltfig73.png' width='50%'>

# ### **5. 动画1--flycloud**

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

# ims is a list of lists, each row is a list of artists to draw in the
# current frame; here we are just animating one artist, the image, in
# each frame
ims = []
for i in range(60):
    x += np.pi / 15.
    y += np.pi / 20.
    im = ax.imshow(f(x, y), animated=True)
    if i == 0:
        ax.imshow(f(x, y))  # show an initial one first
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=50, 
                         blit=True, repeat_delay=1000)
ani.save("File&Figure/6plta1flycloud.gif")


# <img style='float:left;' src='File&Figure\Advanced\6plta1flycloud2.png' width='50%'>
# <img style='float:left;' src='File&Figure\Advanced\6plta1flycloud.gif' width='50%'>

# ### **6. 动画2----sint**

# In[ ]:


import itertools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)

def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 10)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, 
                     interval=10, init_func=init)
ani.save('File&Figure/6plta2sint.gif')


# <img style='float:left;' src='File&Figure\Advanced\6plta2sint2.png' width='40%'>
# <img style='float:left;' src='File&Figure\Advanced\6plta2sint.gif' width='50%'>

# ### **7. 动画3--circlesint**

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])

# draw circle with initial point in left Axes
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")

# draw full curve to set view limits in right Axes
sine, = axr.plot(x, np.sin(x))

# draw connecting line between both graphs
con = ConnectionPatch(
    (1, 0),      (0, 0),
    "data",      "data",
    axesA=axl,   axesB=axr,
    color="C0",  ls="dotted",
)
fig.add_artist(con)

def animate(i):
    pos = np.cos(i), np.sin(i)
    point.set_data(*pos)
    x = np.linspace(0, i, int(i * 25 / np.pi))
    sine.set_data(x, np.sin(x))
    con.xy1 = pos
    con.xy2 = i, pos[1]
    return point, sine, con

ani = animation.FuncAnimation(
    fig,
    animate,
    interval=50,
    blit=False,  # blitting can't be used with Figure artists
    frames=x,
    repeat_delay=100,
)
ani.save("File&Figure/6plta3circlesint.gif")


# <img style='float:left;' src='File&Figure\Advanced\6plta3circlesint2.png' width='30%'>
# <img style='float:left;' src='File&Figure\Advanced\6plta3circlesint.gif' width='50%'>

# ### **8. 动画4--shiftsint**

# In[ ]:


import itertools

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)

def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(xmin, 2*xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, 
                    interval=100, init_func=init)
ani.save("File&Figure/6plta4shiftsint.gif")


# <img style='float:left;' src='File&Figure\Advanced\6plta4shiftsint2.png' width='27%'>
# <img style='float:left;' src='File&Figure\Advanced\6plta4shiftsint.gif' width='50%'>

# In[ ]:




