#https://www.w3schools.com/python/python_datetime.asp
#Python Datetime 日期時間
#Python Dates日期
#A date in Python is not a data type of its own, but we 
# can import a module named datetime to work with dates as date objects.
#Python 中的日期不是其自身的數據類型，但是我們可以導入名為 
# datetime 的模組，把日期視作日期對象進行處理。
#Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
#Concrete date/time and related types.
#具體日期/時間和相關類型。
#See http://www.iana.org/time-zones/repository/tz-link.html 
# for time zone and DST data sources.
#該網站是日期時間的資料來源

print("-------------------------------Date Output 日期輸出")
#Date Output 日期輸出
#When we execute the code from the example above the result
# will be:
#如果我們執行上面的代碼，結果將是：
#2021-10-05 14:50:22.233417
#The date contains year, month, day, hour, minute, second, 
# and microsecond.
#日期包含年、月、日、小時、分鐘、秒和微秒。
#The datetime module has many methods to return information 
# about the date object.
#datetime 模組有許多方法可以傳回有關日期物件的信息。
#Here are a few examples, you will learn more about them 
# later in this chapter:
#以下是一些例子，您將在本章稍後詳細學習它們：
#Return the year and name of weekday:
#傳回 weekday 的名稱和年份：
import datetime
x = datetime.datetime.now()
print(x.year) #2021
print(x.strftime("%A")) #Tuesday
#%A:Weekday, full version
#"%A"輸出Weekday，完整版本,取禮拜幾
#Format using strftime() 格式化使用方法的值是str
#strftime是string format time的縮寫


print("------------------Creating Date Objects 創建日期物件")
#Creating Date Objects 創建日期物件
#To create a date, we can use the datetime() class 
# (constructor) of the datetime module.
#如需創建日期，我們可以使用 datetime 模組的 datetime() 類
#（構造函數）。
#The datetime() class requires three parameters to create
# a date: year, month, day.
#datetime() 類需要三個參數來創建日期：年、月、日。
#Create a date object:
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
#語法：datetime(year,month,day,hour,minute,second)
#year,month,day必填,hour,minute,second非必要填
#The datetime() class also takes parameters for time and 
# timezone (hour, minute, second, microsecond, tzone), but
# they are optional, and has a default value of 0, 
# (None for timezone).
#datetime() 類還接受時間和時區（小時、分鐘、秒、微秒、tzone）
# 的參數，不過它們是可選的，默認值為 0，（時區默認為 None）。

print("------------------Creating Date Objects 創建日期物件")
#The strftime() Method 根據給定格式將物件轉換為字串
#The datetime object has a method for formatting date 
# objects into readable strings.
#datetime 物件擁有把日期對象格式化為可讀字元串的方法。
#The method is called strftime(), and takes one parameter, 
# format, to specify the format of the returned string:
#該方法稱為 strftime()，並使用一個 format 參數來指定傳回字元串
# 的格式：
#Display the name of the month:
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B")) #June
#%B：Month name, full version 取月份
#strftime("%B"),()裡最多只能一個引用參數

print("------------------------------所有合法格式代碼的參考")
#A reference of all the legal format codes:
#所有合法格式代碼的參考：
'''指令	    描述	                     實例'''	
'''%a	    Weekday，短版本 	         Wed'''
'''%A	    Weekday，完整版本	         Wednesday'''	
'''%w	    Weekday，数字0-6，0 为周日 	  3'''	
'''%d	    日，数字 01-31	             31	'''
'''%b	    月名稱，短版本	              Dec'''	
'''%B	    月名稱，完整版本	          December'''	
'''%m	    月，数字01-12	             12'''	
'''%y	    年，短版本，無世纪            18'''	
'''%Y	    年，完整版本	              2018'''	
'''%H	    24小時制，00-23               17'''	
'''%I	    24小時制，00-12               05'''	
'''%p	    AM/PM	                      PM'''	
'''%M	    分，00-59	                  41'''	
'''%S	    秒，00-59	                  08'''
'''%f	    微秒，000000-999999	          548513'''
'''%z	    UTC 偏移	                 +0100'''	
'''%Z	    時區	                      CST'''	
'''%j	    相當於一年的第幾天，001-366	    365'''	
'''%U	    周数，每周的第一天是周日，00-53	52'''	
'''%W	    周数，每周的第一天是周一，00-53	52'''	
'''%c	    本地的日期和時間	           Mon Dec 31 17:41:00 2018	'''
'''%C      Century世紀                    20'''
'''%x	    日期的本地版本	               12/31/18'''	
'''%X	    時間的本地版本	               17:41:00'''	
'''%%	    A % character	              %'''
'''%G	    ISO 8601 year	              2018'''
'''%u	    ISO 8601 weekday (1-7)	      1'''
'''%V	    ISO 8601 weeknumber (01-53)	  01'''
import datetime
x = datetime.datetime(2021, 10, 5, 20, 5, 51, 895373)
print(x.strftime("%a")) #Tue
print(x.strftime("%A")) #Tuesday
print(x.strftime("%w")) #2
print(x.strftime("%d")) #05
print(x.strftime("%b")) #Oct
print(x.strftime("%B")) #October
print(x.strftime("%m")) #10
print(x.strftime("%y")) #21
print(x.strftime("%Y")) #2021
print(x.strftime("%H")) #20
print(x.strftime("%I")) #08
print(x.strftime("%p")) #PM
print(x.strftime("%M")) #PM
print(x.strftime("%S")) #51
print(x.strftime("%f")) #895373
print(x.strftime("%z")) #
print(x.strftime("%Z")) #
print(x.strftime("%j")) #278
print(x.strftime("%U")) #40
print(x.strftime("%W")) #40
print(x.strftime("%c")) #Tue Oct  5 20:05:51 2021
print(x.strftime("%C")) #20
print(x.strftime("%x")) #10/05/21
print(x.strftime("%X")) #20:05:51
print(x.strftime("%%")) #%
print(x.strftime("%G")) #2021
print(x.strftime("%u")) #2
print(x.strftime("%V")) #40

