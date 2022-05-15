#https://www.w3schools.com/python/ref_keyword_del.asp
#Python Keyword del 關鍵字 del
#To delete an object
#刪除物件。
#Delete an object:
#刪除物件：
'''
class MyClass:
  name = "John"
del MyClass
print(MyClass)
'''
#NameError: name 'MyClass' is not defined
#Definition and Usage 定義和用法
#The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
#del 用於刪除物件。 在 Python，一切都是物件，因此 del 關鍵字可用於刪除變數、清單或清單片段等。
#Delete a variable:
print('-------------分隔線------------')
#刪除變數：
'''
x = "hello"
del x
print(x)
'''
#NameError: name 'x' is not defined
#Delete the first item in a list:
print('-------------分隔線------------')
#移除清單中的首個項目：
x = ["apple", "banana", "cherry"]
del x[0]
print(x)
