#https://www.w3schools.com/python/numpy/numpy_ufunc_differences.asp
#NumPy LCM Lowest Common Multiple 最小公倍數
#Finding LCM (Lowest Common Multiple)
#尋找最小公倍數
#The Lowest Common Multiple is the least number that is common multiple of both of the numbers.
#最小公倍數是兩個數字中常見的倍數最少的倍數。
#Find the LCM of the following two numbers:
print("-----------------------尋找以下兩個數字的 LCM")
#尋找以下兩個數字的 LCM：
import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x) #12
y =np.lcm(2,3)
print(y) #6
#Returns: 12 because that is the lowest common 
# multiple of both numbers (4*3=12 and 6*2=12).
#返回： 12， 因為這是兩個數字中最低的常見倍數 
# （4*3=12 和 6*2=12）。

#Finding LCM in Arrays 在陣列中查找 LCM
#To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
#要查找陣列中所有值中的最小公倍數，您可以使用"reduce()"方法。
#The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.
#reduce()方法將使用 ufunc，在此例中，lcm（） 功能，在每個元素上，並減少一個維度陣列。
#Find the LCM of the values of the following array:
print("-----------------------尋找下列陣列值的 LCM")
#尋找下列陣列值的 LCM：
import numpy as np
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
#Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).
#返回： 18， 因為這是所有三個數位中最小公倍數 （3*6×18， 6*3×18 和 9*2×18）.
#array(),()裡不限個數

print("-----------------------尋找所有陣列的 LCM")
#Find the LCM of all of an array where the array contains all integers from 1 to 10:
#尋找所有陣列的 LCM，其中陣列包含 1 到 10 的所有整數：
import numpy as np
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x) #2520
#arange(1, 11)不包括11