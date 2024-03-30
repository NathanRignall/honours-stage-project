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

# rt-socket-test-sleep
plt.figure(figsize=(8,3))
plt.semilogy(data['rt-socket-test-times-parent']['sleep'], label='Sleep')
plt.semilogy(data['rt-socket-test-times-parent']['execute'], label='Duration')
rt_socket_test_diff = np.abs(data['rt-socket-test-times-parent']['sleep'] + data['rt-socket-test-times-parent']['execute'])
plt.plot(rt_socket_test_diff, label='Difference', linestyle='--')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 10000)
plt.ylim(pow(10,0),pow(10,6))
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.savefig('../rt-socket-test-sleeps.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-socket-test-times
plt.figure(figsize=(8,3))
rt_socket_test_times = np.abs(data['rt-socket-test-times-child']['time'] - data['rt-socket-test-times-parent']['time'])
plt.semilogy(rt_socket_test_times, label='Time Difference')
plt.semilogy([np.mean(rt_socket_test_times)] * len(rt_socket_test_times), label='Average', linestyle='--')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 10000)
plt.ylim(pow(10,0),pow(10,3))
plt.xlabel('Time Step')
plt.ylabel('Time Difference (us)')
plt.savefig('../rt-socket-test-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-mem-test-sleep
plt.figure(figsize=(8,3))
plt.semilogy(data['rt-mem-test-times-parent']['sleep'], label='Sleep')
plt.semilogy(data['rt-mem-test-times-parent']['execute'], label='Duration')
rt_mem_test_diff = np.abs(data['rt-mem-test-times-parent']['sleep'] + data['rt-mem-test-times-parent']['execute'])
plt.plot(rt_mem_test_diff, label='Difference', linestyle='--')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 10000)
plt.ylim(pow(10,0),pow(10,6))
plt.xlabel('Time Step')
plt.ylabel('Time (us)')
plt.savefig('../rt-mem-test-sleeps.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-mem-test-times
plt.figure(figsize=(8,3))
rt_mem_test_times = np.abs(data['rt-mem-test-times-child']['time'] - data['rt-mem-test-times-parent']['time'])
plt.semilogy(rt_mem_test_times, label='Time Difference')
plt.semilogy([np.mean(rt_mem_test_times)] * len(rt_mem_test_times), label='Average', linestyle='--')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 10000)
plt.ylim(pow(10,0),pow(10,3))
plt.xlabel('Time Step')
plt.ylabel('Time Difference (us)')
plt.savefig('../rt-mem-test-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# comparison times
plt.figure(figsize=(8,3))
plt.semilogy(rt_socket_test_times, label='Socket')
plt.semilogy(rt_mem_test_times, label='Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 10000)
plt.ylim(pow(10,0),pow(10,3))
plt.xlabel('Time Step')
plt.ylabel('Time Difference (us)')
plt.savefig('../rt-comapre-test-times.pdf', format='pdf', bbox_inches='tight')
plt.close()