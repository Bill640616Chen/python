#https://www.w3schools.com/python/gloss_python_function_arguments.asp
#Function Arguments 調用函數
#Information can be passed into functions as arguments.
#信息可以傳遞到作為參數的函數中。
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#參數在功能名稱后、括弧內指定。您可以隨需要添加盡可能多的參數，只需用逗號將其分開即可。
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
#下列示例具有一個參數（fname）的函數。當函數調用時，我們傳遞一個名字，該名稱在函數內用於列印全名：
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Arguments are often shortened to args in Python documentations.
#在Python 文件中，參數通常被縮短為args。
#Parameters or Arguments? 參數還是參數？
#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#參數和參數的術語可用於同一件事：傳遞到函數中的資訊。
#From a function's perspective:
#從函數的角度來看：
#A parameter is the variable listed inside the parentheses in the function definition.
#參數是函數定義括弧內列出的變數。
#An argument is the value that are sent to the function when it is called.
#參數是調用功能時發送到函數的值。
#Number of Arguments 參數數
#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
#默認情況下，必須調用具有正確參數數的函數。這意味著，如果您的功能預期為 2 個參數，則必須用 2 個參數調用該函數，而不是更多，而不是更少。
print('-------------分隔線------------')
#This function expects 2 arguments, and gets 2 arguments:
#此函數預期為 2 個參數，並獲取 2 個參數：
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
#If you try to call the function with 1 or 3 arguments, you will get an error:
#如果您嘗試用 1 或 3 個參數呼叫該功能，則會出現錯誤：
print('-------------分隔線------------')
#This function expects 2 arguments, but gets only 1:
#此功能預期 2 個參數，但只得到 1：
'''
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")
'''
print("TypeError: my_function() missing 1 required positional argument: 'lname'")
#Related Pages 相關頁面
#Python Functions Tutorial Python 函數教程
#https://www.w3schools.com/python/python_functions.asp
#Function 函數 
#https://www.w3schools.com/python/gloss_python_function.asp
#Call a Function 調用函數 
#https://www.w3schools.com/python/gloss_python_function_call.asp
#*args *阿格斯
#https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
#Keyword Arguments 關鍵字參數
#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp
#*kwargs *克瓦格斯
#https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp
#Default Parameter Value 預設參數值
#https://www.w3schools.com/python/gloss_python_function_default_parameter.asp
#Passing a List as an Argument 將清單作為參數傳遞
#https://www.w3schools.com/python/gloss_python_function_passing_list.asp
#Function Return Value 函數返回值
#https://www.w3schools.com/python/gloss_python_function_return_value.asp
#The pass Statement i Functions pass語句 i 函數
#https://www.w3schools.com/python/gloss_python_function_pass.asp
#Function Recursion 函數遞歸
#https://www.w3schools.com/python/gloss_python_function_recursion.asp