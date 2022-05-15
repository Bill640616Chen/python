#https://www.w3schools.com/python/python_arrays.asp
#Python Arrays 陣列
#Note: Python does not have built-in support for Arrays, 
# but Python Lists can be used instead.
#注意：Python 沒有陣列的內建支援，但可以改用 Python 清單。
#Arrays 陣列
#Note: This page shows you how to use LISTS as ARRAYS, 
# however, to work with arrays in Python you will have to 
# import a library, like the NumPy library.
#注意：此頁面顯示如何使用清單作為ARRAYS，但是，要與 Python 
# 中的陣列配合使用，您必須導入庫，如 NumPy 庫。
#Arrays are used to store multiple values in one single 
# variable:
#陣列用於在一個變數中存儲多個值：
#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
#What is an Array? 什麼是陣列？
#An array is a special variable, which can hold more than 
# one value at a time.
#陣列是一種特殊的變數，一次可容納多個值。
#If you have a list of items (a list of car names, for 
# example), storing the cars in single variables could look 
# like this:
#如果您有項目清單（例如，汽車名稱清單），將汽車存儲在單個變數中
# 可能看起來像這樣
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
#However, what if you want to loop through the cars and 
# find a specific one? And what if you had not 3 cars, 
# but 300?
#但是，如果您想在汽車中迴圈並找到特定的汽車，該怎麼辦？如果你
# 沒有3輛車，而是300輛呢？
#The solution is an array!
#解決方案是一個陣列！
#An array can hold many values under a single name, and 
# you can access the values by referring to an index number.
#陣列可以在單個名稱下保留許多值，並且您可以通過引用索引號來訪問值。

#Access the Elements of an Array 訪問陣列的元素
#You refer to an array element by referring to the index number.
#您透過引用索引編號來引用陣列元素。
#Get the value of the first array item:
#取得第一個陣列項目的價值：
x = cars[0] #[]索引用括號,0為list中的第一個項目
#Modify the value of the first array item:
#可以修改陣列項目的值
cars[0] = "Toyota"

#The Length of an Array 陣列的長度
#Use the len() method to return the length of an array 
# (the number of elements in an array).
#使用 len（） 方法傳回陣列的長度（陣列中的元素數）。
#Return the number of elements in the cars array:
#傳回汽車陣列中的元素數量：
x = len(cars)
#Note: The length of an array is always one more than the highest array index.
#注意：陣列的長度總是比最高陣列索引值多1。
#例：索引0,1,2,但陣列長度為3

#Looping Array Elements 迴圈陣列元件
#You can use the for in loop to loop through all the elements of an array.
print("--------------您可以使用for in迴圈來迴圈陣列的所有元素")
#您可以使用for in迴圈來迴圈陣列的所有元素。
#Print each item in the cars array:
#在汽車陣列中列印每個項目：
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

#Adding Array Elements 添加陣列元素
#You can use the append() method to add an element to an array.
#您可以使用append（）方法向陣列添加元素。
#Add one more element to the cars array:
#在汽車陣列中再添加一個元素
cars.append("Honda") #值加在陳列的最後面,放入print時為None

#Removing Array Elements 刪除陣列元素
#You can use the pop() method to remove an element from the array.
#您可以使用 pop（）方法從陣列中刪除元素。
#Delete the second element of the cars array:
cars.pop(1) #索引1代表第二個原素,mpop可以放入print
cars.pop() #Remove and return item at index (default last).
#You can also use the remove() method to remove an element from the array.
#您也可以使用remove （） 方法從陣列中移除元素。
#Delete the element that has the value "Volvo":
cars.remove("Volvo") #放入print時為None
#()裡一定要有list裡的值,如果list裡沒有會造成錯誤
#Note: The list's remove() method only removes the first occurrence of the specified value.
#Array Methods 陣列方法
#Python has a set of built-in methods that you can use 
# on lists/arrays.
#內建的方法都在list 方法的檔案裡