#https://www.w3schools.com/python/gloss_python_return_boolean.asp
#return_boolean 傳回布林斯值
#Functions can Return a Boolean
#函數可以返回布爾
#You can create functions that returns a Boolean Value:
#您可以建立返回布林值的函數：
#Print the answer of a function:
#列印函數的答案：
def myFunction() :
  return True
print(myFunction())
#You can execute code based on the Boolean answer of a function:
#您可以根據布林對函數的回答執行代碼：
print('-------------分隔線------------')
#Print "YES!" if the function returns True, otherwise print "NO!":
#列印"是！"，如果函數返回真實，否則列印"否！"
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
#Python also has many built-in functions that returns a boolean value, like the function, which can be used to determine if an object is of a certain data type:isinstance()
#Python 還具有許多內置函數，可返回布林值，如該函數，可用於確定物件是否具有特定數據類型：isinstance()
print('-------------分隔線------------')
#Check if an object is an integer or not:
#檢查物件是否為整數：
x = 200
print(isinstance(x, int))
#isinstance的意思是「判斷類型」
#Related Pages 相關頁面
#Python Booleans Tutorial Python 布爾斯教程
#https://www.w3schools.com/python/python_booleans.asp
#boolean_values 布爾斯值
#https://www.w3schools.com/python/gloss_python_boolean_values.asp
#Evaluate Booleans 評估布爾斯
#https://www.w3schools.com/python/gloss_python_evaluate_boolean_values.asp
