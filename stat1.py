#!/usr/bin/python

#calculate mean, median and mode

from array import *
import decimal
import math
import operator

def main():
    n = input("Enter how many number: ")
    no = raw_input("Enter numbers seperated by space: ")
    numArr = map(int, no.split(" "))
    actualArr = numArr
    total = 0
    mid = m1 = m2 = 0
    median = 0.0
    
    if len(numArr) != n:
        n = len(numArr)
        
    # sorting
    numArr.sort()
    
    for num in numArr:
        #print "%d" % num
        total += num       
        
    # even or odd
    if n % 2 == 0:
        m2 = n / 2
        m1 = m2 - 1
        #print m2
        #print m1
        if m1 == 0:
            m1 = 1
        median = (decimal.Decimal(numArr[m1]) + decimal.Decimal(numArr[m2])) / 2
    else:
        if n > 1:
            mid = n / 2                
        else:
            mid = 1
        median = numArr[int(mid)]
    
    #print numArr[m1]
    #print numArr[m2]
        
    previous = 0
    count = 0
    highestCount = 0
    countArr = {}
    for num in numArr:
        if previous == num:
            count += 1 
        else:
            previous = num
            count = 1
        countArr.update({num : count})
        if highestCount < count:
            highestCount = count
        
    #print(countArr)
    #print highestCount  
    
    if highestCount == 1:
        mode = numArr[0] 
    else:
        mode = max(countArr.iteritems(), key = operator.itemgetter(1))[0]
    
    #print "total %d" % total
        
    mean = decimal.Decimal(total) / decimal.Decimal(n)    
    print "Mean: %.1f" % mean
    
    print "Median: %.1f" % median
    
    print "Mode: %d" % mode
        
if __name__ == "__main__":
    main()