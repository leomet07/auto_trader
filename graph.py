#hmath sources
#https://www.dummies.com/education/math/statistics/how-to-calculate-a-regression-line/
#https://www.dummies.com/education/math/statistics/how-to-calculate-a-correlation/

#get plot ready before to reduce end time
from matplotlib import pyplot as plt
import math
import numpy as np
from get_stock import get_price
import time
stock_to_track = "AAPL"
past_prices = []
a = []
'''
#for debug
past_prices  = [222,223,223.5,225,225,227]
#past_prices = past_prices[::-1]

for i in range(len(past_prices)):
    a.append(i)
'''
#FOR PRODUCTIOn

current_stock = 0
for _ in range(8):
    
    price = float(get_price(stock_to_track))
    print(price)
    past_prices.append(price)
    a.append(current_stock)
    current_stock += 1
    time.sleep(1)


#getting the big 5
y_avg =   sum(past_prices)/len(past_prices)
x_avg = sum(a)/len(a)
print("X avg ", x_avg, " Y Avg ", y_avg)
#all diffs

x_dev = 0
for i in a:
    print((i-x_avg)**2)
    x_dev += (i-x_avg)**2
y_dev = 0
for i in past_prices:
    print((i-y_avg)**2)
    y_dev += (i-y_avg)**2
    
print("X dev " ,x_dev,"Y dev ",y_dev)




#making the correlation
#by default no change unless calculated
m = 0
try:
    sum_to_use = 0
    for i in range(len(a)):
        sum_to_use += (a[i] - x_avg)* (past_prices[i] - y_avg)
        print((a[i] - x_avg),"*", (past_prices[i] - y_avg))

    print("Sum to use" + str(sum_to_use))
    print("has to be neg",math.sqrt(x_dev * y_dev  ))
    divided = sum_to_use / math.sqrt((x_dev * y_dev  ))

    correlation = divided
    print("Correlation" + str(correlation))

    #finding the slope of the line


    m = correlation * (y_dev/x_dev)
    print("M (SLOPE) " + str(m))
except ZeroDivisionError:
    print("No change")
    

#getting the y intercept
b = y_avg - m*x_avg

print("B (Y_intercept)" + str(b))


#regenerate the x's for a graph
new_xs = a
new_ys = []
for i in range(len(new_xs)):
    #i is the x in this case
    y = (m*i)+b
    new_ys.append(y)
fig= plt.figure()
fig.title = stock_to_track + ' history'
axes=fig.add_subplot(111)

axes.plot(a,past_prices,new_xs,new_ys)


plt.show()