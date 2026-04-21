# Import Libraries
import pandas as pd
import yfinance as yf
import numpy as np
from statsmodels.tsa.stattools import coint

import seaborn as sns
import matplotlib.pyplot as plt

# Define and downlaod Basket of assets
tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, start="2023-01-01", end="2025-01-01", interval='1d')

# Select 'Adj Close' safely
# This handles the MultiIndex by pulling only the 'Adj Close' column level
# if 'Adj Close' in df.columns.levels[0]:
#     data = df['Adj Close']
# else:
#     # Fallback in case yfinance only returned 'Close'
#     data = df['Close']

print(data.head())

# # Scout Algortithm; run cointegration test on all possible pairs
# def find_cointegrated_pairs(data):
#     n = data.shape[1]
#     score_matrix = np.zeroes((n,n))
#     pvalue_matrix = np.ones((n,n))
#     keys = data.keys()
#     pairs = []

#     for i in range(n):
#         for j in range (i+1, n):
#             S1 = data[keys[i]]
#             S2 = data[keys[j]]
#             # coint returns: test_stat, pvalue, crtical_values
#             result = coint(S1, S2)
#             score = result[0]
#             pvalue = result[1]

#             score_matrix[i,j] = score
#             pvalue_matrix[i,j] = pvalue

#             if pvalue <0.05:
#                 pairs.append((keys[i],keys[j], pvalue))

#     return score_matrix, pvalue_matrix, pairs

# scores, pvalues, pairs = find_cointegrated_pairs(data)

# # Visualize result relationships

# plt.figure(figsize=(10,8))
# sns.heatmap(pvalues,xticklabels=tickers, 
#             yticklabels=tickers, 
#             cmap='RdYlGn_r', 
#             mask = (pvalues>=0.05))

# plt.title("Cointegration P-Values (Siginficant Pairs Only)")
# plt.show()

