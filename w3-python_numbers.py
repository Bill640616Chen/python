#https://www.w3schools.com/python/python_numbers.asp
#Python 號碼
#Python 中有三種數字類型：
int
float
complex
#當您向它們配置值時，會建立數位型態的變數：
x = 1    # int
y = 2.8  # float
z = 1j   # complex ,有j是虛部
print(type(x))
print(type(y))
print(type(z))
#Int
#Int 或整數是一個完整數位，正數或負數，無小數，長度無限。
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#浮
#浮動，或「浮動點號」是一個數位，正數或負數，包含一個或多個小數。
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
#浮動也可以是帶有"e"的科學數位，以指示10的力量。
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
#複雜(數)
#複雜的數位以「j」作為假想部分：
x = 3+5j
print (x.real)#取實部3.0
print (x.imag)#取虛部5.0
print(x)#(3+5j)
y = 5j
z = -5j
print (z.imag) #-5.0
print(type(x))
print(type(y))
print(type(z))
c = -20.3j-5.3j#用-號寫也沒關係
print (c.real)#取實部
print (c.imag)#取虛部
#-0.0,有j的都是虛部啦
#-25.6
#實跟實,虛跟虛,各獨自加減乘除
#類型轉換
#您可以根據方法從一種類型轉換為另一種類型：int()float()complex()
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x) 
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a) #1.0
print(b) #2
print(c) #(1+0j)

print(type(a))
print(type(b))
print(type(c))

#隨機編號
#Python 沒有製作隨機數位的功能，但 Python 有一個內置模組，
#稱為可用於製作隨機數位：random()random
import random #模組只能用import
print(random.randrange(1, 100, 12))#數字隨機出
#(function) randrange: (start: int, stop: int | None = ..., step: int = ...) -> int
#randrange (start, stop ,step),step為0或負數都會出錯