#https://www.w3schools.com/python/ref_random_sample.asp
#Random sample() Method sample()方法
#傳回序列的給定樣本。
#Return a list that contains any 2 of the items from a list:
#傳回清單，其中包含清單中任意 2 個專案：
import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))
import random
mytuple = ("apple", "banana", "cherry")
print(random.sample(mytuple, k=2))
import random
myset = {"apple", "banana", "cherry"}
print(random.sample(myset, k=2))
#Definition and Usage 定義和用法
#The method returns a list with a randomly selection of a specified number of items from a sequnce.sample()
#該方法返回一個清單，其中包含從順序中隨機選擇指定數量的項。sample()
#Note: This method does not change the original sequence.
#注意：此方法不會更改原始序列。
#Syntax 語法
#random.sample(sequence, k)
#Parameter：Values 參數值
#Parameter：Description
#sequence：Required. A sequence. Can be any sequence: list, set, range etc.
#必填。序列。可以是任何序列：清單，集合，範圍等。
#k：Required. The size of the returned list
#必填。返回清單的大小,不能超出原序列的元素個數
#與choices(k)不同,這裡k意思是出現的次數
