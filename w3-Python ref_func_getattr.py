#https://www.w3schools.com/python/ref_func_getattr.asp
#Python getattr Function Python getattr函數
#Returns the value of the specified attribute (property or method)
#返回指定屬性的值（屬性或方法）。
#Get the value of the "age" property of the "Person" object:
#取得 「Person」 物件的 「age」 屬性的值：
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'age')
print(x)
#Definition and Usage 定義和用法
#The getattr() function returns the value of the specified attribute from the specified object.
#getattr（） 函數從指定的物件返回指定屬性的值。
#Syntax 語法
#getattr(object, attribute, default)
#Parameter參數：Values值
#Parameter參數：Description值
#object：Required. An object.
#object：必需。 物件。
#attribute：The name of the attribute you want to get the value from
#attribute：您要從中獲取值的屬性的名稱。
#default：Optional. The value to return if the attribute does not exist
#default：可選。 屬性不存在時返回的值。
#Use the "default" parameter to write a message when the attribute does not exist:
#如果屬性不存在，請使用 「default」 參數來寫一條消息：
class Person:
  name = "John"
  age = 36
  country = "Norway"
x = getattr(Person, 'page', 'my message')
print(x)
#Related Pages 相關頁面
#The delattr() function, to remove an attribute
#delattr（） 函數（刪除屬性）
#The hasattr() function, to check if an attribute exist
#hasattr（） 函數（檢查屬性是否存在）
#The setattr() function, to set the value of an attribute
#setattr（） 函數（設置屬性值）