#https://www.w3schools.com/python/ref_file_readline.asp
#Python File readline() Method Python readline
#Returns one line from the file
#返回檔中的一行。
#Read the first line of the file "demofile.txt":
#讀取檔案 「demofile.txt」 的首行：
f = open("demofile.txt", "r")
print(f.readline())
#Definition and Usage 定義和用法
#The readline() method returns one line from the file.
#readline（） 方法從檔返回一行。
#You can also specified how many bytes from the line to return, by using the size parameter.
#您還可以使用 size 參數指定要從該行返回多少位元組。
#Syntax 語法
#file.readline(size)
#Parameter參數：Values值
#Parameter參數：Description描述
#size：Optional. The number of bytes from the line to return. Default -1, which means the whole line.
#size：可選。 從行返回的位元組數。 默認值 -1，表示整行。
#Call readline() twice to return both the first and the second line:
#調用 readline（） 兩次以返回第一行和第二行：
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
#Return only the five first bytes from the first line:
#僅返回第一行的前五個字節：
f = open("demofile.txt", "r")
print(f.readline(5))






