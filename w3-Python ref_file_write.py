#https://www.w3schools.com/python/ref_file_write.asp
#Python File write() Method Python write
#Writes the specified string to the file
#把指定的字串寫入檔案。
#Open the file with "a" for appending, then add some text to the file:
#以 「a」 開啟檔案進行追加，然後向該檔案添加一些文字：
f = open("demofile2.txt", "a")
f.write("See you soon!")
f.close()
#open and read the file after the appending:
#開啟並閱讀附加後的檔案：
f = open("demofile2.txt", "r")
print(f.read())
#Definition and Usage 定義和用法
#The write() method writes a specified text to the file.
#write（） 方法將指定的文字寫入檔案。
#Where the specified text will be inserted depends on the file mode and stream position.
#指定的文字將插入的位置取決於檔案模式和流位置。
#"a": The text will be inserted at the current file stream position, default at the end of the file.
#"a"：文本將插入目前的檔流的位置，默認情況下插入檔的末尾。
#"w": The file will be emptied before the text will be inserted at the current file stream position, default 0.
#"w"：在將文本插入目前的檔流位置（預設為 0）之前，將清空檔。
#Syntax 語法
#file.write(byte)
#Parameter參數：Values值
#Parameter參數：Description描述
#byte：The text or byte object that will be inserted.
#byte：將要插入的文字或位元組物件。
#More examples
#The same example as above, but inserting a line break before the inserted text:
#與上例相同，但在插入的文本前面插入換行：
f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()
#open and read the file after the appending:
#開啟並閱讀附加後的檔案：
f = open("demofile2.txt", "r")
print(f.read())