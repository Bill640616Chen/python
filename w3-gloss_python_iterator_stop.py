#https://www.w3schools.com/python/gloss_python_iterator_stop.asp
#Stop Iteration 停止迭代
#To prevent the iteration to go on forever, we can use the StopIteration statement.
#為了防止反覆運算永遠持續下去，我們可以使用該語句。StopIteration
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
#在方法中，如果反覆運算完成指定次數，我們可以添加終止條件以提出錯誤：__next__()
#Stop after 20 iterations:
#20 次反覆運算後停止：
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
#Related Pages 相關頁面
#Python Iterator Tutorial Python 迭代器教程
#https://www.w3schools.com/python/python_iterators.asp
#Iterator 迭代器
#https://www.w3schools.com/python/gloss_python_iterators.asp
#Iterator vs Iterable 迭代器對比可迭代
#https://www.w3schools.com/python/gloss_python_iterator_vs_iterable.asp
#Loop Through an Iterator 迴圈迭代器
#https://www.w3schools.com/python/gloss_python_iterator_loop.asp
#Create an Iterator 建立迭代器
#https://www.w3schools.com/python/gloss_python_iterator_create.asp
