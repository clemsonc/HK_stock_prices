import pandas_datareader.data as web
import datetime

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 9, 26)

print (web.DataReader('AAPL', 'yahoo', start, end))
