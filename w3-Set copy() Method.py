#https://www.w3schools.com/python/ref_set_copy.asp
#Python Set copy() Method 集合copy()方法
#Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x) #{'cherry', 'banana', 'apple'}
print(fruits.copy()) #{'banana', 'cherry', 'apple'}
fruits.update(x)
print(fruits) #{'apple', 'cherry', 'banana'}因為值不可重複
print("---------------當游標移到屬性上時,就是出是會否傳回值,預設是none")
print(fruits.add("orange")) #預設是none
#fruits(物件).add(屬性),當游標移到屬性上時,就是出是會否傳回值
#如果最後出現None,代表不能放入print裡輸出
print("----同樣的方法(屬性)在函數裡有return,所以add放入print裡有值輸出")
def add(a,b):
    c = a + b
    return c
#函数赋值给变量
c = add(3,4)
print(c) #7
#函数返回值作为其他函数的实际参数
print(add(3,4)) #7,因為有傳回值

#Definition and Usage
#The copy() method copies the set.

#Syntax
#set.copy()
#Parameter Values
#No parameters
fruits = {"apple", "banana", "cherry"}
x = {"orange"}
fruits.update(x) #update為新增
print(fruits) #{'banana', 'cherry', 'apple', 'orange'}
