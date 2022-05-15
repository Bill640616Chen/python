#https://www.w3schools.com/python/ref_func_frozenset.asp
#Python frozenset Function Python frozenset函數
#Returns a frozenset object
#返回 frozenset 物件。
#Freeze the list, and make it unchangeable:
#凍結清單，使其不可變：
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
#Definition and Usage 定義和用法
#The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
#frozenset（） 函數返回一個不可更改的 Frozenset 物件（類似於 set 物件，僅不可更改）。
#Syntax 語法
#frozenset(iterable)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：An iterable object, like list, set, tuple etc.
#iterable：可反覆運算物件，如清單、集合、元組等。
#Try to change the value of a frozenset item.
#嘗試更改 Frozenset 專案的值。
#This will cause an error:
#這樣會引發錯誤：
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"
print(x)
#x[1]=,把索引位置1的值改掉
#TypeError: 'frozenset' object does not support item assignment