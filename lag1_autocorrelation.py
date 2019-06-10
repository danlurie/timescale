import numpy as np
import pandas as pd
import sys

ts_file, out_path = sys.argv[1:3]

ts_df = pd.read_csv(ts_file, delimiter='\t', header=None)

lag1_array = []
for ROI in range(ts_df.shape[1]):
    lag1_array.append(pd.Series.autocorr(ts_df[ROI], 1))
    
np.savetxt(out_path, np.array(lag1_array))