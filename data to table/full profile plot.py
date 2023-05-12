import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
data = np.loadtxt('C:\\Users\\Admin\\Desktop\\4march.txt')

h=data[:,1]    #height
p=data[:,0]   # pressure
t=data[:,2]    #temperature
rh=data[:,4]    #relative humidity
mr=data[:,5]    #mixing ratio
wd=data[:,6]    #wind direction
ws=data[:,7]    #wind speed
pt=data[:,8]   #potential temperature
vpt=data[:,10]  #virtual potential temperature

sh=mr/(1+mr)
theta=np.radians(wd)
ew=ws*np.cos(theta)
ns=ws*np.sin(theta)

# Create a figure and a set of subplots with a 3x3 grid
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

axes[0, 0].plot(t,h)
axes[0, 0].set_xlabel('Temperature',fontsize=18)
axes[0, 0].set_ylabel('Height',fontsize=18)

axes[0, 1].plot(pt,h,label='po.temp')
axes[0, 1].plot(vpt,h,label='virpo.temp')
axes[0, 1].set_xlabel('pot temp & vir pt',fontsize=18)
axes[0,1].legend()


axes[0, 2].plot(sh,h)
axes[0, 2].set_xlabel('specific humidity',fontsize=18)

axes[1, 0].plot(ws,h)
axes[1, 0].set_xlabel('wind speed',fontsize=18)
axes[1, 0].set_ylabel('Height',fontsize=18)

axes[1, 1].plot(rh,h)
axes[1, 1].set_xlabel('Relative humidity',fontsize=18)

axes[1, 2].plot(wd,h)
axes[1, 2].set_xlabel('wind direction',fontsize=18)

axes[2, 0].plot(ew,h)
axes[2, 0].set_ylabel('Height',fontsize=18)
axes[2, 0].set_xlabel('east west wind',fontsize=18)

axes[2, 1].plot(ns,h)
axes[2, 1].set_xlabel('north south wind',fontsize=18)

axes[2, 2].plot(p,h)
axes[2, 2].set_xlabel('pressure',fontsize=18)


# Adjust the spacing between subplots
plt.tight_layout()
fig.subplots_adjust(top=.94)
fig.suptitle("Trivandrum lat-8.48,long-76.95 at 00Z 04 Mar 2023",fontsize=28)

# Display the figure
plt.show()

















