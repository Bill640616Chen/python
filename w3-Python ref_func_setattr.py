#https://www.w3schools.com/python/ref_func_setattr.asp
#Python setattr() Function Python setattr()函數
#Sets an attribute (property/method) of an object
#設置物件的屬性（屬性/方法）。
#Change the value of the "age" property of the "person" object:
#改變 「person」 物件的 「age」 屬性的值：
class Person:
  name = "John"
  age = 36
  country = "Norway"
setattr(Person, 'age', 40)
print(setattr(Person, 'age', 40)) #None
print(setattr) #<built-in function setattr>
# The age property will now have the value: 40
x = getattr(Person, 'age')
print(x)
#Definition and Usage 定義和用法
#The setattr() function sets the value of the specified attribute of the specified object.
#setattr（） 函數指定物件的指定屬性的值。
#Syntax 語法
#setattr(object, attribute, value)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. An object.
#object：必需。 物件。
#attribute：Required. The name of the attribute you want to set
#attribute：必需。 您希望設定的屬性的名稱。
#value：Required. The value you want to give the specified attribute
#value：必需。 需要。 您要賦予指定屬性的值。
#Related Pages 相關頁面
#The delattr() function, to remove an attribute
#delattr（） 函數（刪除屬性）
#The getattr() function, to get the value of an attribute
#getattr（） 函數（獲取屬性的值）
#The hasattr() function, to check if an attribute exist
#hasattr（） 函數（檢查屬性是否存在）

