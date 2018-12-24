import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])

print ((math.sqrt(a*b))/((math.e**a)*b)+(a*math.e**((2*a)/b)))