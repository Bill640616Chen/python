#https://www.w3schools.com/python/gloss_python_array_methods.asp
#Array Methods 陣列方法
#Python has a set of built-in methods that you can use on lists/arrays.
#Python 有一套內置方法，您可以在清單/陣列上使用。
#append()	Adds an element at the end of the list
#在清單裡最後面添加一個元素
#https://www.w3schools.com/python/ref_list_append.asp
#在清單末尾添加元素
#Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits) #['apple', 'banana', 'cherry', 'orange']
#Definition and Usage
#The append() method appends an element to the end of the list.
#Syntax
#list.append(elmnt)
#Parameter：Description
#elmnt：Required. An element of any type(型別)
#  (string, number, object(物件) etc.)
print("------------------測試Add 2 list to a list:")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = ["Ford", "BMW"]
b.append(c) #先把c放進b
a.append(b) #再把新b放進a
print(a)
#['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo', ['Ford', 'BMW']]]     
print("-----測試輸出為None時,用in-place把值輸出 測試 a.append(b.append(c))")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = ["Ford", "BMW"]
a.append(b.append(c)) #b.append(c)為None
print(a)
#['apple', 'banana', 'cherry', None]
print(a+b+c)
#print(a)====a變成['apple', 'banana', 'cherry', None]
#b.append(c)====b變成['Ford', 'BMW', 'Volvo',['Ford', 'BMW']]
#c還是'Ford', 'BMW'
#['apple', 'banana', 'cherry', None, 'Ford', 'BMW', 'Volvo',
# ['Ford', 'BMW'], 'Ford', 'BMW']
print("---------測試輸出為None時,用in-place把值輸出 print(a.append(b))")
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
print(a.append(b)) #None
print(a+b)
#a.append(b)====a變成['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']
#b還是"Ford", "BMW", "Volvo"
#['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo'],
#  'Ford', 'BMW', 'Volvo']

#clear()：Removes all the elements from the list
#clear()：移除清單裡所有元素
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
print(fruits) #set()
print("-----------用來印證print(fruits.update()) #None，有沒有in place")
fruits1 = {"orange","mango"}
print(fruits.update(fruits1)) #None,有in place
print(fruits)
print(fruits1)
print(list(fruits)+list(fruits1)) #把set轉換成list就可以取in place的值
fruits.update(fruits1)
print(fruits) #{'mango', 'orange'}
#不是所有的None都有in place耶
fruits = {}
print(fruits) #{}

#copy()	Returns a copy of the list
#傳回清單的副本
#https://www.w3schools.com/python/ref_list_copy.asp
#Python List List copy() Method 清單複製方法
#Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x) #['apple', 'banana', 'cherry']
#Definition and Usage
#The copy() method returns a copy of the specified list.
#Syntax
#list.copy()
#Parameter Values
#No parameters ()裡沒參數

#count()	Returns the number of elements with the specified value
#傳回指定值的元素的數量
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

#extend()	Add the elements of a list (or any iterable), to the end of the current list
#添加清單(或是任何可迭代)裡的元素到另一個清單的後面
#https://www.w3schools.com/python/ref_list_extend.asp
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
#print(fruits + points)
#can only concatenate list (not "tuple") to list  
fruits = ['apple', 'banana', 'cherry'] #list
points = (1, 4, 5, 9) #tuple
#points.extend(fruits) #extend為白色,代表tuple沒有這個屬性
print(points) #'tuple' object has no attribute 'extend'
#我想我知道了,因為tuple的內容不可變,所以沒有辦去extend把list加進來
#要如何知道一個物件有什麼屬性?
#真正的答案在於理解 Python 類屬性和 Python 實例屬性之間的區別。

