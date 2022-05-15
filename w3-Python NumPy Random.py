#https://www.w3schools.com/python/numpy/numpy_random.asp
#Random Numbers in NumPy 陣列過濾
#What is a Random Number? 什麼是隨機數？
#Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
#隨機數並不意味著每次都有不同的數位。 隨機意味著無法在邏輯上預測的事物。
#Pseudo Random and True Random.偽隨機和真隨機
#Computers work on programs, and programs are definitive set of instructions. So it means there must be some algorithm to generate a random number as well.
#計算機在程式上工作，程式是權威的指令集。 因此，這意味著必須有某種演算法來生成隨機數。
#If there is a program to generate random number it can be predicted, thus it is not truly random.
#如果存在生成隨機數的程式，則可以預測它，因此它就不是真正的隨機數。
#Random numbers generated through a generation algorithm are called pseudo random.
#通過生成演算法生成的隨機數稱為偽隨機數。
#Can we make truly random numbers?
#我們可以生成真正的隨機數嗎？
#Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
#是的。 為了在我們的計算機上生成一個真正的隨機數，我們需要從某個外部來源獲取隨機數據。 外部來源通常是我們的擊鍵、滑鼠移動、網路數據等。
#We do not need truly random numbers, unless its related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).
#我們不需要真正的隨機數，除非它與安全性（例如加密密鑰）有關或應用的基礎是隨機性（例如數位輪盤賭輪）。
#In this tutorial we will be using pseudo random numbers.
#在本教程中，我們將使用偽隨機數。

#Generate Random Number 生成隨機數
#NumPy offers the random module to work with random numbers.
#NumPy 提供了 random 模組來處理隨機數。
#Generate a random integer from 0 to 100:
print("--------------------產生一個 0 到 100 之間的隨機整數")
#產生一個 0 到 100 之間的隨機整數：
from numpy import random
x = random.randint(100)
print(x)
#from numpy import random 從某模組導入某模組
#randint,random int

#Generate Random Float 生成隨機浮點
#The random module's rand() method returns a random float between 0 and 1.
#random 模組的 rand（） 方法返回 0 到 1 之間的隨機浮點數。
#Generate a random float from 0 to 1:
print("-------------rand(10)--產生 0 到 1 之間的隨機浮點數")
#產生 0 到 1 之間的隨機浮點數：
from numpy import random
x = random.rand(10)
print(x)
#rand()隨機輸出為0-1的float,(10)代表隨機輸出10個float
#若()沒參數,則只會輸出一個,rand是random的縮寫

#Generate Random Array 生成隨機陣列
#In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.
#在 NumPy 中，我們可以使用上例中的兩種方法來創建隨機陣列。
#Integers 整數
#The randint() method takes a size parameter where you can specify the shape of an array.
#randint（） 方法接受 size 參數，您可以在其中指定陣列的形狀。
#Generate a 1-D array containing 5 random integers from 0 to 100:
print("---------------生成一個 1-D 陣列randint(100, size=(5))")
#生成一個 1-D 陣列，其中包含 5 個從 0 到 100 之間的隨機整數：
from numpy import random
x=random.randint(100, size=(5))
print(x)
#在0-100隨機生成

print("----------產生有 3 行的 2-D 陣列randint(100, size=(3, 5))")
#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
#產生有 3 行的 2-D 陣列，每行包含 5 個從 0 到 100 之間的隨機整數：
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)
#在0-100隨機生成

#Floats 浮點數
#The rand() method also allows you to specify the shape of the array.
#rand（） 方法還允許您指定數位的形狀。
#Generate a 1-D array containing 5 random floats:
print("-------------------產生包含 5 個隨機浮點數的 1-D 陣列")
#產生包含 5 個隨機浮點數的 1-D 陣列：
from numpy import random
x = random.rand(5)
print(x)
#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
print("------------產生有 3 行的 2-D 陣列，每行包含 5 個隨機數")
#產生有 3 行的 2-D 陣列，每行包含 5 個隨機數：
from numpy import random
x = random.rand(3, 5)
print(x)

#Generate Random Number From Array 從陣列生成隨機數
#The choice() method allows you to generate a random value based on an array of values.
#choice（） 方法使您可以基於值數位生成隨機值。
#The choice() method takes an array as a parameter and randomly returns one of the values.
print("-----choice（） 方法將陣列作為參數，並隨機返回其中一個值")
#choice（） 方法將陣列作為參數，並隨機返回其中一個值。
#Return one of the values in an array:
#傳回陣列中的值之一：
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)
#The choice() method also allows you to return an array of values.
print("--------------------choice([3, 5, 7, 9], size=(3, 5)")
#choice（） 方法還允許您返回一個值陣列。
#Add a size parameter to specify the shape of the array.
#請添加一個 size 參數以指定數位的形狀。
#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
#生成由陣列參數（3、5、7 和 9）中的值組成的二維數位：
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)
#choice([3, 5, 7, 9], size=(3行, 5隨機在[3, 5, 7, 9]取5個值)
#sns.distplot()distplot是Distribution Plot的縮寫(分佈圖)