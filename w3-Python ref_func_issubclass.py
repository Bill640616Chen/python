#https://www.w3schools.com/python/ref_func_issubclass.asp
#Python issubclass() Function Python issubclass()函數
#Returns True if a specified class is a subclass of a specified object
#如果指定的類是指定物件的子類，則返回 True。
#Check if the class myObj is a subclass of myAge:
#檢查 myObj 是否是 myAge 的子類：
class myAge:
  age = 36
class myObj(myAge):
  name = "John"
  age = myAge
x = issubclass(myObj, myAge)
print(x)
#Definition and Usage 定義和用法
#The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
#issubclass（） 如果指定對像是指定物件的子類，則 issubclass（） 函數將返回 True，否則返回 False。
#Syntax 語法
#issubclass(object, subclass)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An object.
#object：必需。 物件。
#subclass：A class object, or a tuple of class objects
#subclass：物件，或 class 物件的元組。
#Related Pages 相關頁面
#The isinstance() function, to check if an object is of a certain type.
#isinstance（） 函數（檢查物件是否是特定類型）

