import sys
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

def autocorr_range(ts, lag_range):
    ac_array = []
    for lag in lag_range:
        ac_array.append(pd.Series.autocorr(ts, lag))
    return ac_array

def decay_func(x, a, tau, b):
    return a * np.exp(-(x/tau)) + b

def decay(data, ROI, lag_max):
    xvar = list(range(lag_max))
    popt, pcov = curve_fit(decay_func, xvar, autocorr_range(data[ROI], xvar))
    return popt[1] # Return the decay constant

ts_file, max_lag, out_path = sys.argv[1:4]

ts_df = pd.read_csv(ts_file, delimiter='\t', header=None)

decays = []
for ROI in range(ts_df.shape[1]):
    decays.append(decay(ts_df, ROI, int(max_lag)))
    
np.savetxt(out_path, np.array(decays))