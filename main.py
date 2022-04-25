import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

def yrangeCalculate(c_number):

    steps=0

    while(c_number!=1):
        if (c_number % 2 == 0):
            c_number = c_number/2

        else:
            c_number = c_number*3+1

        steps+=1

    return steps
y = np.array([])

for number in range(1,10001):

    y = np.append(y,yrangeCalculate(number))

xrange = np.arange(1,len(y)+1)

plt.plot(y,xrange,'.',c="m",ms=3.2)
plt.xlabel("Steps")
plt.ylabel("Value")
plt.title("Collatz Conjecture Analize of first "+ str(number) +" number:")
plt.show()
