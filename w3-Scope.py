#https://www.w3schools.com/python/python_scope.asp
#Python Scope 作用域
#A variable is only available from inside the region 
# it is created. This is called scope.
#變數僅在創建區域內可用。這稱為作用域。
print("-----------------在函數內部創建的變數只能在該函數內部使用")
#Local Scope 局部作用域
#A variable created inside a function belongs to the local 
# scope of that function, and can only be used inside that 
# function.
#在函數內部創建的變數屬於該函數的局部作用域，並且只能在該函數
# 內部使用。
#A variable created inside a function is available inside 
# that function:
#在函數內部創建的變數只能在該函數內部使用：
def myfunc():
  x = 300
  print(x)
myfunc() #300

print("---------------Function Inside Function 函數內部的函數")
#Function Inside Function 函數內部的函數
#As explained in the example above, the variable x is 
# not available outside the function, but it is available 
# for any function inside the function:
#如上例中所示，變數 x 在函數外部不可用，但對於函數內部的
# 任何函數均可用：
#The local variable can be accessed from a function within the function:
#本地的變數可以被函數內的函數訪問
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

print("-----------------------------Global Scope 全局作用域")
#Global Scope 全局作用域
#A variable created in the main body of the Python code 
# is a global variable and belongs to the global scope.
#在 Python 代碼主體中創建的變數是全局變數，屬於全局作用域。
#Global variables are available from within any scope, 
# global and local.
#全局變數在任何範圍（全局和局部）中可用。
#A variable created outside of a function is global and can be used by anyone:
#在函數外部創建的變數是全局變數，任何人都可以使用：
x = 300
def myfunc():
  print(x)
myfunc()
print(x)

print("-------------------------Naming Variables 命名變數")
#Naming Variables 命名變數
#If you operate with the same variable name inside and 
# outside of a function, Python will treat them as two 
# separate variables, one available in the global scope 
# (outside the function) and one available in the local 
# scope (inside the function):
#如果在函數內部和外部操作同名變數，Python 會將它們視為兩個
# 單獨的變數，一個在全局範圍內可用（在函數外部），而一個在
# 局部範圍內可用（在函數內部）：
#The function will print the local x, and then the code will print the global x:
#該函數將列印局部變數 x，然後代碼還會列印全局變數 x：
x = 300
def myfunc():
  x = 200
  print(x)
myfunc() #這個是調用函數()裡沒變數,所以是取函數裡的變數使用
print(x) #這裡是取函數外的變數使用

print("----------------------Global Keyword Global 關鍵字")
#Global Keyword Global 關鍵字
#If you need to create a global variable, but are stuck 
# in the local scope, you can use the global keyword.
#如果您需要創建一個全局變數，但被卡在本地作用域內，則可以使用 
# global 關鍵字。
#The global keyword makes the variable global.
#global 關鍵字使變數成為全局變數。
#If you use the global keyword, the variable belongs to the global scope:
#如果使用 global 關鍵字，則該變數屬於全局範圍：
x = 200
def myfunc():
  global x
  x = 300
myfunc() 
print(x) #300
#因為函數裡的x宣告為全域變數,所以值取代了原全域變數的值
print("-----------------------------Global Keyword 測試-1")
#Also, use the global keyword if you want to make a 
# change to a global variable inside a function.
#另外，如果要在函數內部更改全局變數，也請使用 global 關鍵字。
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x) #200
#因為函數裡的x宣告為全域變數,所以值取代了原全域變數的值
print("-----------------------------Global Keyword 測試-2")
x = 300
def myfunc():
  global x
  x = 200
  print(x)
myfunc() 
print(x)
#因為函數裡的x宣告為全域變數,所以值取代了原全域變數的值
