#https://www.w3schools.com/python/ref_file_seek.asp
#Python File seek() Method Python seek
#Change the file position
#更改檔案位置。
#Change the current file position to 4, and return the rest of the line:
#將當前檔案位置更改為 4，然後返回其餘行：
f = open("demofile.txt", "r")
f.seek(10)
print(f.readline())
#Definition and Usage 定義和用法
#The seek() method sets the current file position in a file stream.
#seek（） 方法設定檔流中的目前檔案位置。
#The seek() method also returns the new postion.
#seek（） 方法還返回新位置。
#Syntax 語法
#file.seek(offset)
#Parameter參數：Values值
#Parameter參數：Description描述
#offset：equired. A number representing the position to set the current file stream position.
#offset：必需。 數位值，表示用於設置當前檔案流位置的位置。
#(10)從第一行第10個字元開始,到行的最後,值不能為負數
#Return the new position:
#返回新位置：
f = open("demofile.txt", "r")
print(f.seek(10))

