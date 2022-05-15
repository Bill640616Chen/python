#https://www.w3schools.com/python/gloss_python_create_init.asp
#Add __init__() Function 添加__init__()函數
#So far we have created a child class that inherits the properties and methods from its parent.
#到目前為止，我們已經創建了一個子類別，從其父級繼承屬性和方法。
#We want to add the function to the child class (instead of the keyword).__init__()pass
#我們希望將功能添加到子類（而不是關鍵字）。__init__()pass
#Note: The function is called automatically every time the class is being used to create a new object.__init__()
#注意：每次使用該類創建新物件時，該功能都會自動調用。__init__()
#Add the function to the class:__init__()Student
#將功能新增到類別中：__init__()Student
#class Student(Person):
#  def __init__(self, fname, lname):
#    #add properties etc.
#When you add the function, the child class will no longer inherit the parent's function.__init__()__init__()
#添加該功能時，子類將不再繼承父類的功能。__init__()__init__()
#Note: The child's function overrides the inheritance of the parent's function.__init__() __init__()
#注意：孩子的功能淩駕於父母職能的繼承上。__init__() __init__()
#To keep the inheritance of the parent's function, add a call to the parent's function:__init__()__init__()
#為了保持父的功能繼承，請向父的函數添加呼叫：__init__()__init__()
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    #父類的屬性初始化
x = Student("Mike", "Olsen")
x.printname()
#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the function.__init__()
#現在，我們已經成功地增加了__init__（）功能，並保留了父類的繼承，我們準備在功能中添加功能。__init__()
#Related Pages 相關頁面
#Python Inheritance Tutorial Python 繼承教程
#https://www.w3schools.com/python/python_inheritance.asp
#Create Parent Class 創建父類
#https://www.w3schools.com/python/gloss_python_parent_class.asp
#Create Child Class 創建子類
#https://www.w3schools.com/python/gloss_python_child_class.asp
#super Function 繼承函數
#https://www.w3schools.com/python/gloss_python_super.asp
#Add Class Properties 添加類屬性
#https://www.w3schools.com/python/gloss_python_class_add_properties.asp
#Add Class Methods 添加類方法
#https://www.w3schools.com/python/gloss_python_class_add_methods.asp