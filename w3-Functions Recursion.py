#https://www.w3schools.com/python/python_functions.asp
#Python Recursion 遞迴
#Recursion 遞迴
#Python also accepts function recursion, which means a 
# defined function can call itself.
#Python 也接受函數遞迴，這意味著定義的函數可以調用自己。
#Recursion is a common mathematical and programming concept.
# It means that a function calls itself. This has the benefit
# of meaning that you can loop through data to reach a result.
#遞迴是一個常見的數學和程式設計概念。這意味著一個函數會自行調用。
#這具有這樣一種含義，即您可以迴圈數據以達到結果。
#The developer should be very careful with recursion as 
# it can be quite easy to slip into writing a function 
# which never terminates, or one that uses excess amounts 
# of memory or processor power. However, when written 
# correctly recursion can be a very efficient and
# mathematically-elegant approach to programming.
#開發人員面對遞歸應非常小心，因為它可以很容易編寫永不終止的
# 函數或使用過多記憶體或處理器電源的。但是，當編寫正確時，
# 遞迴可以是一種非常高效和數學上優雅的程式設計方法。
#In this example, tri_recursion() is a function that we 
# have defined to call itself ("recurse"). We use the k 
# variable as the data, which decrements (-1) every time 
# we recurse. The recursion ends when the condition is not 
# greater than 0 (i.e. when it is 0).
#在此示例中，tri_recursion（）是我們定義的自稱為"重複"的函數。
# 我們使用 k 變數作為數據，每次遞迴時都會減損 （-1）。當條件不
# 超過 0（即當條件為 0 時），遞迴結束。
#To a new developer it can take some time to work out how 
# exactly this works, best way to find out is by testing 
# and modifying it.
#對於新的開發人員來說，它可能需要一些時間來計算出它究竟是
# 如何工作的，找出答案的最佳方法是測試和修改它。
#Recursion Example 遞迴範例
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results,測試(k-1)決定由哪個數字先代入")
tri_recursion(6)
#當6代入def tri_recursion(k):這時K=6
#進入if(6 > 0):判斷為True
#再執行result = 6 + tri_recursion(6 - 1)
#print(result) = 6 +
#此時tri_recursion(5)再回進入if(5 > 0):判斷為True:
#此時的k=5,再執行result = 5 + tri_recursion(5 - 1)
#print(result) = 6 + 5
#此時tri_recursion(4)再回進入if(4 > 0):判斷為True:
#此時的k=4,再執行result = 4 + tri_recursion(4 - 1)
#print(result) = 6 + 5 + 4
#此時tri_recursion(3)再回進入if(3 > 0):判斷為True:
#此時的k=3,再執行result = 3 + tri_recursion(3 - 1)
#print(result) = 6 + 5 + 4 + 3
#此時tri_recursion(2)再回進入if(2 > 0):判斷為True:
#此時的k=2,再執行result = 2 + tri_recursion(2 - 1)
#print(result) = 6 + 5 + 4 + 3 + 2
#此時tri_recursion(1)再回進入if(1 > 0):判斷為True:
#此時的k=1,再執行result = 1 + tri_recursion(1 - 1)
#print(result) = 6 + 5 + 4 + 3 + 2 + 1
#此時tri_recursion(0)再回進入if(0 > 0):判斷為False:
#直接到return result
#所以輸出是21
#tri_recursion(k - 1)就明白每次遞過是哪個數字開始
#此例是6,因為k-1,所以依序是6,5,4,3,2,1
#此例由6開始註解,幫目己理解,k應該是從1先被代入

#依此類推
#當k=1時,resuslt=1+0           輸出為1
#當k=2時,resuslt=2+1+0         輸出為3
#當k=3時,resuslt=3+2+1+0       輸出為6
#當k=4時,resuslt=4+3+2+1+0     輸出為10
#當k=5時,resuslt=5+4+3+2+1+0   輸出為15
#當k=6時,resuslt=6+5+4+3+2+1+0 輸出為21

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 2)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results,測試(k-2)決定由哪個數字先代入")
tri_recursion(6)
#此例是6,因為k-2,所以依序是6,4,2
#從2開始代入
#當2代入def tri_recursion(k):這時K=2
#進入if(2 > 0):判斷為True
#再執行result = 2 + tri_recursion(2 - 2)
#此時tri_recursion(0)再回進入if(0 > 0):判斷為False
#進入else: result = 0
#進入return result
#進入print(result)輸出2,此時result是2
#本例的輸出為2,6,12

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 3)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results,測試(k-3)決定由哪個數字先代入")
tri_recursion(6)
#此例是6,因為k-3,所以依序是6,3
#本例的輸出是3,9
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 4)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results,測試(k-4)決定由哪個數字先代入")
tri_recursion(6)
#此例是6,因為k-4,所以依序是6,2
#本例的輸出是2,8