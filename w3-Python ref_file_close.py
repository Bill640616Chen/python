#https://www.w3schools.com/python/ref_file_close.asp
#Python File close() Method Python關閉檔案
#Closes the file
#關閉檔案。
#Close a file after it has been opened:
#開啟檔案後關閉檔案：
f = open("demofile.txt", "r")
print(f.read())
f.close()
#Definition and Usage 定義和用法
#The close() method closes an open file.
#close（） 方法關閉打開的檔案。
#You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
#您應該始終關閉檔，在某些情況下，由於存在緩衝，對檔所做的更改可能要等到您關閉檔后才能顯示。
#Syntax 語法
#file.close()
#Parameter參數：Values值
#No parameters 無參數
