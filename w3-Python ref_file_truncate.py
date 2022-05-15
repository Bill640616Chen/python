#https://www.w3schools.com/python/ref_file_truncate.asp
#Python File truncate() Method Python truncate
#Resizes the file to a specified size
#把文件調整為指定的大小。
#Open the file with "a" for appending, then truncate the file to 20 bytes:
#以 「a」 開啟檔案進行追加，然後將檔截斷為 20 個字節：
f = open("demofile2.txt", "a")
f.truncate(20)
f.close()
#刪除第20個字元之後的字元
#open and read the file after the truncate:
#開啟並閱讀截斷後的檔案：
f = open("demofile2.txt", "r")
print(f.read())
#Definition and Usage 定義和用法
#The truncate() method resizes the file to the given number of bytes.
#truncate（） 方法將檔大小調整為給定的位元元組數。
#If the size is not specified, the current position will be used.
#如果未指定大小，將使用當前位置。
#Syntax 語法
#file.truncate(size)
#Parameter參數：Values值
#Parameter參數：Description描述
#size：Optional. The size of the file (in bytes) after the truncate. Default None, which means the current file stream position.
#size：可選。 截斷後檔的大小（以位元組計）。 預設值：None，表示當前檔流位置。
