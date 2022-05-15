#取數字的個十百千位的數字
from sys import stdout
if __name__ == '__main__':
    x = int(input('pls input a four number:\n'))
    xx = []
    a = x / 1000
    b = x % 1000 / 100
    c = x % 100 / 10
    d = x % 10
    xx.append(a)
    xx.append(b)
    xx.append(c)
    xx.append(d)
    print (xx)

from sys import stdin
for s in range(100,1000):
    a=s/100
    b=(s%100)/10
    c=s%10
    print(a,b,c)
    break