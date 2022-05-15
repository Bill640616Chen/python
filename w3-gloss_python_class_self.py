#https://www.w3schools.com/python/gloss_python_self.asp
#Self 
#The parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.self
#參數是當前類實例的引用，用於訪問屬於該類的變數。self
#It does not have to be named , you can call it whatever you like, but it has to be the first parameter of any function in the class:self
#它不必命名，你可以稱之為任何你喜歡的，但它必須是任何功能在類的第一參數：self
#Use the words mysillyobject and abc instead of self:
#使用「神秘物件」和「abc」而不是「自我」這兩個詞：
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#Note: The parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.self
#注意：參數是該類當前實例的引用，用於訪問屬於該類的變數。self
#Related Pages 相關頁面
#Python Syntax Tutorial Python 語法教程
#https://www.w3schools.com/python/python_classes.asp
#Class 類
#https://www.w3schools.com/python/gloss_python_class.asp
#Create Class 創建類
#https://www.w3schools.com/python/gloss_python_class_create.asp
#The Class __init__() Function 類__init__（） 功能
#https://www.w3schools.com/python/gloss_python_class_init.asp
#Object Methods 物件方法
#https://www.w3schools.com/python/gloss_python_object_methods.asp
#Modify Object Properties 修改物件屬性
#https://www.w3schools.com/python/gloss_python_object_modify_properties.asp
#Delete Object Properties 刪除物件屬性
#https://www.w3schools.com/python/gloss_python_object_delete_properties.asp
#Delete Object 刪除物件
#https://www.w3schools.com/python/gloss_python_object_delete.asp
#Class pass Statement 類pass語句
#https://www.w3schools.com/python/gloss_python_class_pass.asp