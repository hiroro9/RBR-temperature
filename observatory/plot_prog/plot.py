import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.rcParams["font.size"]=35

#=====================#
sensor_ID = "T01"
resampling_interval = "1min" #month = "M", day = "D", hour = "H",  minute = "min"
sma_window = 1
#=====================#

nn = sma_window
k = sensor_ID+"_1st"+"_obs_"+resampling_interval

datafile = k +".csv"
data = pd.read_csv(datafile, index_col = 0, usecols=["Time","Temperature","Pressure"])
data.index = pd.to_datetime(data.index)

data = data.rolling(window = nn, min_periods = 1).mean()


#f = data.loc[:,"Pressure"].values
#F = np.fft.fft(f)

fig = plt.figure(figsize=(30,30))
fig.suptitle(sensor_ID)

ax = fig.add_subplot(211)
ax1 = fig.add_subplot(212, sharex = ax)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))

ax.tick_params(labelbottom = False)


data.plot(y="Pressure", ax=ax, legend=False)
data.plot(y="Temperature", ax=ax1,legend=False)


#ax.legend(["TD02"])
#ax1.legend(["TD02"])
#ax1.plot(np.abs(F))

ax.set_ylabel("Pressure [dbar]")
ax1.set_ylabel("Temperature [$^\circ$C]")

fig.savefig(k+"_SMA_"+str(nn)+".png")
plt.close(fig)
