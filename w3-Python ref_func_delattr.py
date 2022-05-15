#https://www.w3schools.com/python/ref_func_delattr.asp
#Python delattr Function Python delattr函數
#Deletes the specified attribute (property or method) from the specified object
#從指定的物件中刪除指定的屬性（屬性或方法）。
#Delete the "age" property from the "person" object:
#刪除 「person」 物件的 「age」 屬性：
class Person:
  name = "John"
  age = 36
  country = "Norway"
delattr(Person, 'age')
#Definition and Usage 定義和用法
#The delattr() function will delete the specified attribute from the specified object.
#delattr（） 函數將從指定物件中刪除指定屬性。
#Syntax 語法
#delattr(object, attribute)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An object.
#object：必需。 物件。
#attribute：Required. The name of the attribute you want to remove
#attribute：必需。 您希望刪除屬性的名稱。
#Related Pages 相關頁面
#The getattr() function, to get the value of an attribute
#getattr（） 函數（獲取屬性值）
#The hasattr() function, to check if an attribute exist
#hasattr（） 函數（檢查屬性是否存在）
#The setattr() function, to set the value of an attribute
#setattr（） 函數（設置屬性值）