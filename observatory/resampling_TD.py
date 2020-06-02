import pandas as pd

#=====================#
sensor_ID = input("input sensor ID!! : ")
times = input("input number of obsevatory! : ")
resample_interval = input("input resampling interval! month = M, day = D, hour = H,  minute = min, second = S : ") 
#
#sensor_ID = "TD01"
#resample_interval = "30S" #month = "M", day = "D", hour = "H",  minute = "min", second = "S" 
#=====================#

n = resample_interval

datafile = sensor_ID + "_" + times + "_obs_full.csv"
data = pd.read_csv(datafile, skiprows=[0],index_col = 0, usecols=["Time","Temperature","Pressure"])
data.index = pd.to_datetime(data.index)

data = data.resample(n).mean()

data.to_csv(sensor_ID+"_"+times+"_obs_"+n+".csv")
