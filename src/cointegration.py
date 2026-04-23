# Import Libraries
import pandas as pd
import yfinance as yf
import numpy as np
from itertools import combinations
from statsmodels.tsa.stattools import coint
import seaborn as sns
import matplotlib.pyplot as plt

# Runs cointegration test on all possible pairs
# Input: yfinance dataframe with 2 or more asset series
# Output: Dataframe of pair comibinations, t-statisic, p-value, and 5% critical value

def find_cointegrated_pairs(df):
    tickers = df.columns.levels[1]                
    ticker_pairs = list(combinations(tickers, 2))                         
    results = []
    
    for t1, t2 in ticker_pairs:
        # Removes N/A in case yfinance has missing data between series                     
        pair_data = df['Close'][[t1,t2]].dropna()      

        # Normalize prices to log (this is not necessary for coint but provides more robust results)
        pair1 = np.log(pair_data[t1])
        pair2 = np.log(pair_data[t2])

        coint_t, pvalue, crit_value = coint(pair1, pair2)
        
        row ={
            'Asset_1': t1,
            'Asset_2': t2,
            'P-Value': pvalue,
            'T-Stat': coint_t,
            'Crit_5%': crit_value[1],
            'Significant': pvalue < 0.05 and coint_t < crit_value[1]
        }

        results.append(row)
        results_df = pd.DataFrame(results)

        #Debug
        # print(f" Pair: {t1} and {t2} | P-Value: {pvalue:.4f}") 

    return results_df

### Example Usage ###

# 1. Define and download basket of assets
tickers = ['ES=F', "NQ=F", "YM=F" ]
data = yf.download(tickers, start="2026-01-01", end="2026-02-28", interval='1d',)

# 2. Run Cointegration test
example = find_cointegrated_pairs(data)

# 3. Export Results Report
example.to_csv(
    'Example_Report.csv',
    index= False,
    float_format = '%.5f',
    encoding='utf-8'
)