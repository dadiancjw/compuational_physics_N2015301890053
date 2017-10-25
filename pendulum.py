import math
import pylab as pl
g=9.8
l=9.8
q=0.5
F=0.5
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
while i<200:
    wi=wi-g/l*math.sin(ri)*dt+q*wi*dt-F*math.sin(wd*ti)*dt
    wlist.append(wi)
    ri=ri+wi*dt
    rlist.append(ri)
    ti=ti+dt
    while ri>math.pi:
        ri=ri-2*math.pi
    while ri<-math.pi:
        ri=ri+2*math.pi
    tlist.append(ti)
    i=i+1
pl.figure(figsize=(10, 8))
pl.plot(tlist,rlist)
pl.title('Chaos Systerm',fontsize=30)
pl.xlabel('time/s',fontsize=20)
pl.ylabel('theta/radians',fontsize=20) #pl.legend([pz,p1,p2],['Straight Line','omg=10','omg=3'],fontsize=34,loc="lower left")
pl.show()
