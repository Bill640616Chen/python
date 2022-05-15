#https://www.w3schools.com/python/gloss_python_lambda.asp
#Lambda Function 匿名函數
#A lambda function is a small anonymous function.
#匿名函數是一個小的匿名函數。
#A lambda function can take any number of arguments, but can only have one expression.
#匿名函數可以採取任意數量的參數，但只能有一個表達。
#Syntax 語法
#lambda arguments : expression
#The expression is executed and the result is returned:
#執行表示語並返回結果：
#A lambda function that adds 10 to the number passed in as an argument, and print the result:
#將 10 新增到作為參數傳遞的數位的 lambda 函數，並列印結果：
x = lambda a : a + 10
print(x(5))
print('-------------分隔線------------')
#Lambda functions can take any number of arguments:
#Lambd函數可以採取任意數量的參數：
#A lambda function that multiplies argument a with argument b and print the result:
#將參數 b 與參數 b 成倍增加並列印結果的 lambda 函數：
x = lambda a, b : a * b
print(x(5, 6))
print('-------------分隔線------------')
#A lambda function that sums argument a, b, and c and print the result:
#一個lambda函數，它總結了參數 a、b 和 c 並列印結果：
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#Related Pages 相關頁面
#Python Lambda Tutorial Python Lambda教程
#https://www.w3schools.com/python/python_lambda.asp
#Why Use Lambda Functions 為什麼使用Lambda函數
#https://www.w3schools.com/python/gloss_python_lambda_why.asp