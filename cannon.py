import math
import numpy as np
import pylab as pl
i=1
x0=0                  # 初始位置横坐标
xi=x0
y0=0                  # 初始位置纵坐标
yi=y0
v0=1500               # 加农炮出膛速度在一千多米/秒这个量级
th=45                 # 出射速度方向于水平面夹角(角度制)
vx0=v0*(math.cos(th))
vy0=v0*(math.sin(th))
g=9.8
C=1
A=1
rho=1
m=1
a=6.5*(10**(-3))
alpha=2.5
T0=300
t=2*vy0/g
dt=t/100
vxi=vx0
vyi=vy0
xlist=[0]
ylist=[0]
vxlist=[vx0]
vylist=[vy0]
while i<=100:
    v=math.sqrt(vxi**2+vyi**2)
    vxi=vxi-(C*A*rho)/(2*m)*((1-a*yi/T0)**alpha)*v*vxi*dt
    vyi=vyi-g*dt-(C*A*rho)/(2*m)*((1-a*yi/T0)**alpha)*v*vyi*dt
    vxlist.append(vxi)
    vylist.append(vyi)
    xi=xi+vxi*dt
    yi=yi+vyi*dt
    xlist.append(xi)
    ylist.append(yi)
    i=i+1
pl.plot(xlist, ylist)         # 调用pylab的plot函数绘制曲线
pl.show()             # 显示绘制出的图
