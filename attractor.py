import math
import pylab as pl
g=9.8
l=9.8
q=0.5
F=1.2
wd=2/3
dt=0.04
w0=0
r0=0.2
t0=0
wi=w0
ri=r0
ti=t0
wlist=[wi]
rlist=[ri]
tlist=[ti]
i=1
while i<100000:
    a=wd*ti
    wi=wi-g/l*math.sin(ri)*dt-q*wi*dt+F*math.sin(a)*dt
    ri=ri+wi*dt
    while ri>math.pi:
        ri=ri-2*math.pi
    while ri<-math.pi:
        ri=ri+2*math.pi
    while a>math.pi:
        a=a-math.pi
    if (math.pi-a)<0.02:
        wlist.append(wi)
        rlist.append(ri)
    ti=ti+dt
    tlist.append(ti)
    i=i+1
pl.figure(figsize=(20, 14))
pl.plot(rlist,wlist,'ko')
pl.title('Chaos Systerm',fontsize=50)
pl.xlabel('theta/radians',fontsize=30)
pl.ylabel('omega',fontsize=30)
pl.show()
