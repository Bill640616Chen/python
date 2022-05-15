#https://www.w3schools.com/python/python_file_write.asp
#Python Write files 寫入檔
#Write to an Existing File 寫入現有檔
#To write to an existing file, you must add a parameter to the open() function:
#如需寫入已有的文件，必須向open（） 函數添加參數：
#"a" - Append - will append to the end of the file
#"a" - 追加 - 會追加到檔的末尾
#"w" - Write - will overwrite any existing content
#"w" - 寫入 - 會覆蓋任何已有的內容
#Open the file "demofile2.txt" and append content to the file:
#開啟檔案 「demofile2.txt」 並將內容追加到檔案中：
f = open("demofile2.txt", "a")
#f = open("demofile2.txt", "a")
#"demofile2.txt",後面只能跟一個參數...
#如果檔不存在,就自動建立
f.write("Now the file has more content!")
f = open("demofile2.txt", "w")
#相同內容會被覆蓋
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Open the file "demofile3.txt" and overwrite the content:
#開啟檔案 「demofile3.txt」 並覆蓋內容：
f = open("demofile3.txt", "w")
#相同內容會被覆蓋
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
#Create a New File 創建新檔
#To create a new file in Python, use the open() method, with one of the following parameters:
#如需在 Python 中創建新檔，請使用 open（） 方法，並使用以下參數之一：
#Character	Meaning
#'r'    	open for reading (default)
#打開為了讀取(預設)唯讀
#'w'    	will create a file if the specified file does not exist
#如果指定的檔不存在就建一個檔
#'x'    	will create a file, returns an error if the file exist
#建立一個新的檔，如果檔案存在就傳回錯誤
#'a'    	open for writing, appending to the end of the file
#           if it exists,will create a file if the specified 
#           file does not exist
#打開用於編寫，如果檔存在，則附著在檔的末尾,如果檔不存在,就建立
#'b'    	binary mode
#二進位模式
#'t'    	text mode (default)
#文字模式（預設）
#'+'	    open a disk file for updating (reading and writing)
#開啟磁碟檔案進行更新（閱讀與寫作）
#'U'	    universal newline mode (deprecated)
#通用換行模式（棄用）

#Create a file called "myfile.txt":
f = open("demofile4.txt", "x")
#"x"檔案存在,傳回錯誤[Errno 17] File exists: 'demofile4.txt'
#Result: a new empty file is created!
#Create a new file if it does not exist:
f = open("demofile4.txt", "w")