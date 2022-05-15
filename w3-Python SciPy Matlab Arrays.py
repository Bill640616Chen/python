#https://www.w3schools.com/python/scipy/scipy_matlab_arrays.php
#SciPy Matlab Arrays Matlab陣列
#Working With Matlab Arrays 與Matlab陣列工作
#We know that NumPy provides us with methods to 
# persist the data in readable formats for Python. 
# But SciPy provides us with interoperability with 
# Matlab as well.
#我們知道，NumPy 為我們提供了以可讀格式持續 Python 
# 數據的方法。但是，SciPy也為我們提供了與Matlab的互操作性。
#SciPy provides us with the module scipy.io, which 
# has functions for working with Matlab arrays.
#SciPy 為我們提供了模組 scipy.io，它具有與 Matlab 
# 陣列配合工作的函數。
#Exporting Data in Matlab Format 以 Matlab 格式輸出數據
#The savemat() function allows us to export data 
# in Matlab format.
print("------------savemat()函數允許我們以 Matlab 格式匯出數據")
#savemat()函數允許我們以 Matlab 格式匯出數據。
#The method takes the following parameters:
#該方法採用以下參數：
#filename - the file name for saving data.
#filename - 用於儲存資料的檔案名稱。
#mdict - a dictionary containing the data.
#mdict - mdict - 包含數據的字典。
#do_compression - a boolean value that specifies whether to compress the result or not. Default False.
#do_compression - 一個boolean值， 具體說明是否壓縮結果。預設錯誤。
#Export the following array as variable name "vec" to a mat file:
#將以下陣列作為變數名稱「vec」匯出到墊子檔：
from scipy import io
import numpy as np
arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})
print(arr)
#Note: The example above saves a file name "arr.mat" on your computer.
#注意：上文示例可在計算機上保存檔名"arr.mat"。
#To open the file, check out the "Import Data from Matlab Format" example below:
#要打開檔，請查看以下「來自 Matlab 格式的導入資料」範例：

#Import Data from Matlab Format 從 Matlab 格式導入數據
#The loadmat() function allows us to import data from a Matlab file.
print("------------loadmat()函數允許我們從 Matlab 檔導入數據")
#loadmat()函數允許我們從 Matlab 檔導入數據。
#The function takes one required parameter:
#該函數需要一個所需的參數：
#filename - the file name of the saved data.
#filename - 儲存資料的檔案名。
#It will return a structured array whose keys are the variable names, and the corresponding values are the variable values.
#它將返回其鍵為可變名稱的結構化陣列，相應的值是變數值。
#Import the array from following mat file.:
#從以下mat文件導入陣列。
from scipy import io
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
# Export:
io.savemat('arr.mat', {"vec": arr})
# Import:
mydata = io.loadmat('arr.mat')
print(mydata)
print("---------使用變數名稱「vec」僅顯示來自 matlab 資料的陣列")
#Use the variable name "vec" to display only the array from the matlab data:
#使用變數名稱「vec」僅顯示來自 matlab 資料的陣列：
from scipy import io
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
#Export:
io.savemat('arr.mat', {"vec": arr})
#Import:
mydata = io.loadmat('arr.mat')
print(mydata['vec'])
#Note: We can see that the array originally was 1D, but on extraction it has increased one dimension.
#注意：我們可以看到，該陣列最初是 1D，但在提取時，它增加了一個維度。
print("---------為了解決上例的1D變2D的問題,透過squeeze_me(擠壓我)=True解決")
#In order to resolve this we can pass an additional argument squeeze_me=True:
#為了解決這個問題，我們可以通過一個額外的論點squeeze_me(擠壓我)=True：
from scipy import io
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
#Export:
io.savemat('arr.mat', {"vec": arr})
#Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])