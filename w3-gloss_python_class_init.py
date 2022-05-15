#https://www.w3schools.com/python/gloss_python_class_init.asp
#__init__() Function __init__()函數
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#以上示例是最簡單的類和物件，在現實生活中應用中並不真正有用。
#To understand the meaning of classes we have to understand the built-in __init__() function.
#要理解課程的意義，我們必須瞭解內置的__init__（）功能。
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#所有類都有一個稱為__init__（）的功能，當類啟動時，該功能始終執行。
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
#使用__init__（） 功能將值分配給物件屬性，或在建立物件時需要執行的其他操作：
#Create a class named Person, use the __init__() function to assign values for name and age:
#建立名為「人」的類，使用__init__（）功能為姓名和年齡分配值：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1)
print( Person("John", 36)) #與上一行記憶體位址不一樣
#列印是哪種型別物件,在記憶體哪個位址
#<__main__.Person object at 0x000001C813DAAD30>
print("name:" + p1.name + " " + "age:" + str(p1.age))
print(p1.age)
#Note: The function is called automatically every time the class is being used to create a new object.__init__()
#注意：每次使用該類創建新物件時，該功能都會自動調用。__init__()
#Related Pages 相關頁面
#Python Syntax Tutorial Python 語法教程
#https://www.w3schools.com/python/python_classes.asp
#Class 類
#https://www.w3schools.com/python/gloss_python_class.asp
#Create Class 創建類
#https://www.w3schools.com/python/gloss_python_class_create.asp
#Object Methods 物件方法
#https://www.w3schools.com/python/gloss_python_object_methods.asp
#self 自我
#https://www.w3schools.com/python/gloss_python_self.asp
#Modify Object Properties 修改物件屬性
#https://www.w3schools.com/python/gloss_python_object_modify_properties.asp
#Delete Object Properties 刪除物件屬性
#https://www.w3schools.com/python/gloss_python_object_delete_properties.asp
#Delete Object 刪除物件
#https://www.w3schools.com/python/gloss_python_object_delete.asp
#Class pass Statement 類pass語句
#https://www.w3schools.com/python/gloss_python_class_pass.asp