#https://www.w3schools.com/python/python_file_handling.asp
#Python File Handling 檔處理
#File handling is an important part of any web application.
#檔處理是任何 Web 應用程式的重要組成部分。
#Python has several functions for creating, reading, updating, and deleting files.
#Python 有幾個用於創建、讀取、更新和刪除檔的函數。
#File Handling 檔處理
#The key function for working with files in Python is the open() function.
#在 Python 中使用檔案的關鍵函數是 open（） 函數。
#The open() function takes two parameters; filename, and mode.
#open（） 函數有兩個參數：檔名和模式。
#There are four different methods (modes) for opening a file:
#有四種打開檔的不同方法（模式）：
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"r" - 讀取 - 預設值。 打開檔進行讀取，如果檔不存在則報錯。
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"a" - 追加 - 打開供追加的檔，如果不存在則創建該檔。
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"w" - 寫入 - 打開檔案進行寫入，如果檔案不存在則創建該檔。
#"x" - Create - Creates the specified file, returns an error if the file exists
#"x" - 建立 - 建立指定的檔案，如果檔存在則返回錯誤。
#In addition you can specify if the file should be handled as binary or text mode
#此外，您可以指定檔是應該作為二進位還是文本模式進行處理。
#"t" - Text - Default value. Text mode
#"t" - 文字 - 預設值。 文字模式。
#"b" - Binary - Binary mode (e.g. images)
#"b" - 二進位 - 二進位模式（例如圖像）。
#Syntax 語法
#To open a file for reading it is enough to specify the name of the file:
#開啟檔案閱讀就足以指定檔案的名稱：
f = open("demofile.txt","a")
#The code above is the same as:
#以上代碼等同於：
f = open("demofile.txt", "rt") #= f = open("demofile.txt")
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
#因為 「r」 （讀取）和 「t」 （文字）是預設值，所以不需要指定它們。
#Note: Make sure the file exists, or else you will get an error.
#註釋：請確保檔存在，否則您將收到錯誤消息。
