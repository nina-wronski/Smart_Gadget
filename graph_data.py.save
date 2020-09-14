import datetime
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
import time

class PlotData:

    def __init__(self):
        self.time_stamp = []
        self.temp = []
        self.hum = []

    def read_csv(self, csv_file):
        data = pd.read_csv(csv_file)
        self.time_stamp = pd.to_datetime(data['Date and Time'])
        self.temp = data['Temperature']
        self.hum = data['Relative Humidity']


    def plot_style(self):

        fig, (ax1, ax2) =plt.subplots(nrows=2, ncols=1, sharex=True)

      #  ax1.plot(self.time_stamp, self.temp, color='#F9F75D', label='Temperature')
       # ax2.plot(self.time_stamp, self.hum, label='Humidity')

        ax1.legend()
        ax1.set_title('Temperature and Relative Humidity values on Sensirion Sensor')
        ax1.set_ylabel('Temperature ($^\circ$C)')
        ax2.legend()
        ax2.set_xlabel('Time (HH:MM:SS)')
        ax2.set_ylabel('Relative Humidity (%rh) ')

        plt.tight_layout()
        #plt.show(block=False)
        #plt.cla()
        #plt.draw()
       # plt.pause(3)
       # plt.clf()
       # plt.pause(3)
       # plt.draw()
       # plt.pause(3)

    def show_plot(self):
        plt.ion()
        plt.isinteractive()
         #plt.pause(0.05)
        #plt.draw()
        #plt.gcf().show()
        #time.sleep(2)
        #plt.cla()
        #plt.close()
#graph = PlotData()
#graph.read_csv('temp_hum_readings.csv')
#graph.plot_style()

#g_data = pd.read_csv('temp_hum_readings.csv')
#print(g_data)
#time_stamp = pd.to_datetime(g_data['Date and Time'])
#temp = g_data['Temperature']
#hum = g_data['Relative Humidity']
#me in time_stamp:
#    print(type(time))

#plt.style.use('dark_background')

#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)

#time_vals = []
#temp_vals = []
#hum_vals = []

#index = count()

def animate(i):
    pullData = pd.read_csv('temp_hum_readings.csv', 'r')
    dataArray = pullData.split('/n')
    xar = []
    yar = []
    zar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append (int(x))
            yar.append(int(y))
            zar.append(int(z))
    ax1.clear()
    ax1.plot(xar, yar)

#ani = animation.FuncAnimation(fig, animate, interval=10000)
#plt.show()


#    time_vals = data['Date and Time']
 #   temp_vals = data['Temperature']
  #  hum_vals = data['Relative Humidity']
  #  plt.cla()
   # plt.plot(time_vals, temp_vals)
   # plt.xlabel('Time HH:MM:SS')
   # plt.ylabel('Temperature')
   # plt.title('Time vs Temperature readings')
   # plt.gcf().autofmt_xdate()
   # plt.tight_layout()

#ani = FuncAnimation(plt.gcf(), animate, 5000)

#plt.tight_layout()

#plt.show()




#fig, (ax1, ax2) =plt.subplots(nrows=2, ncols=1, sharex=True)

#ax1.plot(time_stamp, temp, color='#F9F75D', label='Temperature')
#ax2.plot(time_stamp, hum, label='Humidity')

#ax1.legend()
#ax1.set_title('Temperature and Relative Humidity values on Sensirion Sensor')
#ax1.set_ylabel('Temperature ($^\circ$C)')

#ax2.legend()
#ax2.set_xlabel('Time (HH:MM:SS)')
#ax2.set_ylabel('Relative Humidity (%rh) ')

#plt.tight_layout()
#plt.show()


#plt.plot(time_stamp, temp)
#plt.scatter(time_stamp, hum)
#plt.tight_layout()
#plt.show()
#
#temp_vals = []
#hum_vals = []
#nz_time_now = []



#plt.plot(nz_time_now, temp_vals)

#index = count()

#def animate(i):
 #   nz_time_now.append(next(index))
  #  temp_vals.append(

#while True:
 #   pullData = open('temp_hum_readings.csv', 'r').read()



