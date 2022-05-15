#https://www.w3schools.com/python/gloss_python_function_recursion.asp
#Function Recursion 遞迴
#Python also accepts function recursion, which means a defined function can call itself.
#Python 也接受函數遞歸，這意味著定義的函數可以調用自己。
#Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
#遞歸是一個常見的數學和程式設計概念。這意味著一個函數會自行調用。這具有這樣一種含義，即您可以循環數據以達到結果。
#The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
#開發人員應非常小心復發，因為編寫永不終止的功能或使用過多記憶體或處理器電源的功能很容易。但是，當編寫正確時，遞歸可以是一種非常高效和數學上優雅的程式設計方法。
#In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#在此示例中，tri_recursion（）是我們定義的自稱為"重複"的函數。我們使用k變數作為數據，每次我們復發時都會減損（-1）。當條件不超過 0（即當條件為 0 時），遞歸結束。
#To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
#對於新的開發人員來說，它可能需要一些時間來計算出它究竟是如何工作的，找出答案的最佳方法是測試和修改它。
#Recursion Example
#遞歸示例
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    #k-1改成k+1時會出現錯RecursionError:maximum recursion depth exceeded in comparison
    #遞迴錯誤：超過最大遞迴深度
    print(result)
  else:
    result = 1
#else:這條件一定要設,否則會出現錯誤
  return result
print("\n\nRecursion Example Results")
tri_recursion(3)
#2,當代入1時,1+tri_recursion(0),tri_recursion(0)傳回1
#4,當代入2時,2+tri_recursion(1),tri_recursion(1)傳回2
#7,當代入3時,3+tri_recursion(2),tri_recursion(2)傳回4
#Related Pages 相關頁面
#Python Functions Tutorial Python 函數教程
#https://www.w3schools.com/python/python_functions.asp
#Function 函數 
#https://www.w3schools.com/python/gloss_python_function.asp
#Call a Function 調用函數 
#https://www.w3schools.com/python/gloss_python_function_call.asp
#Function Arguments 函數參數
#https://www.w3schools.com/python/gloss_python_function_arguments.asp
#*args *阿格斯
#https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
#Keyword Arguments 關鍵字參數
#https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp
#*kwargs *克瓦格斯
#https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp
#Default Parameter Value 預設參數值
#https://www.w3schools.com/python/gloss_python_function_default_parameter.asp
#Passing a List as an Argument 將清單作為參數傳遞
#https://www.w3schools.com/python/gloss_python_function_passing_list.asp
#Function Return Value 函數返回值
#https://www.w3schools.com/python/gloss_python_function_return_value.asp
#The pass Statement i Functions pass語句 i 函數
#https://www.w3schools.com/python/gloss_python_function_pass.asp
