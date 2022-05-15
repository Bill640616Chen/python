#https://www.w3schools.com/python/ref_set_clear.asp
#Python Set clear() Method 集合clear()方法
#Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear() #清除所有元素後,輸出自動判斷為資料類型為set(),而不是{}
print(fruits) #set()
#Definition and Usage
#The clear() method removes all elements in a set.

#Syntax
#set.clear() ()內無參數
#Parameter Values
#No parameters
fruits = {"apple", "banana", "cherry"}
print(fruits.clear()) #None,沒有in place
print("-----------用來印證print(fruits.update()) #None，有沒有in place")
fruits1 = {"orange","mango"}
print(fruits.update(fruits1)) #None,有in place
print(list(fruits)+list(fruits1)) #把set轉換成list就可以取in place的值
fruits.update(fruits1)
print(fruits) #{'mango', 'orange'}
#不是所有的None都有in place耶
fruits = {}
print(fruits) #{}
