# This code is written to plot the periodic function in Example 16.3 
from math import*
import matplotlib.pyplot as plt
def rectangularWave(Vm=1,wo=2*pi,n=10000):
    # Vm is the maximum voltage (amplitude) of the pulse; it is set by default to 1V
    # wo is the fundemental frequency of the pulse; it is set by default to 2pi rd/s
    # this means that T=1s
    # n is the number of harmonics; it is set by default to 10000 harmonics
    L=[]
    # L is the list that will store the value of the function at every instant
    av=(Vm/4)
    # av is the aveage Fourier Coefficient
    p=ceil((4*pi)/wo)
    #p is an integer that contains 2 periods 
    X=[]
    i=0
    while (i<p):
        X.append(i)
        i+=0.01
        # X is a list that contains the abscissas(instants)
        # making a step of 0.01 each time 
    t=0
    # begin the figure at time t=0s 
    while(t<p):
        # this range guarantees the presence of 2 periods in the figure
        # we are summing the harmonics at every instant
        s1=0
        # initializing s1 
        # s1 is the sum of the harmonics at each given instant t 
        for k in range(1,n+1):
            # k is here represents the harmonic's number, it starts at 1 and ends at n 
            # (n+1 is an upper bound, not included)
            ak=(Vm/(k*pi))*sin((k*pi)/2)
            bk=(Vm/(k*pi))*(1-cos((k*pi)/2))
            # the two Fourier Coefficients that depend on the harmonic 
            ak1=ak*cos(k*wo*t)
            bk1=bk*sin(k*wo*t)
            # multiplying the coefficients by their asscociated time-depending function
            s1=s1+ak1+bk1
        # s1 is the sum of the harmonic functions at every instant
        s=av+s1
        #s is the value of the function at each instant t
        L.append(s)
        # adding s to the list of ordinates(voltages)
        t+=0.01
        # making a step of 0.01 seconds (10ms) each time 
    plt.plot(X,L)
    # plotting the figure
    plt.xlabel("t")
    # labeling the x-axis as "t"
    plt.ylabel("v(t)")
    # labeling the y-axis as "v(t)"
rectangularWave()
#calling the function; using default parameters

    

        