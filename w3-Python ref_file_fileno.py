#https://www.w3schools.com/python/ref_file_fileno.asp
#Python File fileno() Method Python fileno()
#Returns a number that represents the stream, from the operating system's perspective
#從操作系統的角度返回表示流的數字。
#Return the file descriptor of the stream:
#傳回流的檔案描述符：
f = open("demofile.txt", "r")
print(f.fileno())
#Definition and Usage 定義和用法
#The fileno() method returns the file descriptor of the stream, as a number.
#fileno（） 方法以數位形式返回流的檔描述符。
#An error will occur if the operator system does not use a file descriptor.
#如果作業系統不使用檔描述符，將發生錯誤。
#Syntax 語法
#file.fileno()
#Parameter參數：Values值
#No parameters無參數。


