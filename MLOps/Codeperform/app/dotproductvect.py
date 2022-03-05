import array
import numpy

# 8 bytes size int
a = array.array('q')
for i in range(1000000):
    a.append(i);
  
b = array.array('q')
for i in range(1000000, 2000000):
    b.append(i)

dot = numpy.dot(a,b);

print("dot_product = "+ str(dot));