#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp
#**kwargs 任意關鍵字參數
#Arbitrary Keyword Arguments, **kwargs 任意關鍵字參數
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: before the parameter name in the function definition.**
#如果您不知道有多少關鍵字參數將傳遞到您的函數中，請添加兩個星號：在函數定義中的參數名稱之前。**
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
#這樣，該功能將接收參數字典，並可以相應地訪問專案：
print('-------------分隔線**kwargs------------')
#If the number of keyword arguments is unknown, add a double before the parameter name:**
#如果關鍵字參數的數量未知，在參數名稱之前添加雙倍：**
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
#**kwargs裡的參數無法使用索引
print('-------------分隔線*args------------')
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
#Python 文件中，任意 Kword 參數通常被縮短為**kwargs。
#Related Pages 相關頁面
#Python Functions Tutorial Python 函數教程
#https://www.w3schools.com/python/python_functions.asp
#Function 函數 
#https://www.w3schools.com/python/gloss_python_function.asp
#Call a Function 調用函數 
#https://www.w3schools.com/python/gloss_python_function_call.asp
#Function Arguments 函數參數
#https://www.w3schools.com/python/gloss_python_function_arguments.asp
#*args *阿格斯
#https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
#Keyword Arguments 關鍵字參數
#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp
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