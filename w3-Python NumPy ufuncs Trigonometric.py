#https://www.w3schools.com/python/numpy/numpy_ufunc_trigonometric.asp
#NumPy Trigonometric Functions 三角測量功能
#NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
#NumPy提供通用函數sin(), cos() and tan()取得孤度值與產生相對應的sin, cos and tan的值
#Find sine value of PI/2:
print("--------------------------查找 PI/2 的sine值")
#查找 PI/2 的sine值：
import numpy as np
x = np.sin(np.pi/2)
print(x) #1.0

print("---------------------在陣列所有的值查找sine值")
#Find sine values for all of the values in arr:
#在陣列所有的值查找sine值
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
#[1.         0.8660254  0.70710678 0.58778525]

print("----------------------------把角度轉換為孤度")
#Convert Degrees Into Radians 把角度轉換為孤度
#By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumP.
#默認情況下，所有的三角測量功能都以孤度為參數，但我們可以將孤度轉換為度，反之亦然，以及在NumP。
#Note: radians values are pi/180 * degree_values.
#孤度值是 pi/180 * 度數值。
#Convert all of the values in following array arr to radians:
#將以下陣列 arr 中的所有值轉換為 radians：
import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

print("------------------------------孤度轉為度數")
#Radians to Degrees 孤度轉為度數
#Convert all of the values in following array arr to degrees:
#將以下陣列 arr 中的所有值轉換為度：
import numpy as np
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)

print("------------------------------孤度轉為度數")
#Finding Angles 查找角度
#Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
#從sine, cos, tan的值找角度,例如sin, cos and tan的反向arcsin, arccos, arctan
#NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
#NumPy提供通用函數arcsin(), arccos() and arctan()產生的孤度值是對應的sin, cos and tan值給予的
#Find the angle of 1.0:
#尋找 1.0 的角度：
import numpy as np
x = np.arcsin(1.0)
print(x)

print("---------------------------陣列中每個值的角度")
#Angles of Each Value in Arrays
#陣列中每個值的角度
#Find the angle for all of the sine values in the array
#查找陣列中所有sine值的角度
import numpy as np
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

print("----------------------------------------斜邊")
#Hypotenues 斜邊
#Finding hypotenues using pythagoras theorem in NumPy.
#使用畢氏定理在in NumPy找出斜邊值
#NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
#NumPy提供hypot()函數以基數和垂直值為基礎,並產生畢氏定理的斜邊
#Find the hypotenues for 4 base and 3 perpendicular:
#由底邊長4及垂直邊長3找出斜邊長
import numpy as np
base = 3 #底邊長
perp = 4 #垂直長
x = np.hypot(base, perp)
print(x)