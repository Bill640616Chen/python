#https://www.w3schools.com/python/python_pip.asp
#Python PIP Python 包或模組的包管理器。
#What is PIP? 什麼是 PIP？
#PIP is a package manager for Python packages, or modules if you like.
#PIP 是 Python 包或模組的包管理員。
#Note: If you have Python version 3.4 or later, PIP is included by default.
#註釋：如果您使用的是 Python 3.4 或更高版本，則預設情況下會包含 PIP。
#What is a Package? 什麼是包（Package）？
#A package contains all the files you need for a module.
#包中包含模組所需的所有檔。
#Modules are Python code libraries you can include in your project.
#模組是您可以包含在專案中的 Python 代碼庫。
#Check if PIP is Installed 檢查是否已安裝 PIP
#Navigate your command line to the location of Python's script directory, and type the following:
#將命令行導航到 Python 文稿目錄所在的位置，然後鍵入以下內容：
#Check PIP version: 檢查 PIP 版本：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

#Install PIP 安裝 PIP
#If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

#Download a Package 下載包
#Downloading a package is very easy.
#下載包非常容易。
#Open the command line interface and tell PIP to download the package you want.
#打開命令列介面並告訴 PIP 下載您需要的套件。
#Navigate your command line to the location of Python's script directory, and type the following:
#將命令列導航到 Python 文稿目錄的位置，然後鍵入以下內容：

#Download a package named "camelcase":
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
#Now you have downloaded and installed your first package!
#現在，您已經下載並安裝了第一個包！

#Using a Package 使用包
#Once the package is installed, it is ready to use.
#安裝包后，即可使用。
#Import the "camelcase" package into your project.
#把 「camelcase」 包導入您的專案中。
#Import and use "camelcase":

#import camelcase
#c = camelcase.CamelCase #模組.類
#txt = "hello world"
#print(c.hump(txt))

#Hump is a method that takes an inputted string and turns it 
# into camel case format.
#Hump是一種採用輸入字串並將其轉換為camelcase格式的方法。

#Find Packages 查找包
#Find more packages at https://pypi.org/.
#在 https://pypi.org/，您可以找到更多的包。
#Remove a Package 刪除包
#Use the uninstall command to remove a package:
#請使用 uninstall 命令來移除套件：
#Uninstall the package named "camelcase":
#卸載名為 "camelcase" 的包：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase
#The PIP Package Manager will ask you to confirm that you want to remove the camelcase package:
#PIP 包管理員會要求您確認是否需要刪除 camelcase 包：
#Uninstalling camelcase-02.1:
#  Would remove:
#    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase-0.2-py3.6.egg-info
#    c:\users\Your Name\appdata\local\programs\python\python36-32\lib\site-packages\camecase\*
#Proceed (y/n)?
#Press y and the package will be removed.

#List Packages 列出包
#Use the list command to list all the packages installed on your system:
#請使用 list 命令列出系統上安裝的所有套件：
#List installed packages:
#列出已安裝的套件：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
