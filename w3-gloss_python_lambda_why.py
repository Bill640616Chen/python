#https://www.w3schools.com/python/gloss_python_lambda_why.asp
#Why Lambda Function 為什麼使用匿名函數
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#當您在另一個函數中將 lambda 用作匿名功能時，可以更好地顯示它們的力量。
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
#假設您有一個需要一個參數的函數定義，該參數將乘以一個未知數位：
def myfunc(n):
  return lambda a : a * n
print('-------------分隔線------------')
#Use that function definition to make a function that always doubles the number you send in:
#使用函數定義使功能始終使您發送的號碼翻倍：
def myfunc(n):
  return lambda a , b : a * n * b
mydoubler = myfunc(2)
print(mydoubler(11,2))
print('-------------分隔線------------')
#Or, use the same function definition to make a function that always triples the number you send in:
#或者，使用相同的函數定義使功能始終使您發送的號碼增加三倍：
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
print('-------------分隔線------------')
#Or, use the same function definition to make both functions, in the same program:
#或者，在同一程式中使用相同的函數定義來使兩個功能：
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
#Use lambda functions when an anonymous function is required for a short period of time.
#當需要短時間的匿名功能時，使用 lambda 功能。
#Related Pages 相關頁面
#Python Lambda Tutorial Python Lambda教程
#https://www.w3schools.com/python/python_lambda.asp
#Lambda Functions Lambda函數
#https://www.w3schools.com/python/gloss_python_lambda.asp