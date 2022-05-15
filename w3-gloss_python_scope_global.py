#https://www.w3schools.com/python/gloss_python_global_scope.asp
#Python Global Scope 全域範圍
#A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#在 Python 代碼主體中創建的變數是全域變數，屬於全域範圍。
#Global variables are available from within any scope, global and local.
#全域變數可在任何範圍內使用，包括全域變數和局部變數。
#A variable created outside of a function is global and can be used by anyone:
#在函數外部創建的變數是全域變數，任何人都可以使用：
x = 300
def myfunc():
  print(x)
myfunc()
print(x)
print('-------------分隔線------------')
#Naming Variables 命名變數
#If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
#如果在函數內部和外部使用相同的變數名稱進行操作，Python 會將它們視為兩個單獨的變數，一個在全域作用域（函數外部）可用，另一個在局部作用域（函數內）可用：
#The function will print the local x, and then the code will print the global x:
#該函數將列印本地，然後代碼將列印全域：xx
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)
#Related Pages 相關頁面
#Local Scope 本地範圍
#https://www.w3schools.com/python/gloss_python_local_scope.asp
#Global Keyword 全域關鍵字
#https://www.w3schools.com/python/gloss_python_global_keyword.asp