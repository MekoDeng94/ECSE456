import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from scipy import signal

def MACD(series):
    ewm12 = series.ewm(span=12).mean()
    ewm26 = series.ewm(span=26).mean()
    return (ewm12 - ewm26)

def RSI(series, period):
 delta = series.diff().dropna()
 u = delta * 0
 d = u.copy()
 u[delta > 0] = delta[delta > 0]
 d[delta < 0] = -delta[delta < 0]
 u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
 u = u.drop(u.index[:(period-1)])
 d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
 d = d.drop(d.index[:(period-1)])
 rs = u.ewm(com=period-1, adjust=False).mean()
 return 100 - 100 / (1 + rs)

def ROC(df, n):
    M = df.diff(n - 1)
    N = df.shift(n - 1)
    ROC = pd.Series(((M / N) * 100), name = 'ROC_' + str(n))
    return ROC

def CCI(close, high, low, n, constant):
 TP = (high + low + close) / 3
 CCI = pd.Series((TP - TP.rolling(n).mean()) / (constant * TP.rolling(n).std()), name = 'CCI_' + str(n))
 return CCI

def MassIndex(high, low):
    Range = high - low
    EX1 = Range.ewm(span = 9, min_periods = 8).mean()
    EX2 = EX1.ewm(span = 9, min_periods = 8).mean()
    Mass = EX1 / EX2
    MassIndex = pd.Series(Mass.rolling(25).sum(), name = 'Mass Index')
    return MassIndex

def STOK(close, high, low, n):
 STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
 return STOK

def STOD(close, high, low, n):
 STOK = ((close - low.rolling(n).min()) / (high.rolling(n).max() - low.rolling(n).min())) * 100
 STOD = STOK.rolling(3).mean()
 return STOD

# 5, 10 and 20 day future return
def fiveday(close):
    fiveday = ((close.shift(-5) - close) / close) * 100
    return fiveday

def tenday(close):
     tenday = ((close.shift(-10) - close) / close) * 100
     return tenday

def twentyday(close):
     twentyday = ((close.shift(-20) - close) / close) * 100
     return twentyday

df = pd.read_csv("HistoricalQuotes.csv")
df = df.iloc[::-1]
df["MACD"] = MACD(df["close"])
df["RSI"] = RSI(df["close"],14)
df["ROC"] = ROC(df["close"],12)
df["CCI"] = CCI(df["close"],df["high"],df["low"],20,0.015)
df["MassIndex"] = MassIndex(df["high"], df["low"])
df["%K"] = STOK(df["close"],df["high"],df["low"],14)
df["%D"] = STOD(df["close"],df["high"],df["low"],14)
df["5 day"] = fiveday(df["close"])
df["10 day"] = tenday(df["close"])
df["20 day"] = twentyday(df["close"])

print(df)

plt.subplot(2,1,1)
plt.plot(df["date"].tail(100),df["close"].tail(100))
plt.xticks(rotation=90)
plt.subplot(2,1,2)
plt.plot(df["date"].tail(100),df["MACD"].tail(100))
plt.xticks(rotation=90)
#df2 = df[['5 day', '10 day', '20 day']].mean()
#df2.plot(kind='bar')
plt.show()
