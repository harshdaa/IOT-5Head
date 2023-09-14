from sense_hat import SenseHat
import matplotlib.pyplot as plt
from time import sleep

sense = SenseHat()
numreadings = 1000
windowsize = 15

tmp =[]
avgtmp = []
x_axis = []

for i in range(numreadings):
    x_axis.append(i)
    
    var = sense.get_temperature()
    tmp.append(var)
    if i==0:
        var2 = sum(tmp[-windowsize:])
    else:
        var2 = sum(tmp[-windowsize:])/len(tmp[-windowsize:])
    ##print(len(tmp[-windowsize:]))
    avgtmp.append(var2)
    sleep(0.1)
    
print(tmp)
print(avgtmp)

plt.plot(x_axis, tmp)
plt.plot(x_axis, avgtmp, linestyle='dotted', color='red')


plt.show()



    