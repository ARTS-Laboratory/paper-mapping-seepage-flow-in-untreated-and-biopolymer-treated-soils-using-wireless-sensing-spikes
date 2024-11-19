# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:57:34 2024

@author: chypu
https://geostat-framework.readthedocs.io/_/downloads/pykrige/en/v1.5.0/pdf/
# 1D ordinary kringing with nlag, nuggest, variogramrange control
"""


import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

#%%
# Updating Parameters for Paper
plt.rcdefaults()
params = {
    'lines.linewidth' :1,
    'lines.markersize' :1,
   'axes.labelsize': 8,
    'axes.titlesize':8,
    'axes.titleweight':'normal',
    'font.size': 8,
    'font.family': 'Times New Roman', # 'Times New RomanArial'
    'font.weight': 'normal',
    'mathtext.fontset': 'stix',
    'legend.shadow':'False',
   'legend.fontsize': 8,
   'xtick.labelsize':8,
   'ytick.labelsize':8,
   'text.usetex': False,
    'figure.autolayout': True,
   'figure.figsize': [3.5,3] # width and height in inch 3.5,2.54(max width = 7.5", max length = 10") [6.0,4.05
   }
plt.rcParams.update(params)

#%% To implement a basic Boolean operator to set any inferred voltage below 0 to zero, you can simply add a line of code after executing kriging. 
#%%To avoid extrapolation of kriging results beyond the range of the original data points, 
#%% 10% Silt final

# Define your data
x = np.array([13.5, 13.5, 13.5, 13.5, 13.5])  # x-coordinate for 5 spikes
y = np.array([5, 20, 35, 50, 65])  # y-coordinate for 5 spike


# Voltage data for different timestamp values
V_values = [
    np.array([0.441, 0.377, 0.467, 0.461, 0.425]),  # 1st time stamp TS1: 50sec
    np.array([0.996, 0.958, 1.09, 0.561, 0.483]),  # 2nd time stamp TS2: 1750 sec
    np.array([0.996, 0.941, 1.061, 1.161, 1.187]),  # 3rd  time stamp TS3: 4005 sec
    ]

# Define nlags for each timestamp
nlags_values = [6, 6, 6]

# Define nugget effect values for each timestamp
nugget_values = [0.1, 0.1,0.1]

# Define markers for each timestamp
# markers = ['o', 's', 'D', '^', 'v', 'x']
markers = ['o', 's', 'D']
# Accumulate kriging results for all timestamps
all_timestamps_results = []

# Iterate over different timestamp values
for i, (V, nlags, nugget) in enumerate(zip(V_values, nlags_values, nugget_values), start=1):
    # Ordinary Kriging with a nugget effect
    OK = OrdinaryKriging(
        x,
        y,
        V,
        variogram_model='gaussian',
        variogram_parameters=[15, 30, nugget], 
        nlags=nlags,
        verbose=True,
        enable_plotting=False,
        weight=True,
    )

    # Define grid
    gridx = np.linspace(min(x), max(x), 100) 
    gridy = np.linspace(min(y), max(y), 100)
    
    # Execute kriging
    zstar, ss = OK.execute("grid", gridx, gridy)
    
    # Set negative values to zero # boolean oprator set as V<0-->0
    zstar[zstar < 0] = 0

    # Append kriging results to the list
    all_timestamps_results.append((gridy, zstar[:, 0], f'TS {i}'))

# Plotting all timestamps and scatter plots in a single plot
for gridy, kriging_result, label in all_timestamps_results:
    plt.plot(gridy, kriging_result, label=label)

# Scatter plot of original data points for each timestamp with different markers
for i, (V, marker) in enumerate(zip(V_values, markers), start=1):
    plt.scatter(y, V, marker=marker, s=25, label=f'TS {i}')
plt.grid()
plt.xlabel('location (cm)')
plt.ylabel('voltage (V)')

# Move the legend outside of the plot at the top
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4, facecolor='white', edgecolor='black', framealpha=1)


# plt.legend()
plt.savefig('plots/Silt_Timestamp_all_1DKriging_Plot_boolean.png', dpi=250)
plt.savefig('plots/Silt_Timestamp_all_1DKriging_Plot_boolean.pdf', dpi=250)
plt.show()


