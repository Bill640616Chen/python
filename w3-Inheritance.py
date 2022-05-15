#https://www.w3schools.com/python/python_inheritance.asp
#Python Inheritance 繼承
#Python Inheritance 繼承
#Inheritance allows us to define a class that inherits 
# all the methods and properties from another class.
#繼承允許我們定義一個從另一個類繼承所有方法和屬性的類。
#Parent class is the class being inherited from, also 
# called base class.
#家長班是正在被繼承的班級，也叫基礎班。
#Child class is the class that inherits from another 
# class, also called derived class.
#兒童類是繼承另一個類的類，也稱為衍生類。
print("-----------------------Create a Parent Class 創建父類")
#Create a Parent Class 創建父類
#Any class can be a parent class, so the syntax is the 
# same as creating any other class:
#任何類都可以是父類，因此語法與創建任何其他類相同：
#Create a class named Person, with firstname and lastname 
# properties, and a printname method:
#創建一個名為「人」的類，具有名和姓的屬性，以及列印名的方法：
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute
# the printname method:
x = Person("John", "Doe")
x.printname() #John Doe

print("-----------------------Create a Child Class 創造子類")
#Create a Child Class 創造子類
#To create a class that inherits the functionality from 
# another class, send the parent class as a parameter when
# creating the child class:
#要創建從其他類繼承功能的類，請在創建子類時將父類作為參數發送：
#Create a class named Student, which will inherit the 
# properties and methods from the Person class:
#創建一個名為「學生」的類，該類將從「人」類中繼承屬性和方法：
class Student(Person):
  pass
#Note: Use the pass keyword when you do not want to add any
# other properties or methods to the class.
#注意：當您不想在類中添加任何其他屬性或方法時，請使用pass關鍵字。
#Now the Student class has the same properties and methods as the Person class.
#現在"學生"類具有與"人"類相同的屬性和方法。
#Use the Student class to create an object, and then execute the printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person): #子類繼續父類的寫法
  pass
x = Student("Mike", "Olsen") #子類用父類的函法
x.printname() #Mike Olsen

print("----------------在子類--Add the __init__() Function")
#Add the __init__() Function 添加__init__（） 函數
#So far we have created a child class that inherits the properties and methods from its parent.
#到目前為止，我們已經創建了一個子類，從其父類繼承屬性和方法。
#We want to add the __init__() function to the child class (instead of the pass keyword).
#我們希望將__init__（）功能添加到子類（而不是pass關鍵字）。
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#注意：每次使用類創建新物件時，都會自動調用__init__（）功能。
#Add the __init__() function to the Student class:
#class Student(Person):
  #def __init__(self, fname, lname):
    #add properties etc.
#When you add the __init__() function, the child class 
# will no longer inherit the parent's __init__() function.
#當您添加__init__（）功能時，子類將不再繼承父類的__init__（）功能。
#Note: The child's __init__() function overrides the 
# inheritance of the parent's __init__() function.
#注：子類的__init__（）功能淩駕於父類__init__（）功能的繼承上。

#To keep the inheritance of the parent's __init__() function, 
# add a call to the parent's __init__() function:
#要保留父__init__（）功能的繼承，請向父__init__（）功能添加呼叫：
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(a, fname, lname):
#子類的__init__()功能淩駕於父類__init__()功能的繼承上    
    Person.__init__(a, fname, lname)
#向父類__init__()功能呼叫：
x = Student("Mike", "Olsen") #把子類實體化
#子類創立__init__(a, fname, lname),a是屬於子類
#所以呼叫父煩的__init__(self, fname, lname)時
#self在子類,所以必須改成a,才不會造成錯誤
x.printname() #Mike Olsen
#Now we have successfully added the __init__() function, 
# and kept the inheritance of the parent class, and we 
# are ready to add functionality in the __init__() function.
#現在，我們已經成功地增加了__init__()功能，並保留了父類的繼承，
# 我們準備在__init__()功能中添加功能。

print("--------super() Function 用於調用父類（超類）的一個方法")
#Use the super() Function 用於調用父類（超類）的一個方法
#super（）是用來解決多重繼承問題的，直接用類名調用父類方法在
# 使用單繼承的時候沒問題，但是如果使用多繼承，會涉及到
# 查找順序（MRO）、重複調用（鑽石繼承）等種種問題。
#Python also has a super() function that will make the 
# child class inherit all the methods and properties from
# its parent:
#Python 還具有super()功能，可使子類從其父類繼承所有方法和屬性
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    #super()取代Person,調用父類繼承所有方法和屬性
x = Student("Mike", "Olsen")
#這裡可以調用父類的方法是用了super()
x.printname() #Mike Olsen

print("----------------------------Add Properties 添加屬性")
#Add Properties 添加屬性
#Add a property called graduationyear to the Student class:
#在學生類(子類)添加稱為畢業年的屬性：
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
    #像self.firstname = fname一樣都是類裡的屬性
x = Student("Mike", "Olsen") #一直要實體化類,才能調用類裡面的方法
print(x.graduationyear) #2019

print("--------------------------------在子類中可以增加參數")
#在下面的示例中，2019 年應該是一個變數，並在創建學生類時傳遞到
# 學生類。為此，必須在__init__()函數中添加另一個參數：
#Add a year parameter, and pass the correct year when creating objects:
#添加一個年的參數，並在創建物件時通過正確的年份：
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) 
    #因為調用父類的函數,沒辦法在這增加參數
    #year參數只能加在子類
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear) #2019

print("--------------------------------Add Methods 添加方法")
#Add Methods 添加方法
#Add a method called welcome to the Student class:
#添加一種稱為welcome的方法到學生的類：
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
x.welcome() #Welcome Mike Olsen to the class of 2019
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
#如果在子類中添加與父類功能相同的名稱方法，則父類方法的繼承將被推翻。










