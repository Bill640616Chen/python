#https://www.w3schools.com/python/ref_func_hasattr.asp
#Python hasattr Function Python hasattr函數
#Returns True if the specified object has the specified attribute (property/method)
#如果指定的對象擁有指定的屬性（屬性/方法），則返回 True。
#Check if the "Person" object has the "age" property:
#檢查 「Person」 物件是否有 「age」 屬性：
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = hasattr(Person, 'age')
print(x)
#Definition and Usage 定義和用法
#The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
#如果指定的對象擁有指定的屬性，則hasattr（） 函數將返回 True，否則返回 False。
#Syntax 語法
#hasattr(object, attribute)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An object.
#object：必需。 物件。
#attribute：The name of the attribute you want to check if exists
#attribute：您要檢查是否存在的屬性名稱。
#Related Pages 相關頁面
#The delattr() function, to remove an attribute
#delattr（） 函數（刪除屬性）
#The getattr() function, to get the value of an attribute
#getattr（） 函數（獲取屬性值）
#The setattr() function, to set the value of an attribute
#setattr（） 函數（設置屬性值）

