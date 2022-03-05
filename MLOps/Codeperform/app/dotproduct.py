import array

# 8 bytes size int
a = array.array('q')
for i in range(1000000):
    a.append(i);
  
b = array.array('q')
for i in range(1000000, 2000000):
    b.append(i)

dot = 0.0;

for i in range(len(a)):
      dot += a[i] * b[i]

print("dot_product = "+ str(dot));