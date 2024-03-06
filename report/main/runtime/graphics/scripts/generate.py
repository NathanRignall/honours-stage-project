import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

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

# Compare i100 for linux and linux rt
plt.figure(figsize=(8,3))
plt.semilogy(data['linux-i100-1h_histogram']['time'], data['linux-i100-1h_histogram']['core1'], label='Core 1')
plt.semilogy(data['linux-rt-i100-1h_histogram']['time'], data['linux-rt-i100-1h_histogram']['core1'], label='Core 1 (RT)')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 500)
plt.ylim( (pow(10,0),pow(10,8)) )
plt.xlabel('Latency (us)')
plt.ylabel('Frequency')
plt.savefig('../linux-i100-1h.pdf', format='pdf', bbox_inches='tight')
plt.close()

# Compare i100 for linux and linux rt under CPU load
plt.figure(figsize=(8,3))
plt.semilogy(data['linux-i100-1h-sc4_histogram']['time'], data['linux-i100-1h-sc4_histogram']['core1'], label='Core 1')
plt.semilogy(data['linux-rt-i100-1h-sc4_histogram']['time'], data['linux-rt-i100-1h-sc4_histogram']['core1'], label='Core 1 (RT)')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 500)
plt.ylim( (pow(10,0),pow(10,8)) )
plt.xlabel('Latency (us)')
plt.ylabel('Frequency')
plt.savefig('../linux-i100-1h-sc4.pdf', format='pdf', bbox_inches='tight')
plt.close()

# Compare i100 for linux and linux rt under Memory load
plt.figure(figsize=(8,3))
plt.semilogy(data['linux-i100-1h-sm4_histogram']['time'], data['linux-i100-1h-sm4_histogram']['core1'], label='Core 1')
plt.semilogy(data['linux-rt-i100-1h-sm4_histogram']['time'], data['linux-rt-i100-1h-sm4_histogram']['core1'], label='Core 1 (RT)')
plt.legend()
plt.grid()
plt.margins(0)
plt.xlim(0, 500)
plt.ylim( (pow(10,0),pow(10,8)) )
plt.xlabel('Latency (us)')
plt.ylabel('Frequency')
plt.savefig('../linux-i100-1h-sm4.pdf', format='pdf', bbox_inches='tight')
plt.close()

# xen-i100-1h
# plt.figure(figsize=(12,4))
# plt.semilogy(data['xen-i100-1h_histogram']['time'], data['xen-i100-1h_histogram']['core1'], label='Dom0')
# plt.semilogy(data['xen-vm-rt-guest-i100-1h_histogram']['time'], data['xen-vm-guest-i100-1h_histogram']['core1'], label='Dom1')
# plt.legend()
# plt.grid()
# plt.margins(0)
# plt.xlim(0, 500)
# plt.ylim(0, 100000000)
# plt.xlabel('Latency (us)')
# plt.ylabel('Frequency')
# plt.savefig('xen-i100-1h.pdf', format='pdf', bbox_inches='tight')
# plt.close()