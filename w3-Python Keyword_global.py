#https://www.w3schools.com/python/ref_keyword_global.asp
#Python Keyword global 關鍵字 global
#To declare a global variable
#聲明全域變數。
#Declare a global variable inside a function, and use it outside the function:
#在函數內部聲明一個全域變數，並在函數外部使用它：
#create a function:
#建立函數：
def myfunction():
  global x
  x = "hello"
#execute the function:
#執行函數：
myfunction()
#x should now be global, and accessible in the global scope.
#x 現在有關是全域變數，可以進行全域訪問。
print(x)
#Definition and Usage 定義和用法
#The global keyword is used to create global variables from a no-global scope, e.g. inside a function.
#global 關鍵字用於從非全域範圍創建全域變數，例如在函數內部。
