#https://www.w3schools.com/python/gloss_python_child_class.asp
#Create Child Class 建立子類
#To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
#要創建從其他類繼承功能的類，請在創建子類時將父類作為參數發送：
#Create a class named , which will inherit the properties and methods from the class:StudentPerson
#創建一個命名的類，該類將從類中繼承屬性和方法：StudentPerson
#class Student(Person):
#  pass
#Note: Use the keyword when you do not want to add any other properties or methods to the class.pass
#注意：當您不想將任何其他屬性或方法添加到類中時，請使用關鍵字。pass
#Now the Student class has the same properties and methods as the Person class.
#現在學生班具有與人類相同的屬性和方法。
#Use the class to create an object, and then execute the method:Studentprintname
#使用該類別建立物件，然後執行方法：Student printname
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
#printname(),不管有沒有import,結果都一樣
#因為父類的Person並沒有設定參數,所以printname()裡有參數,會發生錯誤
#NameError: name 'Self' is not defined
print('------------網站範例(把2維陣列轉換為1維)------------')
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
    #else這2行沒寫的話也不會影結果,因為原陣列是
    #[[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]] 
    #因為if條是要元素為清單,就會進到下面的迴圈,不會到else
        else:
            flat_list.append(element)
    #如果多了str,11,12,13,因為str不是list,若沒else這語句,則輸出只有
    #Transformed Flat List [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #element代表陣列裡的元素,list,str都算
    return flat_list
nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10],11,12,13]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))
#Related Pages 相關頁面
#Python Inheritance Tutorial Python 繼承教程
#https://www.w3schools.com/python/python_inheritance.asp
#Create Parent Class 創建父類
#https://www.w3schools.com/python/gloss_python_parent_class.asp
#Create the __init__() Function 創建__init__（） 功能
#https://www.w3schools.com/python/gloss_python_create_init.asp
#super Function 繼承函數
#https://www.w3schools.com/python/gloss_python_super.asp
#Add Class Properties 添加類屬性
#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Methods 添加類方法
#https://www.w3schools.com/python/gloss_python_class_add_methods.asp