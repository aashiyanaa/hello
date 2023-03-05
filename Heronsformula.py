# write a function in python to calculate the area of the triangle using herone's formula
import math
a,b,c= map(int,input.split)
s = a+b+c/2
area = math.sqrt( s*(s-a)*(s-b)*(s-c))
if s-a>0 and s-b>0 and s-c>0:
    print(area)

