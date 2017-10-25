import math
import pylab as pl
g=9.8
l=9.8
q=0.5
F=0
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
while i<700:
    wi=wi-g/l*math.sin(ri)*dt-q*wi*dt+F*math.sin(wd*ti)*dt
    wlist.append(wi)
    ri=ri+wi*dt
    while ri>math.pi:
        ri=ri-2*math.pi
    while ri<-math.pi:
        ri=ri+2*math.pi
    rlist.append(ri)
    ti=ti+dt
    tlist.append(ti)
    i=i+1
pl.figure(figsize=(20, 14))
p1,=pl.plot(tlist,rlist,'k')
p2,=pl.plot(tlist,wlist,'r')
pl.title('Chaos Systerm',fontsize=50)
pl.xlabel('time/s',fontsize=30)
pl.ylabel('theta/radians',fontsize=30)
pl.legend([p1,p2],['Theta','Omega'],fontsize=40,loc="upper right")
pl.show()
