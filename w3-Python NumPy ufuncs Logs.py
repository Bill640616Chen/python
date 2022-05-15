#https://www.w3schools.com/python/numpy/numpy_ufunc_logs.asp
#NumPy Logs 對數
#Logs 對數
#NumPy provides functions to perform log at the base 2, e and 10.
#NumPy 提供函數去演算log對數,底數數為2,e,10
#We will also explore how we can take log for any base by creating a custom ufunc.
#我們還將探索如何通過創建自定義ufunc來記錄任何底數數。
#All of the log functions will place -inf or inf in the elements if the log can not be computed.
#如果無法計算對數，所有對數函數都將在元素中放置 - inf 或 inf。
#Log at Base 2 對數底數2
#Use the log2() function to perform log at the base 2.
#使用log2()函數演算log底數2
#Find log at base 2 of all elements of following array:
print("------------------傳回的值是Ｘ,例:log2１＝Ｘ")
#找尋log底數2,陣列中所有元素
import numpy as np
arr = np.arange(1, 5)
print(np.log2(arr))
#傳回的值是Ｘ,例:log2１＝Ｘ
#Note: The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
#The arange(1, 10)函數傳回整數陣列,從1(包含)開始到10(不包含)

print("------------------傳回的值是Ｘ,例:log10１＝Ｘ")
#Log at Base 10 log底數10
#Use the log10() function to perform log at the base 10.
#使用log10()函數演算log底數10
#Find log at base 10 of all elements of following array:
#找尋log底數10,陣列中所有元素
import numpy as np
arr = np.arange(1, 10)
print(np.log10(arr))

print("------------------傳回的值是Ｘ,例:loge１＝Ｘ")
#Natural Log, or Log at Base e
#自然對數,或都log底數e
#Use the log() function to perform log at the base e.
#使用log()函數演算log底數e
#Find log at base e of all elements of following array:
#找尋log底數e,陣列中所有元素
import numpy as np
arr = np.arange(1, 10) #()裡面是真數
print(np.log(arr))

print("------------傳回的值是Ｘ,例:log任意底數＝Ｘ")
#Log at Any Base log任何底數
#NumPy does not provide any function to take log at 
# any base, so we can use the frompyfunc() function 
# along with inbuilt function math.log() with two 
# input parameters and one output parameter:
#NumPy沒有提供任何函數給log使用任何的底數
# (預設底數是2,10,e),所以我們可以使用rompyfunc()函數
# 以及內建函數math.log()2個輸入參數和1個輸出參數
from math import log
import numpy as np
nplog = np.frompyfunc(log, 2, 1)
#frompyfunc(func, nin, nout, *[, identity])
#frompyfunc(func，nin，nout)函數允許創建一個任意的
#frompyfunc(func，真數，底數)
# Python函數作為Numpy ufunc(通用函數)
print(nplog(100, 15))