#https://www.w3schools.com/python/gloss_python_try_finally.asp
#Python Try Finally 最後嘗試
#The block, if specified, will be executed regardless if the try block raises an error or not.finally
#如果指定了該塊，則無論 try 塊是否引發錯誤，都將執行該塊。finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#This can be useful to close objects and clean up resources:
#這對於關閉物件和清理資源非常有用：
print('-------------分隔線------------')
#Try to open and write to a file that is not writable:
#嘗試開啟並寫入不可寫的檔案：
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
#The program can continue, without leaving the file object open.
#程式可以繼續，而無需使文件物件保持打開狀態。
#Related Pages 相關頁面
#Python Try Except Tutorial Python 嘗試教程除外
#https://www.w3schools.com/python/python_try_except.asp
#Error Handling 錯誤處理
#https://www.w3schools.com/python/gloss_python_error_handling.asp
#Handle Many Exceptions 處理許多異常
#https://www.w3schools.com/python/gloss_python_try_except.asp
#Try Else 嘗試其他
#https://www.w3schools.com/python/gloss_python_try_else.asp
#raise 引發
#https://www.w3schools.com/python/gloss_python_raise.asp