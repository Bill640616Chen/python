#https://www.w3schools.com/python/ref_func_dir.asp
#Python dir Function Python dir函數
#Returns a list of the specified object's properties and methods
#返回指定物件的屬性和方法的清單。
#Display the content of an object:
#顯示物件的內容：
class Person:
  name = "John"
  age = 36
  country = "Norway"
print(dir(Person))
#Definition and Usage 定義和用法
#The dir() function returns all properties and methods of the specified object, without the values.
#dir（） 函數傳回指定物件的所有屬性和方法，不帶值。
#This function will return all the properties and methods, even built-in properties which are default for all object.
#此函數會返回所有屬性和方法，甚至是所有物件預設的內置屬性。
#Syntax語法
#dir(object)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：The object you want to see the valid attributes of
#object：您要查看其有效屬性的物件。
