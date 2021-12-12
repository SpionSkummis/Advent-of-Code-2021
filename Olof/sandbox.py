# numpy
import numpy as np
a = np.array([[1,2,3], [4,5,6]])
print(a)

rr = []
for a in list(open('Olof\day03_input_test.txt','r').read().splitlines()):
    rr.append(list(a))
b = np.array(rr)
print(b)

#alla rader, kolumn 1
print(b[:, 1])