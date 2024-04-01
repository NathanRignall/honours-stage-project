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

# rt-pi4-socket-times
plt.figure(figsize=(8,3))
rt_pi4_socket_times = np.abs(data['rt-pi4-socket-times-child']['time'] - data['rt-pi4-socket-times-parent']['time'])
plt.plot(rt_pi4_socket_times, label='Latency')
plt.plot([np.mean(rt_pi4_socket_times)] * len(rt_pi4_socket_times), label='Average', linestyle='--')
rt_pi4_socket_times_jitter = np.abs(rt_pi4_socket_times - np.roll(rt_pi4_socket_times, 1))
plt.plot(rt_pi4_socket_times_jitter, label='Jitter')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-socket-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-pi4-socket-times-blocking
plt.figure(figsize=(8,3))
rt_pi4_socket_times_blocking = np.abs(data['rt-pi4-socket-times-child-blocking']['time'] - data['rt-pi4-socket-times-parent-blocking']['time'])
plt.plot(rt_pi4_socket_times_blocking, label='Latency')
plt.plot([np.mean(rt_pi4_socket_times_blocking)] * len(rt_pi4_socket_times_blocking), label='Average', linestyle='--')
rt_pi4_socket_times_blocking_jitter = np.abs(rt_pi4_socket_times_blocking - np.roll(rt_pi4_socket_times_blocking, 1))
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-socket-times-blocking.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-pi4-mem-times
plt.figure(figsize=(8,3))
rt_pi4_mem_times = np.abs(data['rt-pi4-mem-times-child']['time'] - data['rt-pi4-mem-times-parent']['time'])
plt.plot(rt_pi4_mem_times, label='Latency')
plt.plot([np.mean(rt_pi4_mem_times)] * len(rt_pi4_mem_times), label='Average', linestyle='--')
rt_pi4_mem_times_jitter = np.abs(rt_pi4_mem_times - np.roll(rt_pi4_mem_times, 1))
plt.plot(rt_pi4_mem_times_jitter, label='Jitter')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-mem-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-pi4-compare-times
plt.figure(figsize=(8,3))
plt.plot(rt_pi4_socket_times, label='Socket')
plt.plot(rt_pi4_socket_times_blocking, label='Socket Blocking')
plt.plot(rt_pi4_mem_times, label='Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-compare-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-pi4-compare-times-jitter
plt.figure(figsize=(8,3))
plt.plot(rt_pi4_socket_times_jitter, label='Socket')
plt.plot(rt_pi4_socket_times_blocking_jitter, label='Socket Blocking')
plt.plot(rt_pi4_mem_times_jitter, label='Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-compare-times-jitter.pdf', format='pdf', bbox_inches='tight')
plt.close()

# pi5-socket-times
plt.figure(figsize=(8,3))
pi5_socket_times = np.abs(data['pi5-socket-times-child']['time'] - data['pi5-socket-times-parent']['time'])
plt.plot(pi5_socket_times, label='Latency')
plt.plot([np.mean(pi5_socket_times)] * len(pi5_socket_times), label='Average', linestyle='--')
pi5_socket_times_jitter = np.abs(pi5_socket_times - np.roll(pi5_socket_times, 1))
plt.plot(pi5_socket_times_jitter, label='Jitter')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../pi5-socket-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# pi5-socket-times-blocking
plt.figure(figsize=(8,3))
pi5_socket_times_blocking = np.abs(data['pi5-socket-times-child-blocking']['time'] - data['pi5-socket-times-parent-blocking']['time'])
plt.plot(pi5_socket_times_blocking, label='Latency')
plt.plot([np.mean(pi5_socket_times_blocking)] * len(pi5_socket_times_blocking), label='Average', linestyle='--')
pi5_socket_times_blocking_jitter = np.abs(pi5_socket_times_blocking - np.roll(pi5_socket_times_blocking, 1))
plt.plot(pi5_socket_times_blocking_jitter, label='Jitter')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../pi5-socket-times-blocking.pdf', format='pdf', bbox_inches='tight')
plt.close()

# pi5-mem-times
plt.figure(figsize=(8,3))
pi5_mem_times = np.abs(data['pi5-mem-times-child']['time'] - data['pi5-mem-times-parent']['time'])
plt.plot(pi5_mem_times, label='Latency')
plt.plot([np.mean(pi5_mem_times)] * len(pi5_mem_times), label='Average', linestyle='--')
pi5_mem_times_jitter = np.abs(pi5_mem_times - np.roll(pi5_mem_times, 1))
plt.plot(pi5_mem_times_jitter, label='Jitter')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../pi5-mem-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# pi5-compare-times
plt.figure(figsize=(8,3))
plt.plot(pi5_socket_times, label='Socket')
plt.plot(pi5_socket_times_blocking, label='Socket Blocking')
plt.plot(pi5_mem_times, label='Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../pi5-compare-times.pdf', format='pdf', bbox_inches='tight')
plt.close()

# pi5-compare-times-jitter
plt.figure(figsize=(8,3))
plt.plot(pi5_socket_times_jitter, label='Socket')
plt.plot(pi5_socket_times_blocking_jitter, label='Socket Blocking')
plt.plot(pi5_mem_times_jitter, label='Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../pi5-compare-times-jitter.pdf', format='pdf', bbox_inches='tight')
plt.close()

# rt-pi4 vs pi5
plt.figure(figsize=(8,3))
plt.plot(rt_pi4_socket_times_blocking, label='rt-pi4 Socket Blocking')
plt.plot(rt_pi4_mem_times, label='rt-pi4 Memory')
plt.plot(pi5_socket_times_blocking, label='pi5 Socket Blocking')
plt.plot(pi5_mem_times, label='pi5 Memory')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(1000, 2000)
plt.ylim(0, 100)
plt.xlabel('Time Step')
plt.ylabel('Latency (us)')
plt.savefig('../rt-pi4-vs-pi5.pdf', format='pdf', bbox_inches='tight')
plt.close()