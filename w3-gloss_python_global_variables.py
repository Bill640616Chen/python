#https://www.w3schools.com/python/gloss_python_global_variables.asp
#Python global_variables
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#在函數之外創建的變數（如上文所有示例中所示）稱為全球變數。
#Global variables can be used by everyone, both inside of functions and outside.
#全球變數可用於功能內外的每個人。
#Create a variable outside of a function, and use it inside the function
#在函數之外創建一個變數，並在函數內使用它
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
#如果在函數內創建具有相同名稱的變數，此變數將是本地的，並且只能在函數內使用。同名的全球變數將保持原樣，具有全球性和原始值。
#Create a variable inside a function, with the same name as the global variable
print('-------------分隔線------------')
#在函數內創建一個變數，與全球變數同名
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
#The global Keyword 全球關鍵字
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#通常，當您在函數內創建變數時，該變數是本地的，並且只能在該函數內使用。
#To create a global variable inside a function, you can use the global keyword.
#要在函數內創建全球變數，您可以使用關鍵字。global
#If you use the global keyword, the variable belongs to the global scope:
print('-------------分隔線------------')
#如果您使用關鍵字，該變數屬於全球範圍：global
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#Also, use the global keyword if you want to change a global variable inside a function.
#此外，如果您想要更改函數內的全球變數，請使用關鍵字。global
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
print('-------------分隔線------------')
#要更改函數內的全球變數值，請使用關鍵字引用該變數：global
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
#Related Pages 相關頁面
#Python Variables Tutorial Python 變數教程
#https://www.w3schools.com/python/python_variables.asp
#Creating Variables 創建變數
#https://www.w3schools.com/python/gloss_python_creating_variables.asp
#Variable Names 可變名稱
#https://www.w3schools.com/python/gloss_python_variable_names.asp
#Assign Value to Multiple Variables 將值分配給多個變數
#https://www.w3schools.com/python/gloss_python_assign_value_to_multiple_variables.asp
#Output Variables 輸出變數
#https://www.w3schools.com/python/gloss_python_variable_output.asp
#String Concatenation 字串串聯
#https://www.w3schools.com/python/gloss_python_string_concatenation.asp
