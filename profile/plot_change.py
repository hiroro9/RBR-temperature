import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
plt.rcParams["font.size"]=35

#=====================#
date_list = ["2018-05-12","2018-07-07"]
#=====================#

file = os.listdir("./")

fig, ax = plt.subplots(figsize=(30,30))

for i in date_list:
    file_in = [s for s in file if i in s]
    datafile = str(file_in[0])
    df = pd.read_csv(datafile)

    x = df.loc[:,"Temperature"].values
    y = df.loc[:,"Depth"].values

    ax.plot(x, y, label = i)
#    interval = 0.01
#    for k in range(0, depth*100):
#       dfm =  dff.query("100 <= Depth < 100.01")
#       print(dfm)

ax.set_xlim(15,27)
ax.set_ylim(0,500)

ax.set_xlabel("Temperature[$^\circ$C]")
ax.set_ylabel("Depth[m]")
ax.legend()

plt.gca().invert_yaxis()

fig.savefig("Temperature_Profile.png")
