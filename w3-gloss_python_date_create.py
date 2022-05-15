#https://www.w3schools.com/python/gloss_python_date_create.asp
#Create Date Object 日期輸出
#To create a date, we can use the datetime() class (constructor) of the datetime module.
#要創建日期，我們可以使用模組的類（構造函數）。datetime()datetime
#The datetime() class requires three parameters to create a date: year, month, day.
#該類需要三個參數來創建日期：年、月、日。datetime()
#Create a date object:
#建立日期物件：
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
#該類還採用時間和時區（小時、分鐘、秒、微秒、tzone）的參數，但它們是可選的，並且預設值為 ，（對於時區）。datetime()0None
#Related Pages 相關頁面
#Python DateTime Tutorial
#https://www.w3schools.com/python/python_datetime.asp
#Datetime Module 日期時間模組
#https://www.w3schools.com/python/gloss_python_date.asp
#Date Output 日期輸出
#https://www.w3schools.com/python/gloss_python_date_output.asp
#The strftime Method 斯特夫時間方法
#https://www.w3schools.com/python/gloss_python_date_strftime.asp
#Date Format Codes 日期格式代碼
#https://www.w3schools.com/python/gloss_python_date_format_codes.asp