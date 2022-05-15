#https://www.w3schools.com/python/python_variables_multiple.asp
#多個變數的多個值
#Python 允許您在一行中為多個變數分配值：
x, y, z ,a = "Orange", "Banana", "Cherry",3
print(x)
print(y)
print(z)
print(a)
#注意：確保變數數與值數相匹配，否則您將出錯。

#多個變數的一個值
#您可以在一行中為多個變數分配相同的值：
x = y = z = "Orange,Banana"
print(x)
print(y)
print(z)

#拆開集合
#如果您的清單中包括一系列值，則圖普等。Python 允許您將值提取到變數中。這叫做拆包。
fruits = ["apple", "banana", "cherry"]#列表
x, y, z = fruits
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]#列表
#x為什麼是取列表最後的值
x = fruits
x=y=z
#x, y, z = fruits,是取這行對應的位置
#若x=z=y,取的是y第1位置的值banana,若x=y=z,取的是位置2的值cherry
#若輸出要一樣,在x=y=z上面打z=fruits重新賦值就可以了
print(x)
print(y)
print(z)
#['apple', 'banana', 'cherry']
#['apple', 'banana', 'cherry']
#['apple', 'banana', 'cherry']
