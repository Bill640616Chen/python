#https://www.w3schools.com/python/python_classes.asp
#Python Classes and Objects 類別和物件
#Python Classes/Objects Python 類/物件
#Python is an object oriented programming language.
#Python 是一種物件導向的程式設計語言。
#Almost everything in Python is an object, with its properties and methods.
#幾乎所有東西在Python裡都是一個物件，具有其特性和方法。
#A Class is like an object constructor, or a "blueprint" for creating objects.
#類就像物件構造器，或創建物件的"藍圖"。
#Create a Class 創建類
#To create a class, use the keyword class:

print("----------------------------要建立類，請使用關鍵字類")
#要建立類，請使用關鍵字類：
#Create a class named MyClass, with a property named x:
#創建名為 MyClass 的類，其中屬性名為 x：
class MyClass:
  x = 5 #X可以稱為變數或物件,5可以稱為參數
print(MyClass) #因為直接印出物件本身
#直接印出類本身<class '__main__.MyClass'>
#不論是從腳本檔案讀取的或是互動模式中的，會被視為
# 一個稱為 __main__ 的模組的一部分
#所以MyClass是__main__模組的一部分

print("----------------------------Create Object 創建物件")
#Create Object 創建物件
#Now we can use the class named MyClass to create objects:
#現在，我們可以使用名為 MyClass 的類來創建物件：
#Create an object named p1, and print the value of x:
#建立名為 p1 的物件，並列印 x 值：
class MyClass:
  x = 5
  y = "engine"
p1 = MyClass()
print(p1.x)
print(p1.y)
#5,p1是MyClass的物件,所以p1.x是取類裡的值
#engine,p1是MyClass的物件,所以p1.y是取類裡的值

#官方文件範例https://docs.python.org/zh-tw/3/tutorial/classes.html?highlight=class
print("----------------------------作用域和命名空間的範例")
#作用域和命名空間的範例
#這是一個範例，演示如何參照不同的作用域和命名空間，以及 global 和 nonlocal 如何影響變數的綁定：
def scope_test(): #作用域測試
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    #assignment賦值
scope_test() #scope 作用域
print("In global scope:", spam)
    #呼叫do_local()時
    #外面已經有spam = "test spam"改變了do_local():裡的值
    #所以After local assignment: test spam
    #呼叫do_nonlocal()時
    #nonlocal的spam改變了外面spam的值
    #After nonlocal assignment: nonlocal spam
    #呼叫do_global()時
    #雖然global改變了nonlocal的值,但是呼叫函數的位置
    #在def cope_test():裡面,所以只能用nonlocal的spam值
    #After global assignment: nonlocal spam
    #scope_test()是外圍呼叫的函數,所以spamh的賦是global spam
    #In global scope: global spam

print("----------------------MyClass是類別，必須實體化才能用")
#Class 物件
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
p1 = MyClass() #MyClass是類別，必須實體化才能用
print(p1.f()) #hello world
print(p1.i) #12345
#若以車來舉例,MyClass只是藍圖
#所以你不能直接使用藍圖,必須經過實體化,即p1=MyClsss()
#用藍圖造成一台名叫p1的車,
# 然後才能跟人說我這台p1跑車裡有個東西叫x, 即p1.x
#然後p1車裡有個按鍵，按下會跳出hello world , 即p1.f()
#因為是方法函數，所以後面要有()

print("-------------喜歡在建立物件時有著自訂的特定實例初始狀態")
#實例化運算（「呼叫」一個 class 物件）會建立一個空的物件。
# 許多 class 喜歡在建立物件時有著自訂的特定實例初始狀態。
# 因此，class 可以定義一個名為 __init__() 的特別 method，
# 像這樣：
class MyClass:
    def __init__(self,data):
        self.data = data
x = MyClass(36) #要把類實體化,才能調用裡面的函數
print(x.data) #36

