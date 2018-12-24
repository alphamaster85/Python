import sys
import math

x = float(sys.argv[1])
u = float(sys.argv[2])
d = float(sys.argv[3])

print ((1/(d*(math.sqrt(2*math.pi))))*math.exp(-(((x-u)**2)/(2*d**2))))