#https://www.w3schools.com/python/ref_func_vars.asp
#Python vars() Function Python vars()函數
#Returns the __dict__ property of an object
#返回物件的 __dict__ 屬性。
#Return the __dict__ atribute of an object called Person:
#傳回名為 Person 的物件的 __dict__ 屬性：
class Person:
  name = "John"
  age = 36
  country = "norway"
x = vars(Person)
print(x)
#Definition and Usage 定義和用法
#The vars() function returns the __dic__ attribute of an object.
#vars（） 函數傳回物件的 __dic__ 屬性。
#The __dict__ attribute is a dictionary containing the object's changeable attributes.
#__dict__ 屬性是包含物件的可變屬性的字典。
#Note: calling the vars() function without parameters will return a dictionary containing the local symbol table.
#註釋：不帶參數調用 vars（） 函數將返回包含局部符號表的字典。
#Syntax 語法
#vars(object)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Any object with a __dict__attribute
#object：任何具有 __dict__ 屬性的物件。