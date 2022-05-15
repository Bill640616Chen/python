#https://www.w3schools.com/python/ref_file_writelines.asp
#Python File writelines() Method Python writelines
#Writes a list of strings to the file
#把字串清單寫入檔案。
#Open the file with "a" for appending, then add a list of texts to append to the file:
#以 「a」 開啟檔案列附加，然後添加文字清單來附加到該檔案：
f = open("demofile3.txt", "a")
f.writelines(["See you soon!", "\nOver and out."])
f.close()
#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
#Definition and Usage 定義和用法
#The writelines() method writes the items of a list to the file.
#writelines（） 方法將清單的專案寫入檔。
#Where the texts will be inserted depends on the file mode and stream position.
#文本插入的位置取決於檔模式和流位置。
#"a":  The texts will be inserted at the current file stream position, default at the end of the file.
#"a"：文本將插入目前的檔流的位置，默認情況下插入檔的末尾。
#"w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.
#"w"：在將文本插入目前的檔流位置（預設為 0）之前，將清空檔。
#Syntax 語法
#file.writelines(list)
#Parameter參數：Values值
#Parameter參數：Description描述
#list：The list of texts or byte objects that will be inserted.
#list：與上例相同，但對每個清單項插入換行：