#https://www.w3schools.com/python/ref_func_type.asp
#Python type() Function Python type()函數
#返回物件的類型。
#Return the type of these objects:
#傳回這些物件的類型：
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33
x = type(a)
y = type(b)
z = type(c)
print(x,y,z,sep='\\')
#Definition and Usage 定義和用法
#The type() function returns the type of the specified object
#type（） 函數傳回指定物件的類型。
#Syntax 語法
#type(object, bases, dict)
#Parameter參數：Values值
#Parameter參數：Description描述
#object：Required. If only one parameter is specified, the type() function returns the type of this object
#object：必需。 如果僅設置一個參數，則 type（） 函數將返回此物件的類型。
#bases：Optional. Specifies the base classes
#bases：可選。 規定基類。
#dict：Optional. Specifies the namespace with the definition for the class
#dict：可選。 規定帶有類定義的名稱空間。