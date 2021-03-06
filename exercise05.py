import math
import pylab as pl
i=1
v0=40
xi=x0=0
yi=y0=0
zi=z0=0
omg=3
theta=0
g=9.8
vxi=v0*(math.cos(20*math.pi/180))
vyi=v0*(math.sin(20*math.pi/180))
vzi=0
xlist=[x0]
ylist=[y0]
zlist=[0]
t=3
dt=t/10000
while i<=10000:
    v=math.sqrt(vxi**2+vyi**2)
    theta=theta+omg*dt
    vxi=vxi-0.0058/(1+math.exp((v-35)/5))*v*vxi*dt
    vyi=vyi-g*dt
    vzi=vzi-vxi*omg*0.00041*dt-4.9*(math.sin(4*theta)-0.25*math.sin(8*theta)+0.08*math.sin(12*theta)-0.025*math.sin(16*theta))*dt
    xi=xi+vxi*dt
    yi=yi+vyi*dt
    zi=zi+vzi*dt
    xlist.append(xi)
    ylist.append(yi)
    zlist.append(zi)
    i=i+1
pl.figure(figsize=(20, 7))
p2,=pl.plot(xlist,zlist,'b')
pz,=pl.plot([0,93],[0,0],'r')
pl.title('Batted Ball Trajectory',fontsize=40)
pl.xlabel('X Distance',fontsize=26)
pl.ylabel('Z',fontsize=30)
pl.legend([pz,p2],['Straight Line','Z'],fontsize=24,loc="lower left")
pl.show()
