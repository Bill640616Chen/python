#https://www.w3schools.com/python/ref_func_next.asp
#Python next() Function Python next()函數
#Returns the next item in an iterable
#返回可反覆運算物件中的下一項。
#Create an iterator, and print the items one by one:
#創建一個反覆運算器，並逐一列印專案：
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)
#Definition and Usage 定義和用法
#The next() function returns the next item in an iterator.
#next（） 函數傳回反覆運算器中的下一項。
#You can add a default return value, to return if the iterable has reached to its end.
#您可以添加預設的返回值，以在反覆運算結束時返回。
#Syntax 語法
#next(iterable, default)
#Parameter參數：Values值
#Parameter參數：Description描述
#iterable：Required. An iterable object.
#iterable：必需。 可反覆運算物件。
#default：Optional. An default value to return if the iterable has reached to its end.
#default：可選。 在反覆運算結束時返回的預設值。
#Return a default value when the iterable has reached to its end:
print('-------------分隔線------------')
#當反覆運算結束時傳回預設值：
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)
x = next(mylist, "orange")
print(x)