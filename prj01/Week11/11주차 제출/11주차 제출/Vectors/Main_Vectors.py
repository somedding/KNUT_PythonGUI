# Vector test code

from Vector import *

v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)
v4 = Vector(5, 7)
v5 = Vector(6, 9)

# 나누기 추가, v4, v5 추가

print(v1 == v2) # False
print(v1 == v3) # True
print(abs(v1))  # 5
print(abs(v2))  # 2.8284...
print(v1 < v2)  # False
print(v1 > v2)  # True
print() # Spacing

# These lines print the vectors (calls the __str__() method)
print('Vector 1:', v1) # 3, 4
print('Vector 2:', v2) # 2, 2
print('Vector 1 + Vector 2:', v1 + v2)  # 5, 6
print('Vector 1 - Vector 2:', v1 - v2)  # 1, 2
print('Vector 1 times Vector 2:', v1 * v2)  # 6, 8
print('Vector 1 times 5:', v1 * 5)  # 15, 20
print('Vector 4 times 6:', v4 * 6)
print('Vector 5 times 3:', v5 * 3)
