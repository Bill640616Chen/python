#https://www.w3schools.com/python/ref_keyword_assert.asp
#Python Keyword assert 關鍵字 assert
#For debugging
#用於調試。
#Test if a condition returns True:
#測試條件是否返回 True：
x = "hello"
#if condition returns True, then nothing happens:
#如果條件返回True，則什麼也不會發生：
assert x == "hello"
#if condition returns False, AssertionError is raised:
##如果条件返回 False，則會引發 AssertionError：
#assert x == "goodbye"
#錯誤訊息assert x == "goodbye"
#AssertionError
#Definition and Usage 定義和用法
#The assert keyword is used when debugging code.
#assert 關鍵字在調試代碼時使用。
#The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
#assert 關鍵字使您可以測試代碼中的條件是否返回 True，否則，程式將引發 AssertionError。
#You can write a message to be written if the code returns False, check the example below.
#您可以編寫一條若代碼返回 False 時輸出的消息，請看下面的例子。
#Write a message if the condition is False:
print('-------------分隔線------------')
#如果條件為 False，則寫一條消息：
y = "hello"
#if condition returns False, AssertionError is raised:
# 如何條件返回 False，引發 AssertionError：
assert y == "goodbye", "y should be 'hello'"