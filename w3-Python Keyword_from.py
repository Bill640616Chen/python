#https://www.w3schools.com/python/ref_keyword_from.asp
#Python Keyword from 關鍵字 from
#To import specific parts of a module
#匯入模組的特定部分。
#Import only the time section from the datetime module, and print the time as if it was 15:00:
#僅從 datetime 模組中導入時間部分，然後將時間列印為 15：00：
from datetime import time
x = time(hour=15)
print(x)
#Definition and Usage 定義和用法
#The from keyword is used to import only a specified section from a module.
#from 關鍵字用於從模組中僅導入指定的部分。
#Related Pages 相關頁面
#The import keyword.
#The as keyword.
#Read more about modules in our Python Modules Tutorial.
#請在我們的 Python 模組 教程中學習更多有關模組的知識。