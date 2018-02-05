import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd



# Brent Crude Oil Historical OHLC
BrentHist = pd.read_csv('Brent Oil Futures Historical Data.csv',
                         header = 0)
BrentHist = BrentHist.reindex(index=BrentHist.index[::-1])
BrentHist.fillna(method = "ffill")

# WTI Crude Oil Historical OHLC
WTIHist = pd.read_csv('Crude Oil WTI Futures Historical Data.csv',
                         header = 0)
WTIHist = WTIHist.reindex(index=WTIHist.index[::-1])
WTIHist.fillna(method = "ffill")

CrudeMergeHist = WTIHist.merge(BrentHist, on = "Date")
CrudeMergeHist.columns = ['Date', 'WTI_Price', 'WTI_Open', 'WTI_High', 'WTI_Low', 'WTI_Vol', 'WTI_Change',
                          'Brent_Price', 'Brent_Open', 'Brent_High', 'Brent_Low', 'Brent_Vol', 'Brent_Change']
CrudeMergeHist.fillna(method = "ffill")

# # Convert UNIX timestamp to standard time
# BrentHist.Date = np.asarray(BrentHist.Date, dtype='datetime64[s]')
# BrentHist.Date = pd.to_datetime(BrentHist.Date)

BrentHistDF = CrudeMergeHist[["Date", "Brent_Price"]]
WTIHistDF = CrudeMergeHist[["Date", "WTI_Price"]]

BrentTS = pd.Series(np.asarray(BrentHistDF.Brent_Price), index = BrentHistDF.Date)
CrudeTS = pd.Series(np.asarray(WTIHistDF.WTI_Price), index = WTIHistDF.Date)
plt.clf() # clear plot
BrentTS.plot()
CrudeTS.plot()
plt.pause(1)



# Plot Spread Differences

CrudeMergeHist["WTI_Brent_Spread"] = (CrudeMergeHist.WTI_Price - CrudeMergeHist.Brent_Price)/ CrudeMergeHist.Brent_Price
SpreadTS = pd.Series(np.asarray(CrudeMergeHist.WTI_Brent_Spread), index = CrudeMergeHist.Date)
SpreadTS.plot()
