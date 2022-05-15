#https://www.w3schools.com/python/ref_list_count.asp
#Python List List count() Method 清單計算次數方法
#Return the number of times the value "cherry" appears in the fruits list:
#傳回水果清單中顯示值「櫻桃」的次數：
fruits = ["apple", "banana", "cherry"]
x = fruits.count("cherry")
print(x) #1
#Definition and Usage
#The count() method returns the number of elements with the specified value.
#Syntax
#list.count(value) (value)裡的參數值
#Parameter Values
#Parameter(參數)：Description(描述)
#value(值)：Required(必填). Any type (string, number, list, tuple, etc.)
# The value to search for.
#Return the number of times the value 9 appears int the list:
fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x) #2