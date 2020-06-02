import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
plt.rcParams["font.size"]=35

#=====================#
sensor_ID_list = {"082992":"TD01","082993":"TD02", "082994":"TD03", "095963":"TD04", "095964":"TD05", "102795":"TD06","102796":"TD07","102797":"TD08","102798":"TD09","102799":"TD10"}
#=====================#

file=os.listdir("./")

fig, ax = plt.subplots(figsize=(30,30))

for i in sensor_ID_list.keys():
    for l in file:
        if i in l:
            file_in = [s for s in file if i in s]
            datafile = str(file_in[0])
            sensor_ID = sensor_ID_list[i]
            
            dff = pd.read_excel(datafile, sheet_name="Data", skiprows=[0],index_col=0, usecols=[0,1,4])

            date = str(dff.index[1])[0:10]
            depth = int(dff["Depth"].max())
            
            x=dff.loc[:,"Temperature"].values
            y=dff.loc[:,"Depth"].values
            
            ax.plot(x, y, label = sensor_ID)
            
            dff.to_csv(sensor_ID+"_profile_"+date+".csv",index=False)
        else:
            pass

ax.set_xlim(15,27)
ax.set_ylim(0,500)

ax.set_xlabel("Temperature[$^\circ$C]")
ax.set_ylabel("Depth[m]")
ax.legend()

plt.gca().invert_yaxis()

fig.savefig("Temperature_Profile_"+date+".png")
