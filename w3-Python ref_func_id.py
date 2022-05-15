#https://www.w3schools.com/python/ref_func_id.asp
#Python id() Function Python id()函數
#Returns the id of an object
#返回物件的id。
#Return the unique id of a tuple object:
#傳回tuple物件的唯一 id：
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
#This value is the memory address of the object and will be different every time you run the program
#此值是物件的記憶體位址，每次運行程式時都會有所不同
#Definition and Usage 定義和用法
#The id() function returns a unique id for the specified object.
#id（） 函數傳回指定物件的唯一 id。
#All objects in Python has its own unique id.
#Python 中的所有物件都有其自己的唯一 id。
#The id is assigned to the object when it is created.
#id 在建立時已分配給物件。
#The id is the object's memory address, and will be different for each time you run the program. (except for some object that has a constant unique id, like integers from -5 to 256)
#id 是物件的記憶體位址，並且在每次運行程式時都不同。 （除了某些具有恆定唯一 id 的物件，比如 -5 到 256 之間的整數）
#Syntax
#id(object)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Any object, String, Number, List, Class etc.
#object：任何物件，字串、數位、清單等等。
