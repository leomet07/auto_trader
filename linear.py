from matplotlib import pyplot as plt
import math
def linear(a,past_prices,plot = True):
    #getting the big 5
    y_avg =   sum(past_prices)/len(past_prices)
    x_avg = sum(a)/len(a)
    #all diffs

    x_dev = 0
    for i in a:
        
        x_dev += (i-x_avg)**2
    y_dev = 0
    for i in past_prices:
        
        y_dev += (i-y_avg)**2
        
    #making the correlation
    #by default no change unless calculated
    m = 0
    try:
        sum_to_use = 0
        for i in range(len(a)):
            sum_to_use += (a[i] - x_avg)* (past_prices[i] - y_avg)
        #correlation of x and y
        correlation = sum_to_use / math.sqrt((x_dev * y_dev  ))
        #finding the slope of the line
        m = correlation * (y_dev/x_dev)
        print("M (SLOPE) " + str(m))
    except ZeroDivisionError:
        print("Aboluley zero change")
        
    
    if m > 0:
        print("Positove trend")
    elif m < 0:
        print("Negative trend")
    else:
        print("No change")
    #getting the y intercept
    b = y_avg - m*x_avg
    #regenerate the x's for a graph
    new_xs = a
    new_ys = []
    for i in range(len(new_xs)):
        #i is the x in this case
        y = (m*i)+b
        new_ys.append(y)
    
    if plot:
        fig= plt.figure()
        axes=fig.add_subplot(111)

        axes.plot(a,past_prices,new_xs,new_ys)
        plt.show()
    return m,b

