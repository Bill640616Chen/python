#https://www.w3schools.com/python/ref_file_seekable.asp
#Python File seekable() Method Python seekable
#Returns whether the file allows us to change the file position
#返回檔案是否允許我們更改檔案位置。
#Check if the file is seekable:
#檢查檔案是否可搜尋：
f = open("demofile.txt", "r")
print(f.seekable())
#Definition and Usage 定義和用法
#The seekable() method returns True if the file is seekable, False if not.
#如果檔可搜索，seekable（） 方法返回 True，否則返回 False。
#A file is seekable if it allows access to the file stream, like the seek() method.
#如果文件允許訪問檔流（例如 seek（） 方法），則該檔是可搜索的。
#Syntax 語法
#file.seekable()
#Parameter參數：Values值
#No parameters.無參數。


