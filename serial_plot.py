import serial
import matplotlib.pyplot as plt
from collections import deque

PORT = 'COM3'
BAUD = 115200
MAX_POINTS = 20    # 顯示最近20個

ser = serial.Serial(PORT, BAUD)
temps = deque(maxlen=MAX_POINTS)
hums  = deque(maxlen=MAX_POINTS)

plt.ion()
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

line1, = ax1.plot([], [], label='Temp (°C)')
line2, = ax2.plot([], [], label='Humidity (%)')

ax1.set_ylim(20, 35)
ax2.set_ylim(30, 100)

ax1.set_xlabel("Samples")
ax1.set_ylabel("Temperature (°C)")
ax2.set_ylabel("Humidity (%)")

while True:
    try:
        data = ser.readline().decode().strip()
        t, h = map(float, data.split(","))

        temps.append(t)
        hums.append(h)

        line1.set_data(range(len(temps)), temps)
        line2.set_data(range(len(hums)), hums)

        ax1.set_xlim(0, MAX_POINTS)

        plt.pause(0.01)
    except:
        pass
    