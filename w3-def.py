def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print(gcd(20, 30)) # 顯示 10
print('-----------------------------------')
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

print(gcd(20, 30))         # 顯示 10
print(type(gcd))           # 顯示 <class 'function'>

gcd2 = gcd
print(gcd2(20, 30))        # 顯示 10
print(id(gcd), id(gcd2))   # 兩個顯示的數字相同
print('-----------------------------------')
def sum(a, b, c = 0):
    return a + b + c

print(sum(10, 20, 30))   # 顯示 60
print(sum(10, 20))       # 顯示 30
print('-----------------------------------')
def sum(a, b, c = 0):
    return a + b + c

print(sum(c = 30, a = 10, b = 20))  # 顯示 60
print('-----------------------------------')
def appendTo(element, arr = []):
     arr.append(element)
     return arr

print(appendTo(10, [1, 2, 3]))
#[1, 2, 3, 10]
print(appendTo(20, [4, 5, 6]))
#[4, 5, 6, 20]
print(appendTo(0))
#[0]
print(appendTo(10))
#[0, 10]
print(appendTo(20))
#[0, 10, 20]
print(appendTo(30))
#[0, 10, 20, 30]
print(appendTo(40))
#[0, 10, 20, 30, 40]
print('----------------------------------')
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(sum(1, 2))        # 顯示 3
print(sum(1, 2, 3))     # 顯示 6
print(sum(1, 2, 3, 4))  # 顯示 10
