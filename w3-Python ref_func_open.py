#https://www.w3schools.com/python/ref_func_open.asp
#Python open() Function Python open()函數
#Opens a file and returns a file object
#打開檔並返回檔案物件。
#Open a file and print the content:
#開啟檔案並列印內容：
f = open("demofile.txt", 'r')
print(f.read())
#Definition and Usage 定義和用法
#The open() function opens a file, and returns it as a file object.
#open（） 函數打開一個檔，並將其作為檔物件返回。
#Read more about file handling in our chapters about File Handling.
#請在我們的文件處理章節學習更多有關文件處理的知識。
#Syntax 語法
#open(file, mode)
#Parameter參數：Values值
#Parameter參數：Description描述
#file：The path and name of the file
#file：檔案的路徑或名稱。
#mode：A string, define which mode you want to open the file in:
#mode：字串，定義您要在哪種模式下打開檔案：
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"r" - 讀取 - 預設值。 打開檔案進行讀取，如果檔不存在，則發生錯誤。
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"a" - 追加 - 打開文件進行追加，如果不存在則創建檔。
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"w" - 寫入 - 打開檔案進行寫入，如果不存在則創建檔。
#"x" - Create - Creates the specified file, returns an error if the file exist
#"x" - 建立 - 建立指定的檔案，如果檔存在則返回錯誤。
#In addition you can specify if the file should be handled as binary or text mode
#另外，您可以指定檔應以二進位還是文本模式處理
#"t" - Text - Default value. Text mode
#"t" - 文字 - 預設值。 文字模式。
#"b" - Binary - Binary mode (e.g. images)
#"b" - 二進位 - 二進位模式（例如圖像）。
#Related Pages 相關頁面
#Learn how to open files in our Read Files Tutorial
#如何讀取檔
#Learn how to write/create files in our Write/Create Files Tutorial
#如何寫入/創建檔
#Learn how to delete files in our Delete Files Tutorial
#如何刪除檔
#io. UnsupportedOperation： not readable python程式設計中
# 老是這情況，是因為這個代碼中有兩處錯誤： 1、你是用open打開
# 一個文件，此時調用的是w寫入模式，下面使用read是沒有許可權的
# 。 2、使用write寫入一個字元s，但是此時並沒有真正的寫入，而
# 是還存在與記憶體中。




