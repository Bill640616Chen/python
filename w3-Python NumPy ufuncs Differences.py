#https://www.w3schools.com/python/numpy/numpy_ufunc_differences.asp
#NumPy Differences 離散差
#A discrete difference means subtracting two successive elements.
#離散的差異意味著減去連續兩個元素。
#E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
#例如，對於 [1、2、3、4]，離散差異為 [2-1、3-2、4-3] = [1、1、1]
#To find the discrete difference, use the diff() function.
#要找到離散的差異，請使用diff()函數。
#Compute discrete difference of the following array:
print("---------------------------------離散差")
#計算下列陣列的離散差異：
import numpy as np
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr) #[  5  10 -20],後面的數字往前減

print("-----diff(arr, n=2)給出參數 n 來反覆執行此操作")
#We can perform this operation repeatedly by giving parameter n.
#我們可以通過給出參數 n 來反覆執行此操作。
#E.g. for [1, 2, 3, 4], the discrete difference with 
# n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, 
# since n=2, we will do it once more, with the new 
# result: [1-1, 1-1] = [0, 0]
#例如，對於 [1， 2， 3， 4]， 與 n = 2 的離散差異將是 
# [2-1， 3-2， 4-3] = [1， 1， 1] ， 然後， 因為 n=2， 
# 我們將再次這樣做， 與新的結果： [1 - 1， 1 - 1] = 
# [0， 0]
#Compute discrete difference of the following array twice:
#計算以下陣列的離散差兩次：
import numpy as np
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
#diff(arr, n=2),n是計算次數
#Returns: [5 -30] because: 15-10=5, 25-15=10, 
# and 5-25=-20 AND 10-5=5 and -20-10=-30

