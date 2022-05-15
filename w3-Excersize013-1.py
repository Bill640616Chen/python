#dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
from sys import stdin
dict = {1:'I', 5:'V', 10:'X',12:"XII", 50:'L', 100:'C', 500:'D', 1000:'M'}

r =""
for s in stdin: 
    if int(s) % 3 == 0 and 1 < int(s) < 5:
        n = int(s) // 2
    #if int(s) == 12:
        r = dict.get(int(n))
    print(type(s))
    print(r+r+r)
    break

#n = dict.get(1)
#print(n+n+n)
#list1 = list(dict)
#print(list1) #印出鍵