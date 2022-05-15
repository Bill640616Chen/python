#https://www.w3schools.com/python/python_variables_output.asp
#輸出變數
#Python 語句通常用於輸出變數。print
#要將文本和變數相結合，Python 使用字元：+
x = "awesome"
print("Python is " + x)
#Python is awesome
#您還可以使用該字元向另一個變數添加變數：+
x = "Python is "
y = "awesome"
z =  x + y
print(z)
#Python is awesome
#對於數位，字元作為數學操作員工作：+
x = 5
y = 10
print(x + y)#15
#如果您試著將字串和數位相結合，Python 會給您一個錯誤：
#只能用format解決
#x = 5
#y = "John"
#print(x + y)
#print(x * y)乘號可以,JohnJohnJohnJohnJohn
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#不受支援的操作類型
#只能用format解決
txt1 = "{}, is the cutest man in the world"
age1 = "Tommy Lu "
print(txt1.format(age1))
txt1 = "{} is 5 years old"
age1 = "John"
print(txt1.format(age1))
