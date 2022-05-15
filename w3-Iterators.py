#https://www.w3schools.com/python/python_inheritance.asp
#Python Iterators 迭代器
#An iterator is an object that contains a countable number
#  of values.
#迭代器是一種物件，該物件包含值的可計數數字。
#An iterator is an object that can be iterated upon, meaning
#  that you can traverse through all the values.
#迭代器是可迭代的對象，這意味著您可以遍歷所有值。
#Technically, in Python, an iterator is an object which 
# implements the iterator protocol, which consist of the 
# methods __iter__() and __next__().
#從技術上講，在 Python 中，迭代器是實現迭代器協議的物件，
# 它包含方法 __iter__() 和 __next__()。

print("--------------------------------迭代器 VS 可迭代物件")
#Iterator vs Iterable 迭代器 VS 可迭代物件
#Lists, tuples, dictionaries, and sets are all iterable 
# objects. They are iterable containers which you can get 
# an iterator from.
#Lists、tuples、字典和集合都是可迭代的物件。它們是可迭代的容器，
# 您可以從中獲取迭代器（Iterator）。
#All these objects have a iter() method which is used to 
# get an iterator:
#所有這些物件都有用於獲取迭代器的 iter() 方法：
#Return an iterator from a tuple, and print each value:
#從tuple傳回一個迭代器，並列印每個值：
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) #apple
print(next(myit)) #banana
print(next(myit)) #cherry
#print(next(myit)),超出迭代器的個數,所以StopIteration
print("--------------------------------next方法的解釋與範例")
#next:
#Return the next item from the iterator. If default is 
# given and the iterator is exhausted, it is returned 
# instead of raising StopIteration.
#從迭代器傳回下一個項目。如果預設值和迭代已用盡，則返回該預設值，
# 而不是用來提高停止迭代器的輸出。
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循環:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循環
        break
print("-----------連字元串都是可迭代的物件，並且可以返回迭代器")
#Even strings are iterable objects, and can return
# an iterator:
#甚至連字元串都是可迭代的物件，並且可以返回迭代器：
#Strings are also iterable objects, containing a sequence of characters:
#字符串也是可迭代的物件，包含一系列字符：
mystr = "banana"
myit = iter(mystr)
print(next(myit)) #b
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
print(next(myit)) #n
print(next(myit)) #a
#next()從迭代器傳回下一個項目,迭代器是myit
#mystr = "banana"是可迭代物品

print("----------Looping Through an Iterator 迴圈一個迭代器")
#Looping Through an Iterator 迴圈一個迭代器
#We can also use a for loop to iterate through an iterable 
# object:
#我們也可以使用 for 循環遍歷可迭代物件：
#Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
#mytuple = ("apple", "banana", "cherry")可迭代物件
#Iterate the characters of a string:
mystr = "banana"
for x in mystr:
  print(x)
#The for loop actually creates an iterator object and 
# executes the next() method for each loop.
#for 循環實際上創建了一個迭代器物件，並為每個循環執行 next() 方法。

print("-----------------------Create an Iterator 創建迭代器")
#Create an Iterator 創建迭代器
#To create an object/class as an iterator you have to 
# implement the methods __iter__() and __next__() 
# to your object.
#要把物件/類創建為迭代器，必須為物件實現 
# __iter__() 和 __next__() 方法。
#As you have learned in the Python Classes/Objects chapter, 
# all classes have a function called __init__(), 
# which allows you to do some initializing when the object 
# is being created.
#正如您在 Python 類/物件一章中學到的，所有類都有名為 
# __init__() 的函數，它允許您在創建物件時進行一些初始化。
#The __iter__() method acts similar, you can do operations
# (initializing etc.), but must always return the iterator 
# object itself.
#__iter__() 方法的作用相似，您可以執行操作（初始化等），
# 但必須始終返回迭代器對象本身。
#The __next__() method also allows you to do operations, 
# and must return the next item in the sequence.
#__next__() 方法也允許您執行操作，並且必須返回序列中的下一個項目。
#Create an iterator that returns numbers, starting with 1, 
# and each sequence will increase by one 
# (returning 1,2,3,4,5 etc.):
#創建一個返回數字的迭代器，從 1 開始，每個序列將增加 1
# （返回 1、2、3、4、5 等）：
class MyNumbers:
  def __iter__(a): 
#__iter__初始化迭代器(a代表類),也是創建迭代器
    a.a = 1 #類.變數=1
    return a #傳回類
  def __next__(a): #傳回(a代表類)的值
    x = a.a #變數 = 類.變數
    a.a += 1 #類.變數 += 1
    return x #傳回變數
myclass = MyNumbers() #myclass把MyNumbers()實體化
myiter = iter(myclass) 
#myiter(迭代器) = iter((myclass)獲取迭代器的方法
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#這樣寫也可以,因為a的位置不同,有的a是物件(或說代表類),有的a是變數
#為什麼只有1,2,3,4,5,因為只有5個next()只傳回迭代器5個值

print("----------------------StopIteration 停止迭代器的輸出")
#StopIteration 停止迭代器的輸出 (Iteration反覆運算)
#The example above would continue forever if you had enough
#  next() statements, or if it was used in a for loop.
#如果你有足夠的 next() 語句，或者在 for 循環中使用，則上面的例子
# 將永遠進行下去。
#To prevent the iteration to go on forever, we can use the 
# StopIteration statement.
#為了防止迭代永遠進行，我們可以使用 StopIteration 語句。
#In the __next__() method, we can add a terminating 
# condition to raise an error if the iteration is done a 
# specified number of times:
#在 __next__() 方法中，如果迭代完成指定的次數，我們可以添加
# 一個終止條件來引發錯誤：
#Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)


