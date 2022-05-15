#https://www.w3schools.com/python/ref_list_extend.asp
#Python List List extend() Method 清單擴展方法
#Add the elements of cars to the fruits list:
#extend不是把清單當一個元素,而是把清單裡的元素一個一個加入
print("-----------------------用extend方法,清單加入清單")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

print("-----------------------用extend方法,tuple加入list")
#Definition and Usage
#The extend() method adds the specified list elements (or any iterable)
# to the end of the current list.
#extend()方法將指定的清單元素（或任何可迭代）添加到當前清單的末尾。
#Syntax
#list.extend(iterable)(可迭代)
#Parameter Values
#Parameter(參數)：Description(描述)
#iterable(可迭代)：Required(必填). Any iterable (list, set, tuple, etc.)
#Add a tuple to the fruits list:把tuple加到list
fruits = ['apple', 'banana', 'cherry'] #list
points = (1, 4, 5, 9) #tuple
fruits.extend(points)
print(fruits) #['apple', 'banana', 'cherry', 1, 4, 5, 9]
print(fruits.extend(points)) #None
#當為None,但是有in-place,必須用print(變數 + 變數)才會有值
print(tuple(fruits) + points)
#有in-place,兩個變數必須是相同型別才能相+
print(fruits + points)
#can only concatenate list (not "tuple") to list  
fruits = ['apple', 'banana', 'cherry'] #list
points = (1, 4, 5, 9) #tuple
points.extend(fruits) #extend為白色,代表tuple沒有這個屬性
print(points) #'tuple' object has no attribute 'extend'
#我想我知道了,因為tuple的內容不可變,所以沒有辦去extend把list加進來
#要如何知道一個物件有什麼屬性?
#真正的答案在於理解 Python 類屬性和 Python 實例屬性之間的區別。
