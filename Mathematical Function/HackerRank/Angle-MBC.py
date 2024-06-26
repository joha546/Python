# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

ab=int(input())
bc=int(input())

# calculating hypotenuse of the triangle
ac=hypot(ab,bc)
m=ac/2
theta=atan(ab/bc)
in_degrees=degrees(theta)
print(f"{round(in_degrees)}\u00b0")

