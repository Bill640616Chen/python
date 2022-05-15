#https://www.w3schools.com/python/ref_keyword_lambda.asp
#Python Keyword lambda 關鍵字 lambda
#To create an anonymous function
#創建匿名函數。
#Create a function that adds 10 to any number you send:
#建立函數，將發送的任意數位加 10：
x = lambda a : a + 10
print(x(5))
#Definition and Usage 定義和用法
#The lambda keyword is used to create small anonymous functions.
#lambda 關鍵字用於創建小型匿名函數。
#A lambda function can take any number of arguments, but can only have one expression.
#Lambda 函數可以接受任意數量的參數，但只能擁有一個運算式。
#The expression is evaluated and the result is returned.
#這個表達式會被計算並返回結果。
#A lambda function with three arguments:
print('-------------分隔線------------')
#具有三個參數的 lambda 函數：
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#Related Pages 相關頁面
#Read more about lambda functions in our Python Lambda Tutorial.
#請在我們的 Python Lambda 教程 中學習更多 lambda 函數的知識。