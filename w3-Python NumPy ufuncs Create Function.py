#https://www.w3schools.com/python/numpy/numpy_ufunc_create_function.asp
#Create Your Own ufunc 創建您自己的 ufunc
#How To Create Your Own ufunc 如何創建自己的 ufunc
#To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.
#要創建您自己的 ufunc，您必須定義一個函數，就像您在 Python 中使用正常功能一樣，然後使用從 Pyfunc （） 方法將其添加到您的 NumPy ufunc 庫。
#The from pyfunc() method takes the following arguments:
#從 pyfunc （） 方法採取以下參數：
#function - the name of the function.
#函數 - 函數的名稱。
#inputs - the number of input arguments (arrays).
#輸入 - 輸入參數（陣列）的數量。
#outputs - the number of output arrays.
#輸出 - 輸出陣列的數量。
#outputs只能小於inputs
#Create your own ufunc for addition:
print("--------------------建立自己的 ufunc 以供添加")
#建立自己的 ufunc 以供添加：
import numpy as np
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
#(myadd, 2, 1),(函數的名稱,輸入參數（陣列）的數量,輸出陣列的數量)

#Check if a Function is a ufunc 檢查函數是否是 ufunc
#Check the type of a function to check if it is a ufunc or not.
#檢查函數的類型，以檢查它是否是 ufunc。
#A ufunc should return <class 'numpy.ufunc'>.
#一個 ufunc 應該返回<class "numpy. ufunc" >。
#Check if a function is a ufunc:
print("--------------------檢查函數是否是 ufunc")
#檢查函數是否是 ufunc：
import numpy as np
print(type(np.add))
#If it is not a ufunc, it will return another type, like this built-in NumPy function for joining two or more arrays:
#如果它不是 ufunc， 它將返回另一種類型， 如此內置 NumPy 功能， 用於加入兩個或多個陣列：
print("-------------------------檢查另一種類型的")
#Check the type of another function: concatenate():
#檢查另一種類型的
import numpy as np
print(type(np.concatenate))
#If the function is not recognized at all, it will return an error:
#如果根本不識別該功能，它將返回錯誤：
print("-----------檢查不存在的東西的類型。這將產生錯誤")
#Check the type of something that does not exist. This will produce an error:
#檢查不存在的東西的類型。這將產生錯誤：
import numpy as np
try:
  x = np.blahblah
  if  type(x) is AttributeError:
    raise Exception("abc")
except Exception as e:
    print(e)

#To test if the function is a ufunc in an if statement, use the numpy.ufunc value (or np.ufunc if you use np as an alias for numpy):
#要在如果語句中測試該函數是否為 ufunc，請使用 numpy.ufunc 值（如果您使用 np 作為 numpy 的別名，則使用 np.ufunc）：
print("-----------使用如果語句來檢查該函數是否為 ufunc：")
#Use an if statement to check if the function is a ufunc or not:
#使用如果語句來檢查該函數是否為 ufunc：
import numpy as np
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')