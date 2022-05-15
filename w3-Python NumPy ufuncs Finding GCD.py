#https://www.w3schools.com/python/numpy/numpy_ufunc_gcd.asp
#NumPy LCM GCD Greatest Common Denominator 
#最大共同點（最大公因數）
#The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
#GCD（最大共同點），也稱為HCF（最大公因數）是兩個數字中最大的共同因素。
#Find the HCF of the following two numbers:
print("----------------------尋找以下兩個數字的 HCF")
#尋找以下兩個數字的 HCF：
import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
#Returns: 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).
#返回： 3，因為這是兩個數字可以除以的最高數字 （6/3+2 和 9/3+3）。

print("-----------------GCD-----在陣列裡找最大公因數")
#Finding GCD in Arrays 在陣列裡找最大公因數
#To find the Highest Common Factor of all values in an array, you can use the reduce() method.
#要查找陣列中所有值的最大公因數，您可以使用"reduce()"方法。
#The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.
#reduce()方法將使用 ufunc，在這種情況下，每個元素上的 gcd （） 函數，並將陣列減少一個維度。
#Find the GCD for all of the numbers in following array:
#尋找以下陣列中所有數字的 GCD：
import numpy as np
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
#Returns: 4 because that is the highest number all values can be divided by.
#返回： 4 因為這是所有值可以除以的最高數字。