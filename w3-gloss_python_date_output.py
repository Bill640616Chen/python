#https://www.w3schools.com/python/gloss_python_date_output.asp
#Python Date Output 日期輸出
#When we execute the code from the example above the result will be:
#當我們執行上面範例中的代碼時，結果將是：
#2021-11-26 11:53:15.108240
#The date contains year, month, day, hour, minute, second, and microsecond.
#日期包含年、月、日、小時、分鐘、秒和微秒。
#The module has many methods to return information about the date object.datetime
#該模組有許多方法來返回有關 date 物件的資訊。datetime
#Here are a few examples, you will learn more about them later in this chapter:
#以下是一些範例，您將在本章後面部分了解有關它們的更多資訊：
#Return the year and name of weekday:
#傳回工作日的年份與名稱：
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#Related Pages 相關頁面
#Python DateTime Tutorial
#https://www.w3schools.com/python/python_datetime.asp
#Datetime Module 日期時間模組
#https://www.w3schools.com/python/gloss_python_date.asp
#Create a Date Object 創建日期物件
#https://www.w3schools.com/python/gloss_python_date_create.asp
#The strftime Method 斯特夫時間方法
#https://www.w3schools.com/python/gloss_python_date_strftime.asp
#Date Format Codes 日期格式代碼
#https://www.w3schools.com/python/gloss_python_date_format_codes.asp