print("-------------------------------------__init__()函數")
#回到https://www.w3schools.com/python/python_classes.asp
#The __init__() Function __init__()函數
#The examples above are classes and objects in their 
# simplest form, and are not really useful in real life 
# applications.
#以上示例是最簡單的類和物件，在現實生活中應用中並不真正有用。
#To understand the meaning of classes we have to understand
#  the built-in __init__() function.
#要理解class(類)的意義，我們必須瞭解內建的__init__()功能。
#All classes have a function called __init__(), which is 
# always executed when the class is being initiated.
#所有類都有一個稱為__init__()的功能，當類啟動時，該功能始終執行。
#Use the __init__() function to assign values to object 
# properties, or other operations that are necessary to 
# do when the object is being created:
#使用__init__()功能將值分配給物件屬性，或在建立物件時需要執行的
# 其他操作：
#Create a class named Person, use the __init__() function to assign values for name and age:
#建立名為「人」的類，使用__init__（）功能為姓名和年齡分配值：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36) #Person是類別，必須實體化才能用
print(p1.name) #John,將值分配給物件屬性
print(p1.age) #36,將值分配給物件屬性
#Note: The __init__() function is called automatically 
# every time the class is being used to create a new object.
#注意：每次使用類創建新物件時，都會自動調用__init__()功能。

print("-------------------------------Object Methods 物件方法")
#Object Methods 物件方法
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#物件也可以包含方法。物件中的方法是屬於物件的函數。
#Let us create a method in the Person class:    
#讓我們在人員類中創建一種方法：
#Insert a function that prints a greeting, and execute it on the p1 object:
#插入列印問候語的功能，並在 p1 物件上執行：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name , self.age)
p1 = Person("John", 36)
p1.myfunc() 
#Hello my name is John
#剛剛做了測試,print()裡的格式,取決於"Hello my name is " +，
# +的後面只能是字串,要輸出36,用逗號隔開,就好啦!!
# 或是用+把int字串化
#Note: The self parameter is a reference to the current 
# instance of the class, and is used to access variables 
# that belong to the class.
#注意：self參數是當前類實例的參考，用於訪問屬於該類的變數。

print("-------------------------The self Parameter self參數")
#The self Parameter self參數
#The self parameter is a reference to the current instance
# of the class, and is used to access variables that 
# belongs to the class.
#self參數是當前類實例的引用，用於訪問屬於類的變數。
#It does not have to be named self , you can call it 
# whatever you like, but it has to be the first parameter 
# of any function in the class:
#它不必被命名為self，你可以稱之為任何你喜歡的，但它必須是任何
# 功能在類的第一參數：
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
print("-----------------The self Parameter self參數-測試1")
class Person:
  def __init__(self, name, age): #self屬於類
    self.name = name #self.name類的變數
    self.age = age #self.age類的變數
  def myfunc(a): 
      #myfunc(a)裡的參數並須在print裡訪問類的變數
    print("Hello my name is " + a.name , a.age)
z = Person("John", 36) #物件=Person(name, age),把類實體化
z.myfunc() 
print("-----------------The self Parameter self參數-測試2")
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = 2 #這裡=name才會被訪問
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " , abc.name)
p1 = Person("John", 36)
p1.myfunc() 
#Hello my name is 2,取了mysillyobject.name = 2的值
#當mysillyobject.name = 2時,
#__init__(mysillyobject, name, age):abc.name並沒有訪問name

print("---------------Modify Object Properties 修改物件屬性")
#Modify Object Properties 修改物件屬性
#You can modify properties on objects like this:
#您可以修改此類物件上的屬性像這樣：
#Set the age of p1 to 40:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name + "  age:", self.age)
p1 = Person("John", 36)
p1.age = 40 #修改物件屬性
p1.name = "Tom" #修改物件屬性
p1.myfunc() #Hello my name is Tom
print(p1.age) #40

print("---------------Delete Object Properties 刪除物件屬性")
#Delete Object Properties 刪除物件屬性
#You can delete properties on objects by using the del keyword:
#您可以使用 del 關鍵字刪除物件上的屬性：
#Delete the age property from the p1 object:
#從 p1 物件中移除年齡屬性：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
#del p1.age
#print(p1.age)
#AttributeError: 'Person' object has no attribute 'age'

print("---------------------------Delete Objects 刪除物件")
#Delete Objects 刪除物件
#You can delete objects by using the del keyword:
#您可以使用 del 關鍵字移除物件：
#Delete the p1 object:
#移除 p1 物件：
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
#del p1
#print(p1)
#NameError: name 'p1' is not defined

print("--------------------The pass Statement pass陳述式")
#The pass Statement pass陳述式
#class definitions cannot be empty, but if you for some 
# reason have a class definition with no content, put in 
# the pass statement to avoid getting an error.
#類定義不能是空的，但是如果您由於某些原因沒有內容的類定義，
# 請放在pass statement中以避免出錯。
class Person:
  pass
# having an empty class definition like this, would raise 
# an error without the pass statement