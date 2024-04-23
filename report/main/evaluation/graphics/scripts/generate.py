import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=plt.cm.Set1(np.linspace(0, 1, 10)))

# Load all .csv files in ./store folder
def load_data():
    data = {}
    for file in os.listdir("../data"):
        if file.endswith(".csv"):
            name = file.split(".")[0]
            data[name] = pd.read_csv(f"../data/{file}")
    return data

# Load all .csv files in ./store folder
data = load_data()

# elafry-times
elafry_times_period = []
elafry_times_sleep = []
elafry_times_duration = []
elafry_times_one = []
elafry_times_two = []
elafry_times_three = []
elafry_times_four = []
elafry_times_five = []
# loop through each row in the data['elafry-times'] 
for index, row in data['elafry-plant-times'].iterrows():
    if row['type'] == 0:
        elafry_times_sleep.append(row['sleep'])
        elafry_times_duration.append(row['execute'])
        elafry_times_one.append(row['time'])
    elif row['type'] == 1:
        elafry_times_two.append(row['time'])
    elif row['type'] == 2:
        elafry_times_three.append(row['time'])
    elif row['type'] == 3:
        elafry_times_four.append(row['time'])
    elif row['type'] == 4:
        elafry_times_five.append(row['time'])

plt.figure(figsize=(8,3))
elafry_one_two = [elafry_times_two[i] - elafry_times_one[i] for i in range(len(elafry_times_one))]
elafry_two_three = [elafry_times_three[i] - elafry_times_two[i] for i in range(len(elafry_times_one))]
elafry_three_four = [elafry_times_four[i] - elafry_times_three[i] for i in range(len(elafry_times_one))]
elafry_four_five = [elafry_times_five[i] - elafry_times_four[i] for i in range(len(elafry_times_one))]
elafry_total = [elafry_times_sleep[i] + elafry_times_duration[i] for i in range(len(elafry_times_one))]
plt.plot(elafry_total, label='Total Time')
plt.plot(elafry_one_two, label='Scheduler Time')
plt.plot(elafry_two_three, label='Messages Time')
plt.plot(elafry_three_four, label='State Time')
plt.plot(elafry_four_five, label='Management Time')
plt.legend()
plt.grid()
plt.margins(0)
plt.ylim(0, 2000)
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.savefig('../elafry-plant-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

#  plot times again but zoom
plt.figure(figsize=(8,3))
plt.plot(elafry_total, label='Total Time')
plt.plot(elafry_one_two, label='Scheduler Time')
plt.plot(elafry_two_three, label='Messages Time')
plt.plot(elafry_three_four, label='State Time')
plt.plot(elafry_four_five, label='Management Time')
plt.legend()
plt.grid()
plt.margins(0)
plt.ylim(0, 2000)
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.xlim(15000, 15050)
plt.savefig('../elafry-plant-times-zoom.pdf', format='pdf', bbox_inches='tight')
plt.close()

plt.figure(figsize=(8,3))
plt.plot(data['elafry-plant-data']['position'], label='Height (m)')
plt.plot(data['elafry-plant-data']['thrust'], label='Thrust (N)')
plt.plot(data['elafry-plant-data']['set'], label='Height Setpoint (m)')
# loop over all loop
loop = data['elafry-plant-data']['loop']
new_loop = []
for i in range(len(loop) - 1):
    if loop[i + 1] - loop[i]  == 1:
        new_loop.append(0)
    else:
        new_loop.append(10)
plt.plot(new_loop, label='Loop')
# find the index where false goes to true
update = data['elafry-plant-data']['update']
update_pos = 0
for i in range(len(update) - 1):
    if update[i] == 0 and update[i + 1] == 1:
        update_pos = i
        break
plt.axvline(x=update_pos, color='black', linestyle='--', label='Update')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.savefig('../elafry-plant-data.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot plant again but zoom at x = 9950 to 10050
plt.figure(figsize=(8,3))
plt.plot(data['elafry-plant-data']['position'], label='Height (m)')
plt.plot(data['elafry-plant-data']['thrust'], label='Thrust (N)')
plt.plot(data['elafry-plant-data']['set'], label='Height Setpoint (m)')
plt.axvline(x=update_pos, color='black', linestyle='--', label='Update')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlabel('Time Step')
plt.ylabel('Value')
plt.xlim(9995, 10005)
plt.ylim(0, 25)
plt.savefig('../elafry-plant-data-zoom.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot elafry harness times same as elafry plant times

# elafry-harness-times
elafry_harness_times_period = []
elafry_harness_times_sleep = []
elafry_harness_times_duration = []
elafry_harness_times_one = []
elafry_harness_times_two = []
elafry_harness_times_three = []
elafry_harness_times_four = []
elafry_harness_times_five = []

# loop through each row in the data['elafry-harness-times']
for index, row in data['elafry-harness-times'].iterrows():
    if row['type'] == 0:
        elafry_harness_times_sleep.append(row['sleep'])
        elafry_harness_times_duration.append(row['execute'])
        elafry_harness_times_one.append(row['time'])
    elif row['type'] == 1:
        elafry_harness_times_two.append(row['time'])
    elif row['type'] == 2:
        elafry_harness_times_three.append(row['time'])
    elif row['type'] == 3:
        elafry_harness_times_four.append(row['time'])
    elif row['type'] == 4:
        elafry_harness_times_five.append(row['time'])

plt.figure(figsize=(8,3))
elafry_harness_one_two = [elafry_harness_times_two[i] - elafry_harness_times_one[i] for i in range(len(elafry_harness_times_one))]
elafry_harness_two_three = [elafry_harness_times_three[i] - elafry_harness_times_two[i] for i in range(len(elafry_harness_times_one))]
elafry_harness_three_four = [elafry_harness_times_four[i] - elafry_harness_times_three[i] for i in range(len(elafry_harness_times_one))]
elafry_harness_four_five = [elafry_harness_times_five[i] - elafry_harness_times_four[i] for i in range(len(elafry_harness_times_one))]
elafry_harness_total = [elafry_harness_times_sleep[i] + elafry_harness_times_duration[i] for i in range(len(elafry_harness_times_one))]
plt.plot(elafry_harness_total, label='Total Time')
plt.plot(elafry_harness_one_two, label='Scheduler Time')
plt.plot(elafry_harness_two_three, label='Messages Time')
plt.plot(elafry_harness_three_four, label='State Time')
plt.plot(elafry_harness_four_five, label='Management Time')
plt.legend()
plt.grid()
plt.margins(0)
plt.ylim(0, 2000)
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.savefig('../elafry-harness-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# plot harness again but zoom at x = 9950 to 10050
plt.figure(figsize=(8,3))
plt.plot(elafry_harness_total, label='Total Time')
plt.plot(elafry_harness_one_two, label='Scheduler Time')
plt.plot(elafry_harness_two_three, label='Messages Time')
plt.plot(elafry_harness_three_four, label='State Time')
plt.plot(elafry_harness_four_five, label='Management Time')
plt.legend()
plt.grid()
plt.margins(0)
plt.ylim(0, 2000)
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.xlim(990, 1090)
plt.savefig('../elafry-harness-times-zoom.pdf', format='pdf', bbox_inches='tight')
plt.close()
