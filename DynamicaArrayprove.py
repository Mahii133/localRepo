import sys

L = []
for i in range(100):
    print(i,sys.getsizeof(L))
    L.append(i)