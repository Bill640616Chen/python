#https://www.w3schools.com/python/python_file_handling.asp
#Python Read files 讀取檔
#Open a File on the Server Python 在伺服器上打開檔
#Assume we have the following file, located in the same folder as Python:
#假設我們有以下文件，位於與 Python 相同的資料夾中：
#demofile.txt
#["Hello! Welcome to demofile.txt",
#"This file is for testing purposes.",
#"Good Luck!"]
#To open the file, use the built-in open() function.
#如需打開檔，請使用內建的open（） 函數。
#The open() function returns a file object, which has a read() method for reading the content of the file:
print("------------------------------------open和read()")
#open（） 函數傳回檔案物件，此物件有一個 read（） 方法用於讀取檔案的內容：
f = open("demofile.txt", "r")
print(f.read())
#If the file is located in a different location, you will have to specify the file path, like this:
#如果檔案的位置在不同的位置,你將要指定檔案的路徑,像這樣：
print("-------------------------------在不同的位置打開檔案")
#Open a file on a different location:
#在不同的位置打開檔案
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())

print("--------Read Only Parts of the File 唯讀檔案的一部分")
#Read Only Parts of the File 唯讀檔案的一部分
#By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#預設情況下，read（） 方法返回整個文本，但您也可以指定要返回的字元數：
#Return the 5 first characters of the file:
#傳回檔案中的前五個字元：
f = open("demofile.txt", "r")
print(f.read(5))
