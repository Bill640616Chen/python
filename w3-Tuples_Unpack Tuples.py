#https://www.w3schools.com/python/python_tuples_unpack.asp
#Python Unpack Tuples 拆開Tuple的包裝
#Unpacking a Tuple 拆開Tuple的包裝
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
#當我們創建一個tuple時，我們通常會為它分配值。這稱為「包裝」一個tuple：
print("-----------------------------------------Packing a tuple")
#Packing a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits) #('apple', 'banana', 'cherry')
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
#但是，在 Python 中，我們也被允許將值提取回變數。這稱為「拆包」：
print("--------------------------Unpacking a tuple:拆開Tuple的包裝")
#Unpacking a tuple:拆開Tuple的包裝
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)  #apple
print(yellow) #banana
print(red)    #cherry
#Note: The number of variables must match the number of values
# in the tuple, if not, you must use an asterisk to collect 
# the remaining values as a list.
#注意：變數的數量必須與圖中的值數相匹配，如果沒有，則必須使用星號
# 作為清單收集剩餘值。
fruits = ("apple", "banana", "cherry",'*')
(green, yellow, red, white) = fruits
print(green)  #apple
print(yellow) #banana
print(red)    #cherry
print(white) #not enough values to unpack (expected 4, got 3)
#如果變數的數量比值的數量多就會顯示沒有足夠的值被拆包
#所以必須在清單的任何位置,一般都在最面添加'*'號