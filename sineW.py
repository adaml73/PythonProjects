maxX = input("Enter x coordinate of Max value:")
maxY = input("Enter y coordinate of Max value:")
minX = input("Enter x coordinate of Min value:")
minY = input("Enter y coordiante of min value:")
period = 1
BValue = 0
CValue = 0
amp = 0
vertD = 0
pComplete = False

import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import figure, show
from numpy import arange, sin, pi, linspace
import Tkinter
import tkMessageBox
#{ToDo __ entering individual x, y values is tedious, modify->
#inputs to accepts tuples, possibly of form "(x, y)"
#Import/implement method of simplyfing B value. euclid gcd algo?
# ^^ only neccesarry if radian mode is added at later date
#consider imbedding within caclBValue function.
#implement abs() (absolute value) function in respective functions
#check/correct variables to comply w/ camelCase, currently sloopy
#later implement ability to perform operations from a more complete
#dataset, utilize dict, min(), max() ect..
#END ToDo}
#7/14/15--corrected error w/vertD function,
#plt.ylabel("Tempurature (F)")
#plt.plot()

def calc_amp(maxY, minY, amp):
    '''
    Subtracts Greatest and least greatest Y values, then multiplies result by
    (0.5), to find amplitiude.
    '''
    amp = 0.5 * (maxY - minY)
    print "A = " + str(amp)
    return amp

def calc_Period(maxX, minX, period):
    '''
    calculates Period, substracts Max and Min x values,
    then multiplies result by 2 to obtain Period
    '''
    period = 2 * (maxX - minX)
    print "P = " + str(period)
    pComplete = True
    return period

def calc_BValue(period, BValue):
    '''
    description
    '''
    BValue = 2 * pi / period
    print "B = " + str(BValue)
    return round(BValue, 3)

def calc_VertD(maxY, minY, vertD):
    '''
    Calculates Vertical shift D, finds sum of max, min y values
    then divides result by two, resulting in vertical shift.
    '''
    vertD = (maxY + minY) / 2
    print "D = " + str(vertD)
    return vertD

def calc_CValue(minX, CValue, BValue):
    '''
    description

    '''
    #print period
    CValue = (minX + (0.25 * period)) * BValue
    print "C = " + str(CValue)
    return CValue


#call functions
#implemet conditionals for A>0, etc
amp = calc_amp(maxY, minY, amp)
period = calc_Period(maxX, minX, period)
BValue = calc_BValue(period, BValue)
vertD = calc_VertD(maxY, minY, vertD)

#if pComplete == True:

CValue = calc_CValue(minX, CValue, BValue)
#insert conditional for case CValue
if CValue > 0:
    print "sin function y = %d[%2.3fx-(%2.3f)]+%d" % (amp, BValue, CValue, vertD)
    #print "experiment {0:.3f}" .format(BValue)

elif CValue < 0:
    print "sin Function y = %d[%2.3fx+(%2.3f)]+%d" % (amp, BValue, CValue, vertD)


# plot function
UInput = input("graph found function? enter 1 for yes or 2 for no:")

if UInput == 1:
    plt.ylim = (minY, maxY)
    #insert conditional for negative values
    x = linspace(0, (4 * maxX),)
    y = amp * np.sin((BValue * x) - (CValue)) + vertD
    plt.plot(x, y)
    plt.show()

elif UInput == 2:
    pass
