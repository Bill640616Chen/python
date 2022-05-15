#https://www.w3schools.com/python/ref_func_isinstance.asp
#Python isinstance() Function Python isinstance()函數
#Returns True if a specified object is an instance of a specified object
#如果指定的對像是指定對象的實例，則返回 True。
#Check if the number 5 is an integer:
#檢查數位 5 是否是整數：
x = isinstance(5, int)
print(x)
#Definition and Usage 定義和用法
#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
#如果指定的對象擁有指定的類型，則isinstance（） 函數返回 True，否則返回 False。
#If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
#如果 type 參數是元組，則如果對像是元組中的類型之一，那麼此函數將返回 True。
#Syntax 語法
#isinstance(object, type)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An object.
#object：必需。 物件。
#type：A type or a class, or a tuple of types and/or classes
#type：類型或類，或類型和/或類的元組。
#Check if "Hello" is one of the types described in the type parameter:
#檢查 「Hello」 是否是 type 參數中描述的類型之一：
x = isinstance("Hello", (float, int, str, list, dict, tuple))
print(x)
#Check if y is an instance of myObj:
#檢查 y 是否是 myObj 的實例：
class myObj:
  name = "John"
y = myObj()
x = isinstance(y, myObj)
print(x)
#Related Pages 相關頁面
#The issubclass() function, to check if an object is a subclass of another object.
#issubclass（） 函數（檢查物件是否是另一個物件的子類）