#https://www.w3schools.com/python/numpy/numpy_ufunc_rounding_decimals.asp
#Rounding Decimals
#四捨五入的十進位
#There are primarily five ways of rounding off decimals in NumPy:
#在 NumPy 中，主要有五種捨入小數點的方法：
#truncation 無條件捨去 trunc() 輸出有浮點
#fix 無條件捨去 fix()
#rounding 四捨五入 round(x [, n]) n是小數後第n+1位計算四捨五入
#floor 向下取整
#ceil 向上取整
#Truncation 無條件捨去
#Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
#移除十進位,然後傳回浮點數趨近於0,使用trunc() 和 fix()函數
#Truncate elements of following array:
#無條件捨去的元素,如下的陣列
print("------------------無條件捨去 trunc() 輸出有浮點")
import numpy as np
arr = np.trunc([-3.1666, 3.6667])
print(arr)
#truncation 無條件捨去 trunc() 輸出有浮點
print("--------------------無條件捨去 fix() 輸出有浮點")
import numpy as np
arr = np.fix([3.14, 1])
print(arr)
#fix 無條件捨去 fix() 輸出有浮點
print("--------round(x [, n]) n是小數後第n+1位計算四捨五入")
import numpy as np
arr = np.round(3.1463256, 3)
print(arr)
#round(x [, n]) n是小數後第n+1位計算四捨五入
print("--------------floor()---向下取整,輸出有浮點")
import numpy as np
arr = np.floor([-1.2, -1.5, -0.2, 0.7, 1.9, 1.2, 2.0])
print(arr)
#[-2. -2. -1.  0.  1.  1.  2.]
#floor() 向下取整,輸出有浮點
print("---------------ceil()---向下取整,輸出有浮點")
import numpy as np
arr = np.ceil([-1.2, -1.5, -0.2, 0.7, 1.9, 1.2, 2.0])
print(arr)
#[-1. -1. -0.  1.  2.  2.  2.]
#ceil() 向上取整,輸出有浮點
