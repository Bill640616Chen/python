#https://www.w3schools.com/python/gloss_python_iterator_create.asp
#Create Iterator 建立迭代
#To create an object/class as an iterator you have to implement the methods and to your object.__iter__() __next__()
#要創建物件/類作為迭代器，您必須實現方法和物件。__iter__() __next__()
#As you have learned in the Python Classes/Objects chapter, all classes have a function called , which allows you do some initializing when the object is being created.__init__()
#正如您在Python 類/物件章節中學到的，所有類都有一個稱為"功能"的功能，它允許您在創建物件時進行一些初始化。__init__()
#The method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.__iter__()
#該方法的作用相似，您可以執行操作（初始化等），但必須始終返回傳回物件本身。__iter__()
#The method also allows you to do operations, and must return the next item in the sequence.__next__()
#該方法還允許您執行操作，並且必須按順序返回下一個專案。__next__()
#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
#創建一個返回數位的傳回器，從 1 開始，每個序列將增加一個（返回 1，2，3，4，5 等）：
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
#myiter = iter(MyNumbers())
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#Related Pages 相關頁面
#Python Iterator Tutorial Python 迭代器教程
#https://www.w3schools.com/python/python_iterators.asp
#Iterator 迭代器
#https://www.w3schools.com/python/gloss_python_iterators.asp
#Iterator vs Iterable 迭代器對比可迭代
#https://www.w3schools.com/python/gloss_python_iterator_vs_iterable.asp
#Loop Through an Iterator 迴圈迭代器
#https://www.w3schools.com/python/gloss_python_iterator_loop.asp
#StopIteration 停止迭代
#https://www.w3schools.com/python/gloss_python_iterator_stop.asp