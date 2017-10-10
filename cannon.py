import math
import pylab as pl
i=1
xi1=xi2=x0=0                # 起始位置横坐标
yi1=yi2=y0=0                # 起始位置纵坐标
v0=1500                     # 加农炮出膛速率在一千多米/秒这个量级
th=45                       # 出射速度方向于水平面夹角(角度制)
vx0=v0*(math.cos(th))       # 水平方向初始速度
vy0=v0*(math.sin(th))       # 竖直方向初始速度
g=9.8                       # 重力加速度
C=1                         # 阻力模型的阻力系数（课本指示视为常数1）
A=0.1                       # 正对截面积/m^2
rho=1.29                    # 海平面标准空气密度（对应温度看作300K）
m=1000                      # 炮弹质量/Kg
a=0.0065                    # 大气密度的绝热模型参数（课本推荐值）
alpha=2.5                   # 大气密度的绝热模型参数（课本推荐值）
T0=300                      # 海平面温度（应该是个变量）
xishu=C*A*rho/(2*m)
vxi1=vxi2=vx0
vyi1=vyi2=vy0
xlist1=xlist2=[x0]
ylist1=ylist2=[y0]
t1=124                                                              # 绝热模型下预计起落时间差
dt1=t1/100                                                          # 绝热模型下计算的步长
t2=235                                                              # 等温模型下预计起落时间差
dt2=t2/100                                                          # 等温模型下计算的步长
while i<=100:                                                       # 循环得出各个节点的位置
    v1=math.sqrt(vxi1**2+vyi1**2)                                   # 绝热模型下节点时刻的速率
    v2=math.sqrt(vxi2**2+vyi2**2)                                   # 等温模型下节点时刻的速率
    vxi1=vxi1-xishu*((1-a*yi1/T0)**alpha)*v1*vxi1*dt1               # 绝热模型下节点时刻对应的横坐标方向速率
    vyi1=vyi1-g*dt1-xishu*((1-a*yi1/T0)**alpha)*v1*vyi1*dt1         # 绝热模型下节点时刻对应的纵坐标方向速率
    xi1=xi1+vxi1*dt1                                                # 绝热模型下节点时刻炮弹对应的横坐标
    yi1=yi1+vyi1*dt1                                                # 绝热模型下节点时刻炮弹对应的纵坐标
    xlist1.append(xi1)                                              # 将计算得到的坐标加入列表中
    ylist1.append(yi1)
    vxi2=vxi2-xishu*(math.exp(-yi2/10000))*v2*vxi2*dt2              # 等温模型下节点时刻对应的横坐标方向速率
    vyi2=vyi2-g*dt2-xishu*(math.exp(-yi2/10000))*v2*vyi2*dt2        # 等温模型下节点时刻对应的纵坐标方向速率
    xi2=xi2+vxi2*dt2                                                # 等温模型下节点时刻炮弹对应的横坐标
    yi2=yi2+vyi2*dt2                                                # 等温模型下节点时刻炮弹对应的纵坐标
    xlist2.append(xi2)
    ylist2.append(yi2)
    i=i+1
pl.plot(xlist1,ylist1,'r')                                      # use pylab to plot x and y
pl.plot(xlist2,ylist2,'b')                                      # use pylab to plot x and y
pl.title('Cannon Shell Trajectory')                             # give plot a title
pl.xlabel('X')                                                  # make axis labels
pl.ylabel('Y')
pl.show()  
