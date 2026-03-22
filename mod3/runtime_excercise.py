# - Big-O notation
# - Helps to measure a code's speed
# - magnitude: units to measure code's speed
# - Think O(n) when you see forloop

1.

a = 1
b = 2
print(a+b)
O(1)

2.

n = 10
for i in range(n):
    print(i)
O(n)

3.

for i in range(5):
    print(i)

for j in range(5):
    print(j)

O(n)    

4.

for i in range(5):
    for j in range(5):
        print(i+j)

5.

for i in range(5):
    for j in range(5):
        print(i+j)
    for x in range(5):
        print(i+x)
6.

a = 0
i = N
while (i > 0):
  a += i
  i //= 2