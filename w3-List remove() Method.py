#https://www.w3schools.com/python/ref_list_remove.asp
#Python List remove() Method 清單移除指定元素方法
#Removes the first item with the specified value
#Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits) #['apple', 'cherry']
#Definition and Usage
#The remove() method removes the first occurrence of the element with the specified value.

print("----------------------------None的資料還在記憶體的測試")
#Syntax
#list.remove(elmnt)
#()裡不能沒有元素,fruits.remove()
#TypeError: list.remove() takes exactly one argument (0 given)
#Parameter Values
#Parameter	Description
#elmnt(元素)：Required(必填). Any type (string, number, list etc.) The element you want to remove
fruits = ['apple', 'banana', 'cherry']
a = ['apple', 'banana',]
print(fruits.remove("banana")) #None
print(a.extend(fruits)) #None
print(a+fruits) #只要輸出none的代表在記憶體都有資料
#['apple', 'banana', 'apple', 'cherry', 'apple', 'cherry']
fruits = ['apple', 'banana', 'cherry']
a = ['apple', 'banana',]
