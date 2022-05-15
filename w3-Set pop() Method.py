#https://www.w3schools.com/python/ref_set_pop.asp
#Python Set pop() Method 集合pop() 方法
#Removes an element from the set
#從集合裡移除一個元素
#Remove a random item from the set:
#隨機從集合裡移除一個項目
fruits = {"apple", "banana", "cherry"}
fruits.pop() #在集合裡隨機移除一個
print(fruits) #{'cherry', 'banana'}
print(fruits.pop()) #直接隨機在集合取一個值傳回,cherry
#Definition and Usage
#The pop() method removes a random item from the set.
#This method returns the removed item.
#Syntax
#set.pop() ()裡禁用參數
#Parameter Values
#No parameter values.
#Return the removed element:隨機移除元素
fruits = {"apple", "banana", "cherry"}
x = fruits.pop() #移除的元素賦值給x,相當於print(fruits.pop())
print(x) #apple
#Note: The pop() method returns removed value.
