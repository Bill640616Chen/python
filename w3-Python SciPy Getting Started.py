#https://www.w3schools.com/python/scipy/scipy_getting_started.php
#SciPy Getting Started SciPy開始
#Installation of SciPy 安裝SciPy
#If you have Python and PIP already installed on a system, then installation of SciPy is very easy.
#如果您已經在系統上安裝了 Python 和 PIP，那麼安裝 SciPy 非常簡單。
#Install it using this command:
#使用此指令安裝它：
#If this command fails, then use a Python distribution that already has SciPy installed like, Anaconda, Spyder etc.
#如果此命令失敗，則使用已經安裝了 SciPy 的 Pyon 分佈，例如，Anaconda、Spyder 等。
#Import SciPy 導入SciPy
#Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:
#安裝 SciPy 後，通過添加來自 Scipy 導入模組聲明的應用中要使用的 SciPy 模組：
from scipy import constants
#Now we have imported the constants module from SciPy, and the application is ready to use it:
#現在，我們已經從 SciPy 導入了常數模組，應用程式已準備好使用它：
#How many cubic meters are in one liter:
#一升多少立方米：
from scipy import constants
print(constants.liter) #0.001
#constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.
#常數：SciPy 提供了一組數學常數，其中之一是升，返回 1 升為立方米。
#You will learn more about constants in the next chapter.
#在接下來的一章中，您將瞭解更多有關常數的詳細情況。

print("----------------------------檢查SciPy版本")
#Checking SciPy Version 檢查SciPy版本
#The version string is stored under the __version__ attribute.
#版本字串存儲在__version__屬性下。
import scipy
print(scipy.__version__)
#Note: two underscore characters are used in __version__.
#注意：__version__中使用兩個下劃線字元。