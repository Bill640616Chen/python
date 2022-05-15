#https://www.w3schools.com/python/ref_file_read.asp
#Python File read() Method Python read
#Returns the file content
# 返回文件內容。
#Read the content of the file "demofile.txt":
#讀取檔 「demofile.txt」 的內容：
f = open("demofile.txt", "r")
print(f.read())
#Definition and Usage 定義和用法
#The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
#read（） 方法從檔案返回指定的位元元組數。 預設值為 -1，表示整個檔。
#Syntax 語法
#file.read()
#Parameter參數：Values值
#Parameter參數：Description描述
#size：Optional. The number of bytes to return. Default -1, which means the whole file.
#size：可選。 要返回的位元組數。 預設值 -1，表示整個檔。
#Read the content of the file "demofile.txt":
#讀取檔 「demofile.txt」 的內容：
f = open("demofile.txt", "r")
print(f.read(33))






