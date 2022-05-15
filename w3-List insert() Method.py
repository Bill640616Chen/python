#https://www.w3schools.com/python/ref_list_insert.asp
#Python List insert() Method 清單指定位置插入元素方法
#Insert the value "orange" as the second element of the fruit list:
#在清單中的第二個元素插入orange值,第二元素的位置為1
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits) #['apple', 'orange', 'banana', 'cherry']
#插入都是在原位置之前
#Definition and Usage
#The insert() method inserts the specified value at the specified position.

#Syntax
#list.insert(pos, elmnt)(位置, 元素)
#Parameter Values
#Parameter(參數)	Description(描述)
#pos(位置)：Required(必填). A number specifying in which position to insert the value
#elmnt(元素)：Required(必填). An element of any type (string, number, object etc.)
