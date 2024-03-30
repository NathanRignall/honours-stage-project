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
elafry_times_sleep = []
elafry_times_duration = []
elafry_times_one = []
elafry_times_two = []
elafry_times_three = []
elafry_times_four = []
# loop through each row in the data['elafry-times'] 
for index, row in data['elafry-times'].iterrows():
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
plt.figure(figsize=(8,3))
elafry_one_two = [elafry_times_two[i] - elafry_times_one[i] for i in range(len(elafry_times_one))]
elafry_two_three = [elafry_times_three[i] - elafry_times_two[i] for i in range(len(elafry_times_one))]
elafry_three_four = [elafry_times_four[i] - elafry_times_three[i] for i in range(len(elafry_times_one))]
elafry_total = [elafry_times_sleep[i] + elafry_times_duration[i] for i in range(len(elafry_times_sleep))]
plt.plot(elafry_one_two, label='Scheduler')
plt.plot(elafry_two_three, label='Messages')
plt.plot(elafry_three_four, label='Management')
plt.plot(elafry_times_sleep, label='Sleep')
plt.plot(elafry_total, label='Total')
plt.legend()
plt.grid()
plt.margins(0)
plt.ylim(0, 4000)
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.savefig('../elafry-times.pdf', format='pdf', bbox_inches='tight')
plt.close()