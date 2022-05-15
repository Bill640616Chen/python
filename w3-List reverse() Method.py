#https://www.w3schools.com/python/ref_list_reverse.asp
#Python List reverse() Method 反轉清單順序方法
#Reverses the order of the list 反轉清單順序
#Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) #['cherry', 'banana', 'apple']
#Definition and Usage
#The reverse() method reverses the sorting order of the elements.
print(fruits.reverse()) #None
#() -> None
#Reverse *IN PLACE*

#Syntax
#list.reverse() ()裡沒參數
#Parameter Values
#No parameters

#https://www.w3schools.com/python/ref_func_reversed.asp
#Python reversed() Function 函數
#Reverse the sequence of a list, and print each item:
#反轉清單的順序，列印每個項目：
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

#Definition and Usage
#The reversed() function returns a reversed iterator object.
#reversed()函數傳回反轉的可迭代物件。
#Syntax
#reversed(sequence)(序列)
#Parameter Values
#Parameter：Description
#sequence：Required. Any iterable object任何可迭代物件
#reversed()
#(class) reversed
#Return a reverse iterator over the values of the given sequence.
#傳回反轉迭代器超過給定序列的值。

#https://www.w3schools.com/python/ref_func_iter.asp
#Python iter() Function 函數
#iter() 函数用来生成迭代器
#Create an iterator object, and print the items:
#製造一個可迭代器物件,並列印項目
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
#next() 返回迭代器的下一个项目。
#next() 函数要和生成迭代器的 iter() 函数一起使用。
#apple
#banana
#cherry
#iter(iterable) -> iterator iter(callable, sentinel) -> iterator
#Get an iterator from an object. In the first form, the argument
#  must supply its own iterator, or be a sequence. In the second
#  form, the callable is called until it returns the sentinel.
#從物件獲取可迭代器。在第一種形式中，參數必須提供自己的可迭代器，或者是
# 一個序列。在第二種形式中，可調用被調用，直到它返回哨兵。
#Definition and Usage
#The iter() function returns an iterator object.

#Syntax
#iter(object, sentinel)
#参数
#object -- 支持迭代的集合对象。
#sentinel -- 如果传递了第二个参数，则参数 object 必须是一个可调用的对象
# （如，函数），此时，iter 创建了一个迭代器对象，每次调用这个迭代器对象
# 的__next__()方法时，都会调用 object。
#Parameter Values
#Parameter：Description
#object：Required. An iterable object
#sentinel：Optional. If the object is a callable object the 
# iteration will stop when the returned value is the same as 
# the sentinel
#如果對像是可調用物件，則當返回值與哨兵相同時，反覆運算將停止
