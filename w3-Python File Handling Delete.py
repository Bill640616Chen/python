#https://www.w3schools.com/python/python_file_remove.asp
#Python Delete files 刪除檔案
#Delete a File 刪除檔案
#To delete a file, you must import the OS module, and run its os.remove() function:
#如需刪除檔，必須導入OS模組，並運行其os.remove（） 函數：
#Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

#Check if File exist:檢查檔是否存在
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
#避免錯誤，您可能需要在嘗試刪除檔案之前檢查該檔案是否存在：
#Check if file exists, then delete it:
#檢查檔案是否存在，然後刪除它：
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#Delete Folder 刪除檔案
#To delete an entire folder, use the os.rmdir() method:
#如需刪除整個資料夾，請使用os.rmdir（） 方法：
#Remove the folder "myfolder":
#刪除資料夾 「myfolder」
import os
os.rmdir("myfolder")

#系統找不到指定的檔案。: 'myfolder'  
#Note: You can only remove empty folders.