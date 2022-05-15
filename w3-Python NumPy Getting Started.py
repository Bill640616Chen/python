#https://www.w3schools.com/python/numpy/numpy_getting_started.asp
#NumPy Getting Started NumPy開始
#Installation of NumPy 安裝 NumPy
#If you have Python and PIP already installed on a system, then installation of NumPy is very easy.
#如果您已經在系統上安裝了 Python 和 PIP，那麼安裝 NumPy 非常容易。
#Install it using this command:
#請使用這條指令安裝它：
#C:\Users\Your Name>pip install numpy
#If this command fails, then use a python distribution that already has NumPy installed like, Anaconda, Spyder etc.
#如果此命令失敗，請使用已經安裝了 NumPy 的 python 發行版，例如 Anaconda、Spyder 等。
#Import NumPy 導入 NumPy
#Once NumPy is installed, import it in your applications by adding the import keyword:
#安裝 NumPy 後，透過新增 import 關鍵字將其匯入您的應用程式：
import numpy
#Now NumPy is imported and ready to use.
#現在，Numpy 已導入並可以使用。
import numpy
#arr = numpy.array([1, 2, 3, 4, 5])
print(numpy.array([1, 2, 3, 4, 5]))
#原本輸出不正常AttributeError: module 'numbers' has no attribute 'Integral'
#在我專案資料夾（python_work）中有一個 numbers.py 的檔，將其刪除後則恢復正常。 則問題是出現在import的定位上。
#把numbers.py改名過恢復正常,輸出[1 2 3 4 5]
#NumPy 通常以 np 別名導入。
#NumPy as np
#NumPy is usually imported under the np alias.
#別名：在 Python 中，別名是用於引用同一事物的替代名稱。
#alias: In Python alias are an alternate name for referring to the same thing.
#別名：在 Python 中，別名是用於引用同一事物的替代名稱。
#Create an alias with the as keyword while importing:
#請匯入時使用 as 關鍵字建立別名：
import numpy as np
#Now the NumPy package can be referred to as np instead of numpy.
#現在，可以將 NumPy 包稱為 np 而不是 numpy。
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Checking NumPy Version 檢查 NumPy 版本
#The version string is stored under __version__ attribute.
#版本字串存儲在 __version__ 屬性中。
import numpy as np
print(np.__version__)
np.full_like