#index()	Returns the index of the first element with the specified value
#傳回第一個元素指定值的索引
#https://www.w3schools.com/python/ref_list_index.asp
#Python List List index() Method 清單索引方法
#What is the position of the value "cherry":
#value「櫻桃」的位置是什麼？
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x) #索引位置為2
#Definition and Usage
#The index() method returns the position at the first occurrence of the specified value.
#Syntax
#list.index(elmnt)(元素)
#Parameter：Values
#Parameter(參數)：Description(描述)
#elmnt(元素)：Required(必填). Any type (string, number, list, etc.).
# The element to search for
#What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
print(fruits.index(32)) #都是從左往右點,所以32在位置3
#Note: The index() method only returns the first occurrence of the value.

print("------------------------------在指定的位值添加一個元素")
#insert()	Adds an element at the specified position
#在指定的位值添加一個元素
#https://www.w3schools.com/python/ref_list_insert.asp
#Python List insert() Method 清單指定位置插入元素方法
#Insert the value "orange" as the second element of the fruit list:
#在清單中的第二個元素插入orange值,第二元素的位置為1
fruits = ['apple', 'banana', 'cherry']
fruits.insert(-1, "orange")
print(fruits.insert(0,'grape')) #none,在in-placel裡
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

print("------------------------------------在指定位置移除元素")
#pop()	Removes the element at the specified position
#在指定位置移除元素
#https://www.w3schools.com/python/ref_list_pop.asp
#Python List pop() Method 清單指定位置移除元素方法
#Removes the element at the specified position
#Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1) #(索引位置)
print(fruits) #['apple', 'cherry']
#Definition and Usage
#The pop() method removes the element at the specified position.
print("-----------x = fruits.pop() #移除的元素傳回x,()預設值為-1")
#Syntax
#list.pop(pos) (索引位置)
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
print("----------不用設變數---print(fruits.pop())傳回移除的元素 #")
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop()) #cherry
#Note: The pop(),(在索引的範圍內) method returns removed value.
#如果超出範圍或空清單,會出現pop index out of range
#fruits = ['apple', 'banana', 'cherry']
#print(fruits.pop(3))
#IndexError: pop index out of range
#fruits = ['apple', 'banana', 'cherry']
#fruits.clear()
#print(fruits.pop())
#IndexError: pop from empty list

print("--------------------------------移除第一個項目的指定值")
#remove()	Removes the first item with the specified value
#移除第一個項目的指定值
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

print("------------------------------------反轉清單內容的順序")
#reverse()	Reverses the order of the list
#反轉清單內容的順序
#https://www.w3schools.com/python/ref_list_reverse.asp
#Python List reverse() Method 反轉清單順序方法
#Reverses the order of the list 反轉清單順序
#Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) #['cherry', 'banana', 'apple']
#Definition and Usage
#The reverse() method reverses the sorting order of the elements.
print(fruits.reverse()) #None
print(fruits) #列印in-place
#() -> None
#Reverse *IN PLACE*
#Syntax
#list.reverse() ()裡沒參數
#Parameter Values
#No parameters
#https://www.w3schools.com/python/ref_func_reversed.asp
#Python reversed() Function 函數
#Reverse the sequence of a list, and print each item:
#反轉清單的順序，列印每個項目：
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
#Definition and Usage
#The reversed() function returns a reversed iterator object.
#reversed()函數傳回反轉的可迭代物件。
#Syntax
#reversed(sequence)(序列)
#Parameter Values
#Parameter：Description
#sequence：Required. Any iterable object任何可迭代物件
#reversed()
#(class) reversed
#Return a reverse iterator over the values of the given sequence.
#傳回反轉迭代器超過給定序列的值。

