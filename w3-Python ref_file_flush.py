#https://www.w3schools.com/python/ref_file_flush.asp
#Python File flush() Method Python flush()
#Flushes the internal buffer
#刷新內部緩衝區。
#You can clear the buffer when writing to a file:
#您可以在寫入檔案時清除緩衝：
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")
f.flush()
f.write("\n...and another one!")
#Definition and Usage 定義和用法
#The flush() method cleans out the internal buffer.
#flush（） 方法清除內部緩衝。
#Syntax 語法
#file.flush()
#Parameter參數：Values值
#No parameters無參數。



