#https://www.w3schools.com/python/numpy/numpy_array_sort.asp
#NumPy Sorting Arrays 陣列排序
#Sorting Arrays 陣列排序
#Sorting means putting elements in an ordered sequence.
#排序是指將元素按有序順序排列。
#Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
#有序序列是擁有與元素相對應的順序的任何序列，例如數位或字母、升序或降序。
#The NumPy ndarray object has a function called sort(), that will sort a specified array.
#NumPy ndarray 物件有一個名為 sort（） 的函數，該函數將對指定的陣列進行排序。
#Sort the array:
print("-------------------------對陣列進行排序sort(arr)")
#對陣列進行排序：
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
#Note: This method returns a copy of the array, leaving the original array unchanged.
#註釋：此方法返回陣列的副本，而原始數位保持不變。

#You can also sort arrays of strings, or any other data type:
#您還可以對字串陣列或任何其他資料類型進行排序：
#Sort the array alphabetically:
print("-------------------------對陣列以字母順序進行排序")
#對陣列以字母順序進行排序：
import numpy as np
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
#Sort a boolean array:
print("------------------------------對布林陣列進行排序")
#對布林陣列進行排序：
import numpy as np
arr = np.array([True, False, True])
print(np.sort(arr))

print("------------------------------對 2-D 陣列排序")
#Sorting a 2-D Array 對 2-D 陣列排序
#If you use the sort() method on a 2-D array, both arrays will be sorted:
#如果在二維陣列上使用 sort（） 方法，則將對兩個陣列進行排序：
#Sort a 2-D array:
#對 2-D 陣列排序
import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
#陣列內的元素排列