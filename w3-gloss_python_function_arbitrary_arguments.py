#https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
#*args * 阿格斯
#Arbitrary Arguments, *args 任意參數*args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#如果您不知道有多少參數將傳遞到您的函數中，請在函數定義中添加參數名稱之前。*
#This way the function will receive a tuple of arguments, and can access the items accordingly:
#這樣，該功能將收到大量參數(tuple)，並可以相應地訪問專案：
#If the number of arguments is unknown, add a * before the parameter name:
#如果參數數未知，則在參數名稱之前添加一個參數名稱：*
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
#kid[],[]裡的是tuple的索引位置
#Arbitrary Arguments are often shortened to *args in Python documentations.
#任意參數通常縮短為 Python 文件中的*args。
#Related Pages 相關頁面
#Python Functions Tutorial Python 函數教程
#https://www.w3schools.com/python/python_functions.asp
#Function 函數 
#https://www.w3schools.com/python/gloss_python_function.asp
#Call a Function 調用函數 
#https://www.w3schools.com/python/gloss_python_function_call.asp
#Function Arguments 函數參數
#https://www.w3schools.com/python/gloss_python_function_arguments.asp
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