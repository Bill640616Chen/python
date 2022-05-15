#https://www.w3schools.com/python/python_mysql_getstarted.asp
#Python MySQL
#Python can be used in database applications.
#Python 可用於資料庫應用程式。
#One of the most popular databases is MySQL.
#最受歡迎的資料庫之一是 MySQL。
#MySQL Database MySQL資料庫
#To be able to experiment with the code examples in this tutorial, you should have MySQL installed on your computer.
#為了能夠在此教程中嘗試代碼範例，您應該在電腦上安裝 MySQL。
#You can download a free MySQL database at https://www.mysql.com/downloads/.
#您可以在 https://www.mysql.com/downloads/ 下載免費的 MySQL 資料庫。
#Install MySQL Driver 安裝 MySQL 驅動程式
#Python needs a MySQL driver to access the MySQL database.
#Python 需要一個 Mysql 驅動程式來訪問 Mysql 資料庫。
#In this tutorial we will use the driver "MySQL Connector".
#在此教程中，我們將使用驅動程式"MySQL 連接器"。
#We recommend that you use PIP to install "MySQL Connector".
#我們建議您使用 PIP 安裝「MySQL 連接器」。
#PIP is most likely already installed in your Python environment.
#PIP 很可能已經安裝在您的 Python 環境中。
#Navigate your command line to the location of PIP, and type the following:
#將命令線導航到 PIP 的位置，並鍵入以下類型：
#Download and install "MySQL Connector":
#下載並安裝「MySQL 連接器」
#Now you have downloaded and installed a MySQL driver.
#現在，您已經下載並安裝了 MySQL 驅動程式。
#Test MySQL Connector 測試 MySQL 連接器
#To test if the installation was successful, or if you already have "MySQL Connector" installed, create a Python page with the following content:
#要測試安裝是否成功，或者您已經安裝了「MySQL 連接器」，請創建具有以下內容的 Python 頁面：
#demo_mysql_test.py:
import mysql.connector
#if this page is executed with no errors, you have the "mysql.connector" module installed.
#如果此頁面執行時沒有錯誤，則安裝了「mysql.connector」模組。
#If the above code was executed with no errors, "MySQL Connector" is installed and ready to be used.
#如果執行上述代碼時沒有錯誤，則安裝「MySQL 連接器」 並準備使用。
#Create Connection 創建連接
#Start by creating a connection to the database.
#首先創建與資料庫的連接。
#Use the username and password from your MySQL database:
#使用MySQL資料庫中的使用者名和密碼：
#demo_mysql_connection.py:
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)
print(mydb)
#Now you can start querying the database using SQL statements.
#現在，您可以開始使用 SQL 對帳單查詢資料庫。


