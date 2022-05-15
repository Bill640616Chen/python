#https://www.w3schools.com/python/ref_list_pop.asp
#Python List pop() Method 清單指定位置移除元素方法
#Removes the element at the specified position
#Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) #(索引位置)
print(fruits) #['apple', 'cherry']
#Definition and Usage
#The pop() method removes the element at the specified position.

print("-----------x = fruits.pop() #移除的元素傳回x,()預設值為1")
#Syntax
#list.pop(pos) (pos)
#()預設值為-1,負數是由最右邊-1往左邊數,同時會傳回最後一個項目
#Parameter Values
#Parameter(參數)：Description(描述)
#pos(指定位置移除元素)：Optional. A number specifying the position of the element you want to remove, default value is -1, which returns the last item
#Return the removed element:傳回移除的元素
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop() #移除的元素傳回x
print(x) #cherry
print(fruits) #['apple', 'banana']
#Remove and return item at index (default last).
#在索引上刪除和返回項目（預設是最後一個）
#Raises IndexError if list is empty or index is out of range.
#如果是空清單或者索引超出範圍,則會提高索引錯誤
print("------------------------x = fruits.pop(2)傳回移除的元素 #")
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(2)
print(x) #cherry
print("----------不用設變數---print(fruits.pop(2))傳回移除的元素 #")
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(2)) #cherry
#Note: The pop(),(在索引的範圍內) method returns removed value.
#如果超出範圍或空清單,會出現pop index out of range
#fruits = ['apple', 'banana', 'cherry']
#print(fruits.pop(3))
#IndexError: pop index out of range
#fruits = ['apple', 'banana', 'cherry']
#fruits.clear()
#print(fruits.pop())
#IndexError: pop from empty list