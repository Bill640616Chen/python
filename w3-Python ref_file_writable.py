#https://www.w3schools.com/python/ref_file_writable.asp
#Python File writable() Method Python writable
#Returns whether the file can be written to or not
#返回是否能夠寫入檔。
#Check if the file is writable:
#檢查檔案是否可寫：
f = open("demofile.txt", "a")
print(f.writable())
#Definition and Usage 定義和用法
#The writable() method returns True if the file is writable, False if not.
#如此檔案是可寫的,writable()方法會返回真,否則會返回假
#A file is writable if it is opened using "a" for append or "w" for write.
#如果使用 「a」 追加或使用 「w」 寫入來打開檔，則該檔是可寫的。
#Syntax 語法
#file.writable()
#Parameter參數：Values值
#No parameters.無參數。