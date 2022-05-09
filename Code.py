import numpy as np
import scipy as sp
import mpmath as mp
import time as ti
from scipy import optimize
import matplotlib.pyplot as plt

si = 350
a = 100
e = 0.1
b = np.sqrt(a**2 - (a*e)**2)
c = np.sqrt(a**2 - b**2)
x = np.linspace(-a + c, a + c, si)
y = np.sqrt((b**2)*(1-((x-c)**2)/(a**2)))
plt.plot(x, y, color='tab:red')
plt.plot(x, -1*y, color='tab:red')
xs = np.linspace(-1, 1, a)
ys = np.sqrt(1-xs**2)
plt.plot(xs, ys, color='tab:orange',linewidth = 5)
plt.plot(xs, -1*ys, color='tab:orange',linewidth = 5)

M = 24.851090
def fE(x):
    return x - e*np.sin(x) - M
begin = ti.time()*1000
Eb = sp.optimize.brentq(fE,-1,100)
end = ti.time()*1000
plt.text(0, -130, 'brentq(): '+ str(Eb) + ' time:' + str(end-begin), horizontalalignment = 'center', verticalalignment = 'top', fontsize = 10, color = 'blue')

m = np.arange(1, a + 1, dtype=float)
E = []

def HelpFun(n,m,y):
    ans = 1.0
    for i in range(1,n+1):
        ans *= y / i**2
    for i in range(1,m+1):
        ans *= y/(i+n)
    for i in range(1,n+1):
        ans *= y
    return ans

def J2(j,x):
    j = int(j)
    ansar = []
    for i in range(0,a):
         ansar.append(((-1)**i)*HelpFun(i,j,x/2))
    return sum(ansar)

begin = ti.time()*1000
for i in range(0,a):
    E.append((m[i]**-1)*mp.besselj(m[i], m[i]*e)*np.sin(m[i]*M))
Es = M + 2*sum(E)
end = ti.time()*1000
plt.text(0, -140, 'bessel1(): '+ str(Es) + ' time:' + str(end-begin), horizontalalignment = 'center', verticalalignment = 'top', fontsize = 10, color = 'blue')

E = []
begin = ti.time()*1000
for i in range(0,a):
    E.append((m[i]**-1)*J2(m[i], m[i]*e)*np.sin(m[i]*M))
Ej = M + 2*sum(E)
end = ti.time()*1000
plt.text(0, -150, 'bessel2(): '+ str(Ej) + ' time:' + str(end-begin), horizontalalignment = 'center', verticalalignment = 'top', fontsize = 10, color = 'blue')

plt.show()