# pip install pandas
# pip install finance-datareader
# pip install matplotlib
# pip install openpyxl

import matplotlib.pyplot as plt
import pandas as pd
import FinanceDataReader as fdr
# 한국 거래소
df_krx = fdr.StockListing("KRX")
print(df_krx.head())
df_krx.to_excel('krx.xlsx', index=False, engine='openpyxl')
# 나스닥
df_nasdaq = fdr.StockListing("NASDAQ")
print(df_nasdaq.head())
df_nasdaq.to_excel('nasdaq.xlsx', index=False, engine='openpyxl')
# S&P500
df_snp = fdr.StockListing("S&P500")
df_snp.to_excel('snp.xlsx', index=False, engine='openpyxl')
print(df_snp.head())



# AAPL = fdr.DataReader("APPL")
# AAPL['Close'].plot()
# plt.show()