#https://www.w3schools.com/python/ref_keyword_raise.asp
#Python Keyword raise 關鍵字 raise
#To raise an exception
#產生異常。
#Raise an error and stop the program if x is lower than 0:
#如果 x 大於 0，則沒引發錯誤執行下個程式：false就沒執行下一行
#如果 x 小於 0，則引發錯誤並停止程式：true就繼續執行下一行
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
#Definition and Usage 定義和用法
#The raise keyword is used to raise an exception.
#raise 關鍵字用於引發異常。
#You can define what kind of error to raise, and the text to print to the user.
#您可以定義要引發的錯誤類型以及要向使用者列印的文字。
#Raise a TypeError if x is not an integer:
print('-------------分隔線------------')
#如果 x 不是整數，則引發 TypeError：
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
