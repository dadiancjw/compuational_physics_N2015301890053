import math
import pylab as pl
g=9.8
l=9.8
q=0.5
F=1.35
Fi=F
flist=[Fi]
wd=2/3
dt=0.04
w0=0
r0=0.2
t0=0
wi=w1i=w2i=w0
ri=r1i=r2i=r0
ti=t0
wlist=[wi]
rlist=[ri]
tlist=[ti]
i=1
while i<150:
    Fi=Fi+0.002
    j=1
    ti=0
    
    while j<5000:
        wi=wi-g/l*math.sin(ri)*dt-q*wi*dt+Fi*math.sin(wd*ti)*dt
        flist.append(Fi)
        ri=ri+wi*dt
        while ri>math.pi:
            ri=ri-2*math.pi
        while ri<-math.pi:
            ri=ri+2*math.pi
        wlist.append(wi)
        rlist.append(ri)
        ti=ti+dt
        tlist.append(ti)
        j=j+1

    i=i+1    
pl.figure(figsize=(20, 14))
pl.plot(flist,rlist,'r')
pl.title('Chaos Systerm',fontsize=50)
pl.xlabel('Fd/N',fontsize=30)
pl.ylabel('theta/radians',fontsize=30)
pl.show()
