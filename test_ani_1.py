import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from smart_gadget_1 import SmartGadget
import pytz
import datetime
import csv

A2_device = 'F8:70:C7:E1:BB:A2'
A2_SG = SmartGadget(A2_device)

#F1_device = 'FD:15:AA:19:BC:F1'
#F1_SG = SmartGadget(F1_device)

plt.style.use('dark_background')
fig, (ax1, ax2) =plt.subplots(nrows=2, ncols=1, sharex=True)

file_to_write = 'temp_hum_readings.csv'

t = open(file_to_write, 'w')

wc=csv.writer(t)
wc.writerow(['Date and Time', 'Temperature', 'Relative Humidity'])

def A2_csv():
    file_to_write = 'A2_readings.csv'

    tA2 = open(file_to_write, 'w')

    A2_wc=csv.writerA2(tA2)
    A2_wc.writerow(['Date and Time', 'Temperature', 'Relative Humidity'])


def F1_csv();
    file_to_write = 'F1_readings.csv'

    tF1 = open(file_to_write, 'w')

    F1_wc=csv.writerF1(tF1)
    F1_wc.writerow(['Date and Time', 'Temperature', 'Relative Humidity'])


time_stamp = []
temp = []
hum = []

def nz_time():
    dt_utc = datetime.datetime.now(tz=pytz.UTC)
    dt_nz = dt_utc.astimezone(pytz.timezone('NZ'))
    return dt_nz

def plot_axis():

def A2_append_values():
    Atime_now = nz_time()
    Atemp_now = A2_SG.temp_reading()
    Ahum_now = A2_SG.hum_reading()
    time_stamp.append(Atime_now)
    temp.append(Atemp_now)
    hum.append(Ahum_now)
    wc.writerow([time_now, temp_now, hum_now])

def F1_append_values():
    Ftime_now = nz_time()
    Ftemp_now = F1_SG.temp_reading()
    Fhum_now = F1_SG.hum_reading()
    time_stamp.append(Ftime_now)
    temp.append(Ftemp_now)
    hum.append(Fhum_now)
    wc.writerow([Ftime_now, Ftemp_now, Fhum_now])
    return Ftime_now, Ftemp_now,Fhum_now

def A2_plot():
    ax1.plot(time_stamp, temp, label='Temperature', color='#2B7E28')
    ax2.plot(time_stamp, hum, label='Humidity', color='#F884FC')

    ax1.legend()
    ax1.set_title('Temperature and Relative Humidity values on Sensirion Sensor$
    ax1.set_ylabel('Temperature ($^\circ$C)')
    ax2.legend()
    ax2.set_xlabel('Time (HH:MM:SS)')
    ax2.set_ylabel('Relative Humidity (%rh) ')



def F1_plot():
    ax1.plot(time_stamp, temp, label='Temperature', color='#2B7E28')
    ax2.plot(time_stamp, hum, label='Humidity', color='#F884FC')

    ax1.legend()
    ax1.set_title('Temperature and Relative Humidity values on Sensirion Sensor$
    ax1.set_ylabel('Temperature ($^\circ$C)')
    ax2.legend()
    ax2.set_xlabel('Time (HH:MM:SS)')
    ax2.set_ylabel('Relative Humidity (%rh) ')



def animate(i, time_stamp, temp, hum):

    time_now = nz_time()

    temp_now = A2_SG.temp_reading()
    hum_now = A2_SG.hum_reading()
    time_stamp.append(time_now)
    temp.append(temp_now)
    hum.append(hum_now)
    wc.writerow([time_now, temp_now, hum_now])

    ax1.clear()
    ax2.clear()
    plt.style.use('dark_background')

    ax1.plot(time_stamp, temp, label='Temperature', color='#2B7E28')
    ax2.plot(time_stamp, hum, label='Humidity', color='#F884FC')

    ax1.legend()
    ax1.set_title('Temperature and Relative Humidity values on Sensirion Sensor')
    ax1.set_ylabel('Temperature ($^\circ$C)')
    ax2.legend()
    ax2.set_xlabel('Time (HH:MM:SS)')
    ax2.set_ylabel('Relative Humidity (%rh) ')

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.20)


ani = FuncAnimation(
    fig, animate, fargs=(time_stamp, temp, hum), interval=1000
)
plt.show()
