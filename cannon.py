import math
import pylab as pl
i=1
xi1=xi2=x0=0
yi1=yi2=y0=1
v0=1500                     # 加农炮出膛速度在一千多米/秒这个量级
th=45                       # 出射速度方向于水平面夹角(角度制)
vx0=v0*(math.cos(th))
vy0=v0*(math.sin(th))
g=9.8
C=1
A=0.1
rho=1.29
m=1000
a=0.0065
alpha=2.5
T0=300
xishu=C*A*rho/(2*m)
vxi1=vxi2=vx0
vyi1=vyi2=vy0
xlist1=xlist2=[0]
ylist1=ylist2=[0]
t1=132
dt1=t1/100
t2=232
dt2=t2/100
while i<=100:
    v1=math.sqrt(vxi1**2+vyi1**2)
    v2=math.sqrt(vxi2**2+vyi2**2)
    vxi1=vxi1-xishu*((1-a*yi1/T0)**alpha)*v1*vxi1*dt1
    vyi1=vyi1-g*dt1-xishu*((1-a*yi1/T0)**alpha)*v1*vyi1*dt1
    xi1=xi1+vxi1*dt1
    yi1=yi1+vyi1*dt1
    xlist1.append(xi1)
    ylist1.append(yi1)
    vxi2=vxi2-xishu*(math.exp(-yi2/y0))*v2*vxi2*dt2
    vyi2=vyi2-g*dt2-xishu*(math.exp(-yi2/y0))*v2*vyi2*dt2
    xi2=xi2+vxi2*dt2
    yi2=yi2+vyi2*dt2
    xlist2.append(xi2)
    ylist2.append(yi2)
    i=i+1
pl.plot(xlist1,ylist1,'r')             # use pylab to plot x and y
pl.plot(xlist2,ylist2,'r')             # use pylab to plot x and y
pl.title('Cannon Shell Trajectory')      # give plot a title
pl.xlabel('X')                           # make axis labels
pl.ylabel('Y')
pl.show()                                # 显示绘制出的图
