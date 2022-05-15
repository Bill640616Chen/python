#https://www.w3schools.com/python/ref_func_callable.asp
#Python callable() Function Python callable()函數
#Returns True if the specified object is callable, otherwise False
#如果指定的對像是可調用的，則返回 True，否則返回 False。
#Check if a function is callable:
#檢查函數是否可呼叫：
def x():
  a = 5
print(callable(x))
#Definition and Usage 定義和用法
#The callable() function returns True if the specified object is callable, otherwise it returns False.
#如果指定的對像是可調用的，則 callable（） 函數返回 True，否則返回 False。
#Syntax 語法
#callable(object)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：The object you want to test if it is callable or not.
#object：需要測試是否可調用的物件。
#A normal variable is not callable:
#一般變數是不可呼叫的：
x = 5
print(callable(x))