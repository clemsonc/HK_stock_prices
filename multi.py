import pandas as pd
import pandas_datareader.data as web
from datetime import date, timedelta

with open("looking.txt", "r") as ins:
    array = []
    for line in ins:
        newline = line.replace("\n", "")
        array.append(newline)

stock = web.get_quote_yahoo(array)
print(stock)
stock.to_excel(r'today.xlsx')


# ls_key = 'Adj Close'
# #ls_key = 'Open'
# end = date.today()
# start = end - timedelta(days=5)
#
# f = web.DataReader(array, 'yahoo', start, end)
#
# cleanData = f.ix[ls_key]
# dataFrame = pd.DataFrame(cleanData)
#
# print (dataFrame[:4])
