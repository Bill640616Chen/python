#https://www.w3schools.com/python/scipy/scipy_sparse_data.php
#SciPy Sparse Data SciPy稀疏數據
#What is Sparse Data 什麼是稀疏數據
#Sparse data is data that has mostly unused elements (elements that don't carry any information ).
#稀疏的數據大多具有未使用的元素（不攜帶任何資訊的元素）。
#It can be an array like this one:
#它可以是這樣的陣列：
#[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
#Sparse Data: is a data set where most of the item values are zero.
#稀疏數據：是大多數專案值為零的數據集。
#Dense Array: is the opposite of a sparse array: most of the values are not zero.
#密集陣列：與稀疏陣列相反：大多數值不是零。
#In scientific computing, when we are dealing with partial derivatives in linear algebra we will come across sparse data.
#在科學計算中，當我們處理線性代數中的部分衍生物時，我們會遇到稀疏的數據。

#How to Work With Sparse Data 如何處理稀疏的數據
#SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
#SciPy 有一個模組， scipy.sparse， 提供處理稀疏數據的功能。
#There are primarily two types of sparse matrices that we use:
#我們主要使用兩種類型的稀疏矩陣：
#CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
#CSC - 壓縮稀疏欄。對於高效的算術，快速列切片。
#CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products
#CSR - 壓縮稀疏列。對於快速行切片，更快的矩陣向量產品
#We will use the CSR matrix in this tutorial.
#我們將在此教程中使用 CSR 矩陣。
#CSR Matrix CSR矩陣
#We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().
#我們可以通過將arry傳遞到函數scipy.sparse.csr_matrix()來創建CSR矩陣。

print("-----------csr_matrix(arr)-從陣列建立 CSR 矩陣")
#Create a CSR matrix from an array:
#從陣列建立 CSR 矩陣：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
#切出的是索引值,每列後面是讓索引位置的值
'''
From the result we can see that there are 3 items with value.
從結果中我們可以看到，有3個項目的價值。
The 1. item is in row 0 position 5 and has the value 1.
The 2. item is in row 0 position 6 and has the value 1.
The 3. item is in row 0 position 8 and has the value 2.
'''

print("------csr_matrix(arr).data-稀疏矩陣方法")
#Sparse Matrix Methods 稀疏矩陣方法
#Viewing stored data (not the zero items) with the data property:
#檢視資料屬性的儲存資料（不是零項）：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)

print("------csr_matrix(arr).count_nonzero()")
#Counting nonzeros with the count_nonzero() method:
#使用count_nonzero（）方法計算非零個數：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).count_nonzero())

print("------eliminate_zeros從矩陣中移除零條目")
#Removing zero-entries from the matrix with the eliminate_zeros() method:
#使用eliminate_zeros（） 方法從矩陣中消除零條目：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

print("-------sum_duplicates()方法消除重複項目")
#Eliminating duplicate entries with the sum_duplicates() method:
#使用sum_duplicates()方法消除重複項目：
#Eliminating duplicates by adding them:
#透過新增它們來消除重複：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)

print("-------使用tocsc()方法從 csr 轉換為 csc")
#Converting from csr to csc with the tocsc() method:
#使用tocsc()方法從 csr 轉換為 csc：
import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()
print(newarr)
#Note: Apart from the mentioned sparse specific operations, sparse matrices support all of the operations that normal matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.
#注意：除了上述稀疏的特定操作外，稀疏矩陣支援所有正常矩陣支援的業務，如重塑、總結、算術、廣播等。
print("-------使用tocsr()方法從 csc 轉換為 csr")
import numpy as np
from scipy.sparse import csc_matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csc_matrix(arr).tocsr()
print(newarr)