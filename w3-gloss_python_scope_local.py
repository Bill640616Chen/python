#https://www.w3schools.com/python/gloss_python_local_scope.asp
#Python Local Scope 本地範圍
#A variable is only available from inside the region it is created. This is called scope.
#變數只能從創建它的區域內部獲得。這稱為作用域。
#Local Scope 本地範圍
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
#在函數內創建的變數屬於該函數的局部作用域，並且只能在該函數內使用。
#A variable created inside a function is available inside that function:
#在函數內建立的變數在該函數中可用：
def myfunc():
  x = 300
  print(x)
myfunc()
print('-------------分隔線------------')
#Function Inside Function 功能內部 功能
#As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
#如上面的範例中所述，該變數在函數外部不可用，但它可用於函數內的任何函數：x
#The local variable can be accessed from a function within the function:
#可以從函數中的函數存取局部變數：
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
#若myinnerfunc()縮排,則外部調不到內部的函數

