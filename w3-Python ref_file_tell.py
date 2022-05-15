#https://www.w3schools.com/python/ref_file_tell.asp
#Python File tell() Method Python tell
#Returns the current file position
#返回当前的文件位置。
#Find the current file position:
#尋找目前的檔案位置：
f = open("demofile.txt", "r")
print(f.tell())
#返回索引位置0
#Definition and Usage 定義和用法
#The tell() method returns the current file position in a file stream.
#tell（） 方法傳回檔案流中的目前檔案位置。
#Tip: You can change the current file position with the seek() method.
#提示：您可以通過 seek（） 方法更改目前的檔案的位置。
#Syntax 語法
#file.tell()
#Parameter參數：Values值
#No parameter values.無參數值。
#Return the current file position after reading the first line:
f = open("demofile.txt", "r")
print(f.readline())
print(f.tell())
#列出第一行的所有孛元
#返回行的最後索引位置238