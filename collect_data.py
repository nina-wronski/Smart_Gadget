import csv
from smart_gadget_1 import SmartGadget
from time import sleep
#import matplotlib.pyplot as plt
import datetime
import pytz
#import random
#from itertools import count
import pandas as pd
#from graph_data import PlotData


A2_device = 'F8:70:C7:E1:BB:A2'
A2_SG = SmartGadget(A2_device)

#while True:
#   A2_SG.temp_reading()
#    A2_SG.hum_reading()

file_to_write = 'temp_hum_readings.csv'

t = open(file_to_write, 'w')

wc=csv.writer(t)
wc.writerow(['Date and Time', 'Temperature', 'Relative Humidity'])

#for x in range(5):
#    dt_utc = datetime.datetime.now(tz=pytz.UTC)
#    dt_nz = dt_utc.astimezone(pytz.timezone('NZ'))
#    wc.writerow([dt_nz, A2_SG.temp_reading(), A2_SG.hum_reading()])
#    sleep(5)

#graph = PlotData()
#graph.read_csv('temp_hum_readings.csv')
#graph.plot_style()

#graph.show_plot()

while True:
    dt_utc = datetime.datetime.now(tz=pytz.UTC)
    dt_nz = dt_utc.astimezone(pytz.timezone('NZ'))
    #graph.time_stamp.append(dt_nz)
    #graph.temp.append(A2_SG.temp_reading())
    #graph.hum.append(A2_SG.hum_reading())
    wc.writerow([dt_nz, A2_SG.temp_reading(), A2_SG.hum_reading()])
    #graph.plot_style()
    #sleep(5)
    #graph.close_graph()
    sleep(10)

t.close()


