#https://www.w3schools.com/python/gloss_python_iterator_vs_iterable.asp
#Iterator vs Iterable 迭代器對比可迭代
#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#迭代器是包含可計數值數的物件。(迭代器亦稱反覆運算器)
#All these objects have a method which is used to get an iterator:iter()
#所有這些物件都有一個用於獲取反覆運算器的方法：iter()
#Return an iterator from a tuple, and print each value:
#從元組返回反覆運算器，並列印每個值：
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print('-------------分隔線------------')
#Even strings are iterable objects, and can return an iterator:
#甚至字串也是可反覆運算的對象，並且可以返回反覆運算器：
#Strings are also iterable objects, containing a sequence of characters:
#字串也是可反覆運算的物件，包含一系列字元：
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print('-------------分隔線------------')
mystr = (123,11,23,97,20,)
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
#Related Pages 相關頁面
#Python Iterator Tutorial Python 迭代器教程
#https://www.w3schools.com/python/python_iterators.asp
#Iterator 迭代器
#https://www.w3schools.com/python/gloss_python_iterators.asp
#Loop Through an Iterator 迴圈迭代器
#https://www.w3schools.com/python/gloss_python_iterator_loop.asp
#Create an Iterator 建立迭代器
#https://www.w3schools.com/python/gloss_python_iterator_create.asp
#StopIteration 停止迭代
#https://www.w3schools.com/python/gloss_python_iterator_stop.asp