print("-------------------排序清單")
#sort()	Sorts the list
#排序清單
#https://www.w3schools.com/python/ref_list_sort.asp
#Python List sort() Method 對清單進行排序方法
#對清單進行排序
print("-------------------sort elenmant順序測試")
#Sort the list alphabetically:
#按照字母排序
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) #['BMW', 'Ford', 'Volvo']
print("-------------------sort Ab大小寫的順序測試")
cars = ['a', 'A', 'b','C']
cars.sort()
print(cars) #['A', 'C', 'a', 'b']先排大寫再排小寫
print("-------------------sort 負數與整數的順序測試")
cars = ['-3', '-5', '-1','-6','0']
cars.sort()
print(cars) #['-1', '-3', '-5', '-6', '0']在負數裡0放最後
print("-------------------sort 負數與整數的順序測試")
cars = ['2', '1', '0','5']
cars1 = ['-3','-1','-6','0']
cars.sort()
print(cars) #['0', '1', '2', '5'] 
print(cars.sort()) #None測試,皆為就地變值in-place
print(cars1.sort()) #None測試,皆為就地變值in-place
print(cars+cars1) #['0', '1', '2', '5', '-1', '-3', '-6', '0']
#Definition and Usage
#The sort() method sorts the list ascending by default.
#預設的sort()方法,按照上升的方式排序清單
#例：[6,3,5]-->[3,5,6],abc亦同,先排大寫再排小寫
print("------------reverse您還可以做一個函數來決定排序標準")
#You can also make a function to decide the sorting criteria(s).
#您還可以做一個函數來決定排序標準。
#Syntax
#list.sort(reverse=True|False, key=myFunc)
#sort的參數專用關鍵字key,不能更改,keyword argument for sort()
#當語法參數為自選時,代表參數非必填
#Parameter Values
#Parameter(參數)：Description(描述)
#reverse(反轉)：Optional(自選). 
#reverse=True will sort the list descending. Default is reverse=False
#key(key功能)：Optional(自選).
#A function to specify the sorting criteria(s)
#Sort the list descending:降幂排列
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
print("------------key=myFunc您還可以自訂函數來決定排序標準(此例為len)")
# A function that returns the length of the value:
#按照字串的長度排序的功能
def myFunc(e):
  return len(e)
#上面定義了一個功能函數,用來測量字串的長度
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
#key(key: (_p0: str) -> SupportsLessThan)=myFunc(傳回清單裡字串長度)
#每測量完一個字串就把值丟給key,然後key就執行SupportsLessThan(從最小值開始)
#所以字串最短的就傳回給cars
print(cars) #['VW', 'BMW', 'Ford', 'Mitsubishi']

print("------------key=myFunc您還可以自訂函數來決定排序標準(此例為傳回值)")
#Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
#key(key: (_p0: str) -> SupportsLessThan)=myFunc(傳回清單指定鍵的值)
#每傳完一個鍵就把值丟給key,然後key就執行SupportsLessThan(從最小值開始)
#所以最小值產生的鍵值的就傳回給cars
print(cars)

print("------------list.sort(reverse=True|False, key=myFunc())")
#Sort the list by the length of the values and reversed:

# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
#key=myFunc(測量字串的長度)本來按照長度排['VW', 'BMW', 'Ford', 'Mitsubishi']
#然後再執行reverse=True,把key=myFunc輸出的清單,反序排列
#['Mitsubishi', 'Ford', 'BMW', 'VW']
print(cars)

#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#注意：Python 沒有對陣列的內置支援，但 Python 清單可以改為使用。

#Related Pages 相關頁面
#Python Array Tutorial Python 陣列教程
#https://www.w3schools.com/python/python_arrays.asp
#Array 陣列
#https://www.w3schools.com/python/gloss_python_array.asp
#What is an Array 什麼是陣列
#https://www.w3schools.com/python/gloss_python_arrray_what_is.asp
#Access Arrays 訪問陣列
#https://www.w3schools.com/python/gloss_python_array_access.asp
#Array Length 陣列長度
#https://www.w3schools.com/python/gloss_python_array_length.asp
#Looping Array Elements 迴圈陣列元件
#https://www.w3schools.com/python/gloss_python_array_loop.asp
#Add Array Element 添加陣列元素
#https://www.w3schools.com/python/gloss_python_array_add.asp
#Remove Array Element 刪除陣列元素
#https://www.w3schools.com/python/gloss_python_array_remove.asp
