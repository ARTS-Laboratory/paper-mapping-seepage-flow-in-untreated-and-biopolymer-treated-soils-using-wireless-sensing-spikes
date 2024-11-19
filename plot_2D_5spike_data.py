# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:58:49 2024

@author: chypu
"""

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import ScalarFormatter #n this example, ScalarFormatter is used to format the y-axis ticks in scientific notation. 
#%% plotting with specific parameters
plt.rcdefaults()
# Updating Parameters for Paper
params = {
    'lines.linewidth' :1,
    'lines.markersize' :0.5,
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
   'figure.figsize': [3.5,2.7] # 6,4 for test3, ansys data 6,7
   }
plt.rcParams.update(params)




#%% compact sand data
# Reading data
filename = "data/final_post_process_data/compact_sand_final.csv" 

D1=pd.read_csv(filename,skiprows=1)
# t1=D1.iloc[:,0] # time in second
t1=D1.iloc[:,0]/60 # time in minute
# t1=D1.iloc[:,0] # time in sec
s1=D1.iloc[:,1] # spike 1
s2=D1.iloc[:,2] #spike 2
s3=D1.iloc[:,3] # spike 3
s4=D1.iloc[:,4] # spike 4
# s5=D1.iloc[:,5] # spike 5

#%%
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(t1,s1,linestyle='-', label='spike 1')
ax.plot(t1,s2,linestyle='--', label='spike 2')
ax.plot(t1,s3,linestyle='-.', label='spike 3')
ax.plot(t1,s4,linestyle=':',label='spike 4')
ax.legend(loc='lower right',bbox_to_anchor=(0.95,0.01),ncol=1,facecolor='white', edgecolor = 'black', framealpha=1)
# plt.xlim(0,2365/60)
plt.ylim(0.006,1.15)
# plt.xlabel('time (sec)') #sample points
plt.xlabel('time (minute)') #sample points
plt.ylabel('voltage (v)')

# Add TS labels
time_points = [35/60, 970/60, 1700/60]  # Example time points for TS 1, TS 2, TS 3
labels = ['TS 1', 'TS 2', 'TS 3']

for time, label in zip(time_points, labels):
    plt.axvline(x=time, color='k', linestyle='--')  # Add a vertical dashed line
    plt.text(time, 1.17, label, rotation=0, verticalalignment='bottom', horizontalalignment='center')  # Annotate with TS labels

# Save the plot
plt.savefig('plots/4spikes_2D_plot_comsand_TS3.pdf', dpi=100)
plt.savefig('plots/4spikes_2D_plot_comsand_TS3.png', dpi=100)


#%% 0.5% XG Biopolymers final
# Reading data
filename = "data/final_post_process_data/0.5% XG Biopolymers_final.csv" 

D1=pd.read_csv(filename,skiprows=1)
# t1=D1.iloc[:,0] # time in second
t1=D1.iloc[:,0]/60 # time in minute
# t1=D1.iloc[:,0] # time in sec
s1=D1.iloc[:,1] # spike 1
s2=D1.iloc[:,2] #spike 2
s3=D1.iloc[:,3] # spike 3
s4=D1.iloc[:,4] # spike 4
s5=D1.iloc[:,5] # spike 5

#%%
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(t1,s1,linestyle='-', label='spike 1')
ax.plot(t1,s2,linestyle='--', label='spike 2')
ax.plot(t1,s3,linestyle='-.', label='spike 3')
ax.plot(t1,s4,linestyle=':',label='spike 4')
ax.plot(t1,s5,linestyle='-', label='spike 5')
ax.legend(loc='upper right',bbox_to_anchor=(1,1.0),ncol=1,facecolor='white', edgecolor = 'black', framealpha=1)
# plt.xlim(0,2365/60)
plt.ylim(0.006,1.63)
# plt.xlabel('time (sec)') #sample points
plt.xlabel('time (minute)') #sample points
plt.ylabel('voltage (v)')

# Add TS labels
time_points = [45/60, 1450/60, 4000/60]  # Example time points for TS 1, TS 2, TS 3
labels = ['TS 1', 'TS 2', 'TS 3']

for time, label in zip(time_points, labels):
    plt.axvline(x=time, color='k', linestyle='--')  # Add a vertical dashed line
    plt.text(time, 1.67, label, rotation=0, verticalalignment='bottom', horizontalalignment='center')  # Annotate with TS labels

# Save the plot
plt.savefig('plots/5spikes_2D_plot_Biopolymers_TS3.pdf', dpi=100)
plt.savefig('plots/5spikes_2D_plot_Biopolymers_TS3.png', dpi=100)

#%% 10% Silt_final
# Reading data
filename = "data/final_post_process_data/10% Silt_final.csv" 

D1=pd.read_csv(filename,skiprows=1)
# t1=D1.iloc[:,0] # time in second
t1=D1.iloc[:,0]/60 # time in minute
# t1=D1.iloc[:,0] # time in sec
s1=D1.iloc[:,1] # spike 1
s2=D1.iloc[:,2] #spike 2
s3=D1.iloc[:,3] # spike 3
s4=D1.iloc[:,4] # spike 4
s5=D1.iloc[:,5] # spike 5

#%%
fig1 = plt.figure()
ax = fig1.add_subplot(111)
ax.plot(t1,s1,linestyle='-', label='spike 1')
ax.plot(t1,s2,linestyle='--', label='spike 2')
ax.plot(t1,s3,linestyle='-.', label='spike 3')
ax.plot(t1,s4,linestyle=':',label='spike 4')
ax.plot(t1,s5,linestyle='-', label='spike 5')
ax.legend(loc='lower right',bbox_to_anchor=(1,0.01),ncol=1,facecolor='white', edgecolor = 'black', framealpha=1)
# plt.xlim(0,2365/60)
plt.ylim(0.006,1.3)
# plt.xlabel('time (sec)') #sample points
plt.xlabel('time (minute)') #sample points
plt.ylabel('voltage (v)')

# Add TS labels
time_points = [50/60, 1750/60, 4005/60]  # Example time points for TS 1, TS 2, TS 3
labels = ['TS 1', 'TS 2', 'TS 3']

for time, label in zip(time_points, labels):
    plt.axvline(x=time, color='k', linestyle='--')  # Add a vertical dashed line
    plt.text(time, 1.3, label, rotation=0, verticalalignment='bottom', horizontalalignment='center')  # Annotate with TS labels

# Save the plot
plt.savefig('plots/5spikes_2D_plot_10per_Silt_TS3.pdf', dpi=100)
plt.savefig('plots/5spikes_2D_plot_10per_Silt_TS3.png', dpi=100)