#https://www.w3schools.com/python/numpy/numpy_ufunc_set_operations.asp
#NumPy Set Operations 集合操作
#What is a Set 什麼是集合
#A set in mathematics is a collection of unique elements.
#數學集是獨特的集合。
#Sets are used for operations involving frequent intersection, union and difference operations.
#集合被使用於操作涉及頻繁交叉、聯合和差額操作。
#Create Sets in NumPy 在 NumPy 中創建集合
#We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
#我們可以使用 NumPy 的獨特 （） 方法從任何陣列中尋找唯一元素。例如，創建一個設置陣列，但請記住，設置的陣列只能是 1D 陣列。
#Convert following array with repeated elements to a set:
print("-------------將具有重複元素的以下陣列轉換為一組")
#將具有重複元素的以下陣列轉換為一組：
import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
#unique()找獨特的值,只能一個陣列

print("-------------------------------------查找聯合")
#Finding Union 查找聯合
#To find the unique values of two arrays, use the union1d() method.
#要查找兩個陣列的獨特值，請使用union1d()方法。
#Find union of the following two set arrays:
#尋找以下兩個設置陣列的聯合：
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
#union1d找獨特的值,可以N的陣列

print("-----------------------------------查找交叉點")
#Finding Intersection 查找交叉點
#To find only the values that are present in both arrays, use the intersect1d() method.
#要僅找到兩個陣列中存在的值，請使用相交 intersect1d() 方法。
#Find intersection of the following two set arrays:
#尋找以下兩個設定陣列的交集：
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr) #[3 4]
#Note: the intersect1d() method takes an optional 
# argument assume_unique, which if set to True can 
# speed up computation. It should always be set to 
# True when dealing with sets.
#注意：相交intersect1d()方法assume_unique需要可選的
# 參數，如果設置為 True 可以加快計算速度。在處理集時，
# 應始終將其設置為真實。

print("-------------------------------------查找差異")
#Finding Difference 查找差異
#To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
#查找第一個集合的值,不存在第二個集合,使用setdiff1d() method
#Find the difference of the set1 from set2:
#找出第一個集合與第二集合的差異
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
#Note: the setdiff1d() method takes an optional 
# argument assume_unique, which if set to True 
# can speed up computation. It should always be 
# set to True when dealing with sets.
#the setdiff1d()取自選的參數"假設_獨特",如果集合
# 是True,可以加速運算,在處理集時，應始終將其設置為真實。

print("--------------------------------查找對稱差異")
#Finding Symmetric Difference 查找對稱差異
#To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
#要僅查找兩組中不存在的值，請使用 setxor1d（）方法。
#Find the symmetric difference of the set1 and set2:
#尋找集 1 和 set2 的對稱差異：
import numpy as np
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)
#Note: the setxor1d() method takes an optional 
# argument assume_unique, which if set to True 
# can speed up computation. It should always be 
# set to True when dealing with sets.
#注意：setxor1d（） 方法assume_unique需要可選的參數，
# 如果設置為 True 可以加快計算速度。在處理集時，應始終
# 將其設置為真實。

