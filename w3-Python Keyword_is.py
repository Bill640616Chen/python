#https://www.w3schools.com/python/ref_keyword_is.asp
#Python Keyword is 關鍵字 is
#To test if two variables are equal
#測試兩個變數是否相等。
#Check if two objects are the same object:
#檢查兩個物件是否為相同物件：
x = ["apple", "banana", "cherry"]
y = x
print(x is y)
#Definition and Usage 定義和用法
#The is keyword is used to test if two variables refer to the same object.
#is 關鍵字用於測試兩個變數是否引用同一物件。
#The test returns True if the two objects are the same object.
#如果兩個對像是同一物件，則test返回True。
#The test returns False if they are not the same object, even if the two objects are 100% equal.
#如果兩個物件不是同一物件，即使兩個物件 100% 相等，test 也會返回 False。
#Use the == operator to test if two variables are equal.
#請使用 == 運算子測試兩個變數是否相等。
#Test two objects that are equal, but not the same object:
print('-------------分隔線------------')
#測試兩個相等但不相同的物件：
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y) #False
print(x == y) #True