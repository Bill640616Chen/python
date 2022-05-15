#https://www.w3schools.com/python/gloss_python_pip_packages.asp
#Download a Package 下載套件
#Downloading a package is very easy.
#下載套件非常簡單。
#Open the command line interface and tell PIP to download the package you want.
#打開命令列介面，告訴 PIP 下載所需的套件。
#Navigate your command line to the location of Python's script directory, and type the following:
#將命令列導航到 Python 文稿目錄的位置，然後鍵入以下內容：
#Download a package named "camelcase":
#下載一個名為「camelcase」的套件：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
#Now you have downloaded and installed your first package!
#現在，您已經下載並安裝了第一個軟體包！
#Using a Package 使用包
#Once the package is installed, it is ready to use.
#安裝套件后，即可使用。
#Import the "camelcase" package into your project.
#將「駱駝殼」包導入到專案中。
#Import and use "camelcase":
#導入和使用「駱駝殼」：
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
#Find Packages 查找套件
#Find more packages at https://pypi.org/.
#在https://pypi.org/找到更多套件。
#List Packages 列出包
#Use the list command to list all the packages installed on your system:
#使用以下命令列出系統上安裝的所有套件：list
#List installed packages:
#列出已安裝的套件：
#C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
#Result:
#結果：
'''
Package         Version
-----------------------
camelcase       0.2
mysql-connector 2.1.6
pip             18.1
pymongo         3.6.1
setuptools      39.0.1
'''
#Related Pages 相關頁面
#Python PIP Tutorial
#https://www.w3schools.com/python/python_pip.asp
#Install PIP
#https://www.w3schools.com/python/gloss_python_pip_install.asp
#PIP Remove Package PIP 刪除包
#https://www.w3schools.com/python/gloss_python_pip_packages_remove.asp