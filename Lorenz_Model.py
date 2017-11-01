import pylab as pl
x=1
y=0
z=0
t=0
dt=0.0001
tlist=[]
xlist=[]
ylist=[]
zlist=[]
i=1
b=8/3
s=10
r=30
while i<1000000:
    zlist.append(z)
    z=z+(x*y-b*z)*dt
    tlist.append(t)
    xlist.append(x)
    x=x+s*(y-x)*dt
    ylist.append(y)
    y=y+(-x*z+r*x-y)*dt
    t=t+dt
    i=i+1
pl.figure(figsize=(20, 14))
pl.plot(xlist,zlist,'r')
pl.title('Lorenz Model/Phase space Plot(r=30)',fontsize=60)
pl.xlabel('n',fontsize=50)
pl.ylabel('time',fontsize=50)
pl.show()
