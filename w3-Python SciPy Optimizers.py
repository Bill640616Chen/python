#https://www.w3schools.com/python/scipy/scipy_optimizers.php
#SciPy Optimizers SciPy優化器
#Optimizers in SciPy 優化器in SciPy
#Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.
#優化器是 SciPy 中定義的一組程式，它們要麼找到函數的最小值，要麼找到方程式的平方根。
#Optimizing Functions 優化函數
#Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.
#從本質上講，機器學習中的所有演算法只不過是一個複雜的方程式，需要在給定數據的説明下最小化。
#Roots of an Equation 方程式的根
#NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:
#NumPy 能夠為多項式和線性方程式找到根，但它無法找到非線性方程式的根，例如：
#x + cos(x)
#For that you can use SciPy's optimze.root function.
#為此，您可以使用 SciPy 的優化.根功能。
#This function takes two required arguments:
#此功能需要兩個必要的參數：
#fun - a function representing an equation.
#fun - 代表方程式的函數
#x0 - an initial guess for the root.
#x0 - 根的初始猜測
#The function returns an object with information regarding the solution.
#該功能返回物件，其中提供了有關解決方案的資訊。
#The actual solution is given under attribute x of the returned object:
#實際解決方案根據返回物件的屬性 x 給出：
print("----------------------------root(eqn, 0)")
#Find root of the equation x + cos(x):
#尋找方程式 x 的平方根
from scipy.optimize import root
from math import cos
def eqn(x):
  return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)
#列印方程式的方根
#Note: The returned object has much more information about the solution.
#注意：返回的物件有更多有關解決方案的資訊。
#Print all information about the solution (not just x which is the root)
print("-----------------列印有關解決方案的所有資訊")
#列印有關解決方案的所有資訊（而不僅僅是 x 是根）
from scipy.optimize import root
from math import cos
def eqn(x):
  return x + cos(x)
myroot = root(eqn, 0)
print(myroot)

#Minimizing a Function 最小化一個函數
#A function, in this context, represents a curve, curves have high points and low points.
#在此上下文中，函數表示曲線，曲線具有高點和低點。
#High points are called maxima.
#高點稱為最大值。
#Low points are called minima.
#低點稱為最小值。
#The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.
#整個曲線中的最高點稱為全球最大值，而其餘點稱為本地最大值。
#The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.
#整個曲線的最低點稱為全球最小值，而其餘的點稱為本地最小值。
#Finding Minima 查找最小值
#We can use scipy.optimize.minimize() function to minimize the function.
#我們可以使用 scipy.optimize.minimize() 功能來最小化功能。
#The minimize() function takes the following arguments:
#minimize() 功能需要以下參數：
#fun - a function representing an equation.
#fun - 代表方程式的函數
#x0 - an initial guess for the root.
#x0 - 根的初始猜測
#method - name of the method to use. Legal values:
#method - 要使用的方法的名稱。合法值：
#    'CG'：center of gravity (CG) - 重心
#    'BFGS'擬牛頓方法
#BFGS演算法(Broyden–Fletcher–Goldfarb–Shanno)
#    'Newton-CG'
#    'L-BFGS-B'
#    'TNC'
#    'COBYLA'
#    'SLSQP'
#Sequential Least-Squares Quadratic Programming (SLSQP) 算法
#callback - function called after each iteration of optimization.
#callback - 每次優化反覆運算后調用的功能。
#options - a dictionary defining extra params:
#options - 定義額外參數的字典
#{    "disp": boolean - print detailed description
#     "gtol": number - the tolerance of the error
#  }
#scipy.optimize.minimize(fun, x0, args=(), 
# method=None, jac=None, hess=None, hessp=None, 
# bounds=None, constraints=(), tol=None, 
# callback=None, options=None)
#最小化一個或多個變量的標量函數。
#Minimize the function x^2 + x + 2 with BFGS:
print("-------------minimize(eqn, 0, method='BFGS')")
print("-----------------列印有關解決方案的所有資訊")
#最小化功能 x+2 = x = 2 與 BFGS：
from scipy.optimize import minimize
def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)
#minimize(fun, x0, method='legal value')
#minimize(eqn, 0, method='BFGS')
print("-------------minimize(eqn, 0, method='TNC')")
from scipy.optimize import minimize
def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0,method='TNC')
print(mymin)
