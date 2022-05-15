#https://www.w3schools.com/python/numpy/numpy_ufunc_products.asp
#NumPy Products 乘積
#To find the product of the elements in an array, use the prod() function.
#找到陣列裡的元素的乘積,使用prod()函數
#Find the product of the elements of this array:
print("-------------------------找到陣列裡元素的乘積")
#找到陣列裡元素的乘積
import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x) #24,because 1*2*3*4 = 24

print("------------------------找到2陣列裡元素的乘積")
#Find the product of the elements of two arrays:
#找到2個陣列裡元素的乘積
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x) #40320,because 1*2*3*4*5*6*7*8 = 40320

print("------------------------------在軸上的乘積")
#Product Over an Axis 在軸上的乘積
#If you specify axis=1, NumPy will return the product of each array.
#如果您指定軸+1，NumPy 將返回每個陣列的乘積。
#Perform summation in the following array over 1st axis:
#在以下陣列中對第 1 軸進行加總：
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr) #[  24 1680]

print("---------------------------------累積乘積")
#Cummulative Product 累積乘積
#Cummulative product means taking the product partially.
#累積乘積意味著部分獲取乘積。
#E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
#例如，[1，2，3，4] 的部分乘積是 [1， 1*2， 1*2*3， 1*2*3*4] = [1， 2， 6， 24]
#Perfom partial sum with the cumprod() function.
#用cumprod()函數演算部分加總
#Take cummulative product of all elements for following array:
#採取以下陣列的所有元素的累積乘積：
import numpy as np
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr) #[   5   30  210 1680]