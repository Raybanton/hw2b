from numpy import loadtxt,log
from math import exp
values = loadtxt("values.txt",float)
geometric = exp(sum(log(values))/len(values))
print(geometric)
