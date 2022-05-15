#https://www.w3schools.com/python/numpy/numpy_array_search.asp
#NumPy Searching Arrays 陣列搜索
#Searching Arrays 搜索陣列
#You can search an array for a certain value, and return the indexes that get a match.
#您可以在陣列中搜索（檢索）某個值，然後返回獲得匹配的索引。
#To search an array, use the where() method.
#要搜索陣列，請使用 where（） 方法。
#Find the indexes where the value is 4:
print("----------where(arr == 4)---尋找值為 4 的索引位置值")
#尋找值為 4 的索引位置值：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) #(array([3, 5, 6], dtype=int64),)
#The example above will return a tuple: (array([3, 5, 6],)
#上例會返回一個元組：（array（[3， 5， 6]，）
#Which means that the value 4 is present at index 3, 5, and 6.
#意思就是值 4 出現在索引 3、5 和 6。
#Find the indexes where the values are even:
print("----------where(arr%2 == 0)---尋找值為偶數的索引")
#尋找值為偶數的索引：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
#x取array裡的值在(arr%2 == 0)做運算
print(x)
#Find the indexes where the values are odd:
print("----------where(arr%2 == 1)---尋找值為奇數的索引")
#尋找值為奇數的索引：
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

print("-------------------------Search Sorted 搜索排序")
#Search Sorted 搜索排序(傳回指定值索引位置的值)
#預設搜尋從左到右
#There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#有一個名為 searchsorted（） 的方法，該方法在陣列中執行二進位搜索，並返回將在其中插入指定值以維持搜尋順序的索引。
#The searchsorted() method is assumed to be used on sorted arrays.
#假定 searchsorted（） 方法用於排序數位。
#Find the indexes where the value 7 should be inserted:
#尋找應在其中插入值 7 的索引：
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
#Example explained: The number 7 should be inserted on index 1 to remain the sort order.
#例子解釋：應該在索引 1 上插入數位 7，以保持排序順序。
#The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
#該方法從左側開始搜索，並返回第一個索引，其中數位7不再大於下一個值。

print("-----------Search From the Right Side 從右側搜索")
#Search From the Right Side 從右側搜索(傳回指定值索引位置的值)
#By default the left most index is returned, but we can give side='right' to return the right most index instead.
#默認情況下，返回最左邊的索引，但是我們可以給定 side='right'，以返回最右邊的索引。
#Find the indexes where the value 7 should be inserted, starting from the right:
#從右邊開始尋找應該插入值 7 的索引：
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
#索引值永遠是左到右、上到下。把7插在陣列的right side,
# 所以索引位置是2
#用法： numpy.searchsorted(arr, num, side=’left’, sorter=None)
'''
參數：
arr :[陣列]輸入陣列。如果sorter為None，則必須按升序對其進行排序，
否則sorter必須是對其進行排序的索引陣列。
num :[陣列]我們要插入到arr中的值。
side :['left'，'right']，可選。如果為“ left”，則給出找到的第一
個合適位置的索引。如果為“正確”，則返回上一個這樣的索引。如果沒有
合適的索引，則返回0或N(其中N是a的長度)。
num :[陣列，可選]整數索引陣列，將陣列a升序排列。它們通常是argsort的結果。
Return :[索引]，與num形狀相同的插入點陣列。
'''
print(x)
print("----測試1---Search From the Right Side 從右側搜索")
import numpy as np
arr = np.array([6, 7, 8, 9,13])
x = np.searchsorted(arr, [5,8,9,10,11,12,15,16], side='right')
#索引值永遠是左到右、上到下。把值插在陣列元素的right side
#(5)6,7,8,(8)9,(9)(10)(11)(12)13,(15)(16)
#(5)<6,只能放左邊,(8)放在8的右邊9字的位罝,(9)也是,
# (10)(11)(12)<13只能放在13的位置,(15)(16)>13
#如果沒有合適的索引，則返回0或N(其中N是a的長度)。
print(x) #[0 3 4 4 4 4 5 5]
print("----測試2---Search From the left Side 從左側搜索")
#把要索引陣列的元素放入原始陣列元素的左邊
#比如(8)放在原始8的左邊,(9)也是,(10)(11)(12)<13,(15)(16)>13
import numpy as np
arr = np.array([6, 7, 8, 9,13])
x = np.searchsorted(arr, [5,8,9,10,11,12,15,16], side='left')
#索引值永遠是左到右、上到下。把值插在陣列元素的right side
#(5)6,7,(8)8,(9)9,(10)(11)(12)13,(15)(16)
#如果沒有合適的索引，則返回0或N(其中N是a的長度)。
print(x) #[0 2 3 4 4 4 5 5]
print("----測試3---Search From the Right Side 從右側搜索")
import numpy as np
arr = np.array([1,2,3,4])
x = np.searchsorted(arr,3, side='right')
#1,2,3,(3)4
print(x) #3
#白話翻譯是你搜尋的3要插入arr陣列中3的前面(left)，
# 還是arr陣列中3的後面(right)。所以left會回傳索引值2，
# right會回傳索引值3。
print("----測試3---Search From the Right Side 從右側搜索")
import numpy as np
arr = np.array([1,2,3,4])
x = np.searchsorted(arr,3, side='left')
#1,2,(3)3,4
print(x) #2
#Example explained: The number 7 should be inserted on index 2 to remain the sort order.
#例子解釋：應該在索引 2 上插入數位 7，以保持排序順序。
#The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.
#該方法從右邊開始搜索，並返回第一個索引，其中數位7不再小於下一個值。

print("---------------------------Multiple Values 多個值")
#Multiple Values 多個值
#To search for more than one value, use an array with the specified values.
#要搜索多個值，請使用擁有指定值的陣列。
#Find the indexes where the values 2, 4, and 6 should be inserted:
#尋找應在其中插入值 2、4 和 6 的索引：
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
#1,(2)3,(4)5,(6)7
print(x) #[1 2 3]索引位置
#The return value is an array: [1 2 3] containing the three 
# indexes where 2, 4, 6 would be inserted in the original 
# array to maintain the order.
#返回值是一個陣列：[1 2 3] 包含三個索引，其中將在原始陣列中
# 插入 2、4、6 以維持順序。

