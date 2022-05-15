#https://www.w3schools.com/python/ref_random_randint.asp
#Random randint() Method randint()方法
#傳回給定範圍之間的隨機數。
#Return a number between 3 and 9 (both included):
#返回一個介於 3 和 9 之間的數位（均包括在內）：
import random
print(random.randint(3, 5))
#Definition and Usage 定義和用法
#The method returns an integer number selected element from the specified range.randint()
#該方法返回從指定範圍中選擇的元素的整數。randint()
#Note: This method is an alias for .randrange(start, stop+1)
#注意：此方法是 的別名。randrange(start, stop+1)
#Syntax 語法
#random.randint(start, stop)
#Parameter：Values 參數值
#Parameter：Description
#start：Required. An integer specifying at which position to start.
#必填。一個整數，指定從哪個位置開始。
#stop：Required. An integer specifying at which position to end.
#必填。一個整數，指定在哪個位置結束。
print('會出現stop的數字')

