#https://www.w3schools.com/python/scipy/scipy_interpolation.php
#SciPy Interpolation SciPy插值
#What is Interpolation? 什麼是插值
#Interpolation is a method for generating points between given points.
#插值是一種在給定點之間生成點的方法。
#For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.
#例如：對於第 1 點和第 2 點，我們可以插值並查找點 1.33 和 1.66。
#Interpolation has many usage, in Machine Learning we often deal with missing data in a dataset, interpolation is often used to substitute those values.
#插值有許多用法，在機器學習中，我們經常處理數據集中的缺失數據，插值通常用於替換這些值。
#This method of filling values is called imputation.
#這種填充值的方法稱為缺失值處理。
#Apart from imputation, interpolation is often used where we need to smooth the discrete points in a dataset.
#除了缺失值處理之外，在我們需要平滑數據集中的離散點時，通常使用插值。
#How to Implement it in SciPy? 如何在 SciPy 中實現它？
#SciPy provides us with a module called scipy.interpolate which has many functions to deal with interpolation:
#SciPy 為我們提供了一個名為 scipy.interpolate的模組，它具有處理插值的許多函數：
#1D Interpolation1D 插值
#The function interp1d() is used to interpolate a distribution with 1 variable.
#函數interp1d()用於將分佈與1個變數進行插值。
#It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.
#它需要 x 點和 y 點，並返回可調用的函數，可以調用新的 x 和返回相應的 y。
#For given xs and ys interpolate values from 2.1, 2.2... to 2.9:
print("--------對於給定的 xs 和 ys 插值從 2.1， 2.2...至2.9")
#對於給定的 xs 和 ys 插值從 2.1， 2.2...至2.9：
from scipy.interpolate import interp1d
import numpy as np
xs = np.arange(10)
ys = 2*xs + 1
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)
#arange([start,] stop[, step,], dtype=None, *, like=None)
#Note: that new xs should be in same range as of the old xs, meaning that we cant call interp_func() with values higher than 10, or less than 0.
#注意：新 x 應與舊 x 處於相同的範圍，這意味著我們不能調用值高於 10 或小於 0 的interp_func（）。

print("--------Spline Interpolation 正弦波(樣條曲線)插值")
#Spline Interpolation 正弦波(樣條曲線)插值
#In 1D interpolation the points are fitted for a single curve whereas in Spline interpolation the points are fitted against a piecewise function defined with polynomials called splines.
#在 1D 插值中，點適合單個曲線，而在 Spline 插值中，點與稱為 spline 的多名詞定義的片面函數相連接。
#The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.
#UnivariateSpline （） 函數需要 xs 和 ys， 並產生一個可呼叫的 funciton， 可以呼叫新的 xs 。
#Piecewise function: A function that has different definition for different ranges.
#分件函數：對不同範圍有不同的定義的函數。
#Find univariate spline interpolation for 2.1, 2.2... 2.9 for the following non linear points:
#尋找單變體 spline 插值 2.1， 2.2...2.9 表示以下非線性點：
from scipy.interpolate import UnivariateSpline
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

print("---------------Rbf()--帶徑向基礎函數的插值")
#Interpolation with Radial Basis Function
#帶徑向基礎函數的插值
#Radial basis function is a function that is defined corresponding to a fixed reference point.
#徑向基礎函數是與固定參考點相對應的函數。
#The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.
#Rbf()功能還以 xs 和 ys 作為參數，並生成可調用的功能，可調用新 x。
#Interpolate following xs and ys using rbf and find values for 2.1, 2.2 ... 2.9:
#使用 rbf 的 x 和 ys 進行插值， 並查找 2.1、 2.2...2.9:
from scipy.interpolate import Rbf
import numpy as np
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)