# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:55:14 2024

@author: chypu

https://geostat-framework.readthedocs.io/_/downloads/pykrige/en/v1.5.0/pdf/
# 1D ordinary kringing with nlag, nuggest, variogramrange control
"""

import IPython as IP
IP.get_ipython().run_line_magic('reset', '-sf')

import numpy as np
import matplotlib.pyplot as plt
from pykrige.ok import OrdinaryKriging

plt.close('all')
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


def calculate_resistance(V_out, V_in=3.3, R2=6800):
    """
    Calculate the resistance of the material using a voltage divider formula.

    Parameters:
    V_out (float or np.ndarray): Measured output voltage in volts.
    V_in (float): Input voltage in volts (default: 3.3V).
    R2 (float): Resistance of the known resistor in ohms (default: 6.8 kΩ).

    Returns:
    float or np.ndarray: Calculated resistance in ohms.
    """
    if isinstance(V_out, np.ndarray):
        if np.any((V_out <= 0) | (V_out >= V_in)):
            raise ValueError("V_out values must be between 0 and V_in for a valid calculation.")
    elif V_out <= 0 or V_out >= V_in:
        raise ValueError("V_out must be between 0 and V_in for a valid calculation.")
    
    R1 = (R2 * (V_in - V_out)) / V_out
    return R1

#%% To implement a basic Boolean operator to set any inferred voltage below 0 to zero, you can simply add a line of code after executing kriging. 
#%%To avoid extrapolation of kriging results beyond the range of the original data points, 

#%% 0.5% XG Biopolymers 

# Define your data
x = np.array([13.5, 13.5, 13.5, 13.5, 13.5])  # x-coordinate for 5 spikes
y = np.array([5, 20, 35, 50, 65])  # y-coordinate for 5 spike


# Voltage data for different timestamp values
V_values = [
    np.array([1.038, 0.806, 1.367, 1.558, 1.241]),  # 1st time stamp TS1: 45 sec
    np.array([0.7, 0.487, 0.867, 1.129, 0.812]),  # 2nd time stamp TS2: 1450 sec
    np.array([0.538, 0.406, 0.641, 0.851, 0.625]),  # 3rd  time stamp TS3: 4000 sec
    ]

# convert the V values to R values
R_values = [calculate_resistance(V_out_array) for V_out_array in V_values]

# For ease of coding, recast R as V
# V_values = R_values


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
for i, (R, nlags, nugget) in enumerate(zip(R_values, nlags_values, nugget_values), start=1):
    # Ordinary Kriging with a nugget effect
    OK = OrdinaryKriging(
        x,
        y,
        R,
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
    
    # Set negative values to zero # boolean oprator set as R<0-->0
    zstar[zstar < 0] = 0

    # Append kriging results to the list
    all_timestamps_results.append((gridy, zstar[:, 0], f'TS {i}'))

plt.figure(figsize=(3,2.75))
# Plotting all timestamps and scatter plots in a single plot
for gridy, kriging_result, label in all_timestamps_results:
    plt.plot(gridy, kriging_result/1000, label=label)

# Scatter plot of original data points for each timestamp with different markers
for i, (R, marker) in enumerate(zip(R_values, markers), start=1):
    plt.scatter(y, R/1000, marker=marker, s=25, label=f'TS {i}')
plt.grid()
plt.xlabel('location (cm)')
plt.ylabel('resistance (k$\Omega$)')

# Move the legend outside of the plot at the top
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4, facecolor='white', edgecolor='black', framealpha=1)


# plt.legend()
plt.savefig('plots/Biopolymers_Timestamp_all_1DKriging_Plot_boolean.png', dpi=250)
plt.savefig('plots/Biopolymers_Timestamp_all_1DKriging_Plot_boolean.pdf', dpi=250)
plt.show()

