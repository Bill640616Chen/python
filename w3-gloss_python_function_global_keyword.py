#https://www.w3schools.com/python/gloss_python_global_keyword.asp
#Global Keyword 全域關鍵字
#If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#如果需要創建全域變數，但卡在局部作用域中，則可以使用關鍵字。global
#The global keyword makes the variable global.
#關鍵字使變數成為全域變數。global
#If you use the global keyword, the variable belongs to the global scope:
#如果使用關鍵字，則該變數屬於全域範圍：global
def myfunc():
  global x
  x = 300
myfunc()
print(x)
print('-------------分隔線------------')
#Also, use the global keyword if you want to make a change to a global variable inside a function.
#此外，如果要對函數內的全域變數進行更改，請使用關鍵字。global
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
#要更改函數內全域變數的值，請使用關鍵字引用該變數：global
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)
x = 300
print('-------------分隔線------------')
def myfunc():
  global x
  x = 200
print(x)
myfunc()
print('-------------分隔線------------')
def myfunc():
  global x
  x = 200
  print(x)
myfunc()
#Related Pages 相關頁面
#Local Scope 本地範圍
#https://www.w3schools.com/python/gloss_python_local_scope.asp
#Global Scope 全球範圍
#https://www.w3schools.com/python/gloss_python_global_scope.asp