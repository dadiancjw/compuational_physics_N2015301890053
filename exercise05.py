import math
import pylab as pl
i=1
v0=40
xi=x0=0
yi=y0=0
z0=0
g=9.8
vxi=v0*(math.cos(20*math.pi/180))
vyi=v0*(math.sin(20*math.pi/180))
vzi=0
xlist=[x0]
ylist=[x0]
zlist=[0]
t=21
dt=t/1000
while i<=1000:
    v=math.sqrt(vxi**2+vyi**2)
    vxi=vxi-(0.0039+0.0058/(1+math.exp((v-35)/5))*v*vxi*dt
    vyi=vyi-g*dt
    vzi=vzi-vxi*omg*0.00041*dt
    x1=x1+vxi*dt
    yi=yi+vyi*dt
    zi=zi+vzi*dt
    xlist.append(xi)
    ylist.append(yi)
    zlist.append(zi)
    i=i+1
pl.figure(figsize=(20, 11))
pl.plot(xlist,ylist,'r')
pl.title('Cannon Shell Trajectory',fontsize=40)
pl.xlabel('Horizon Distance',fontsize=26)
pl.ylabel('Height',fontsize=30)
pl.show()
