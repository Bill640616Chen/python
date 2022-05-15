#https://www.w3schools.com/python/numpy/numpy_ufunc_summations.asp
#NumPy Summations 加總
#Summations 加總
#What is the difference between summation and addition?
#加總和加法的差異是什麼?
#Addition is done between two arguments whereas summation happens over n elements.
#在兩個參數之間進行加法，而加總發生在 n個 元素上。
#Add the values in arr1 to the values in arr2:
print("----------add(arr1, arr2)--對陣列1及陣列2相加")
#對陣列1及陣列2相加
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.add(arr1, arr2)
print(newarr) #[2 4 6]

print("----------sum(arr1, arr2)--對陣列1及陣列2加總")
#Sum the values in arr1 and the values in arr2:
#對陣列1及陣列2加總
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr) #12

print("-------------------------------軸上的總和")
#Summation Over an Axis 軸上的總和
#If you specify axis=1, NumPy will sum the numbers in each array.
#如果您指定軸+1，NumPy 將匯總每個陣列中的數字。
#Perform summation in the following array over 1st axis:
#在以下陣列中對第 1 軸進行總結：
import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr) #[6 6]

print("---------------------------------累積總和")
#Cummulative Sum 累積總和
#Cummulative sum means partially adding the elements in array.
#累積和意味著在陣列中部分添加元素。
#E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
#[1、2、3、4] 的部分總和為 [1、1+2、1+2+3、1+2+3+4] = [1、3、6、10] 。
#Perfom partial sum with the cumsum() function.
#用cumsum()函數演算部分總和
#Perform cummulative summation in the following array:
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr) #[1 3 6]