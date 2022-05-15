#https://www.w3schools.com/python/python_lambda.asp
#Python Lambda 匿名函數
#A lambda function is a small anonymous function.
#lambda函數是一個小的匿名函數
#A lambda function can take any number of arguments, but can only have one expression.
#lambda函數可以取任何參數的數量,但只有一個表達式
#Syntax 語法
#lambda arguments : expression
#lambda 參數 ： 表達式
#The expression is executed and the result is returned:
#這個表達式可以被執行並且結果可以傳回
#Add 10 to argument a, and return the result:
print("----------------------------增加10到參數a,並且傳回結果")
#增加10到參數a,並且傳回結果
x = lambda a : a + a + 10
print(x(5)) 
#20,(5)是lambda a : 匿名函數
# 參數a:a+a(:後面必有只有a,數量不限)(5)是lambda的a
print("---------------------將參數 a 與參數 b 相乘並返回結果")
#Lambda functions can take any number of arguments:
#Lambda函數可以取任何參數的數字
#Multiply argument a with argument b and return the result:
#將參數 a 與參數 b 相乘並返回結果：
x = lambda a, b : a * b * a
print(x(5, 6)) 
#150,(5, 6)是lambda a, b : 匿名參數
# 參數a,b:a*b*a(:後面必有只有ab,數量不限)(5,6)是lambda a, b
print("------------------------加總參數 a、b 和 c 並返回結果")
#Summarize argument a, b, and c and return the result:
#加總參數 a、b 和 c 並返回結果：
x = lambda a, b, c : a + b + c * a
print(x(5, 6, 2)) 
#21,(5,6,2)是lambda a, b, c : 匿名函數
# 參數a, b, c : a + b + c * a(:後面必須只有abc,數量不限)
# (5,6,2)是lambda a, b, c : a + b + c * a