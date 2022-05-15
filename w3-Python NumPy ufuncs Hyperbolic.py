#https://www.w3schools.com/python/numpy/numpy_ufunc_hyperbolic.asp
#NumPy Hyperbolic Functions 雙曲函數
#NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
#NumPy提供了通用函數sinh(), cosh() and tanh()取的孤度值並產生對應sinh, cosh and tanh 的值
#Find sinh value of PI/2:
print("---------------------------尋找 PI/2 的正值")
#尋找 PI/2 的正值：
import numpy as np
x = np.sinh(np.pi/2)
print(x)

print("--------------------在陣列裡所有的值找cosh值")
#Find cosh values for all of the values in arr:
#在陣列裡所有的值找cosh值
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)

print("---------------------Finding Angles 找角度")
#Finding Angles 找角度
#Finding angles from values of hyperbolic sine, 
# cos, tan. E.g. sinh, cosh and tanh inverse 
# (arcsinh, arccosh, arctanh).
#從sine, cos, tan. E.g. sinh, cosh和tanh 的反向 
# (arcsinh, arccosh, arctanh).雙曲函數的值找角度
#Numpy provides ufuncs arcsinh(), arccosh() and 
# arctanh() that produce radian values for 
# corresponding sinh, cosh and tanh values given.
#Numpy提供了通用函數arcsinh(), arccosh() and 
# arctanh()產生sinh, cosh and tanh對應的弧度值
#Find the angle of 1.0:
#尋找 1.0 的角度：
import numpy as np
x = np.arcsinh(1.0)
print(x)

print("-------------------------陣列中每個值的角度")
#Angles of Each Value in Arrays
#陣列中每個值的角度
#Find the angle for all of the tanh values in array:
#尋找陣列中所有 tanh 值的角度：
import numpy as np
arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x)