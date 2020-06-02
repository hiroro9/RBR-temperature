import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.rcParams["font.size"]=35

#=====================#
sensor_ID_list = ["TD01", "TD02","TD03", "TD04", "TD05"]
resampling_interval = "30S" #month = "M", day = "D", hour = "H",  minute = "min"
sma_window = 100
range = "2018_0707_0914"
initial_date = "2018-07-10 12:00:00"
final_date = "2018-09-10 12:00:00"
#=====================#

nn = sma_window

fig = plt.figure(figsize=(35,35))
fig.suptitle(range)

ax = fig.add_subplot(211)
ax1 = fig.add_subplot(212, sharex = ax)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d\n%H:%M"))
ax.tick_params(labelbottom = False)

ax.set_ylabel("Pressure [dbar]")
ax1.set_ylabel("Temperature [$^\circ$C]")


for i in sensor_ID_list:

    k = i +"_resampled_"+resampling_interval
    
    datafile = k +".csv"
    data = pd.read_csv(datafile, index_col = 0, usecols=["Time","Temperature","Pressure"])
    data = data.loc[initial_date:final_date,:]
    data = data - data.values[0,:]
    data = data.rename(columns={"Temperature": i+"T", "Pressure":i+"P"})
    data.index = pd.to_datetime(data.index)
    
    data = data.rolling(window = nn, min_periods = 1).mean()
    
    data.plot(y=i+"P", ax=ax)
    data.plot(y=i+"T", ax=ax1)
    
ax.legend(loc = "upper left", bbox_to_anchor=(0.99, 1))
ax1.legend(loc = "upper left",bbox_to_anchor=(0.99, 1))

fig.savefig("longterm_SMA_"+str(nn)+"_"+range+".png")
plt.close(fig)
