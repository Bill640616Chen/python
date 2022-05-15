#https://www.w3schools.com/python/ref_random_randrange.asp
#Random randrange() Method randrange()方法
#傳回給定範圍之間的隨機數。
#Return a number between 3 and 9:
#返回一個介於 3 和 9 之間的數位：
import random
print(random.randrange(3,90,7))
print('不會出現stop的數字')
print(random.randrange(1,3))
#Definition and Usage 定義和用法
#The method returns a randomly selected element from the specified range.randrange()
#該方法返回從指定範圍中隨機選擇的元素。randrange()
#Syntax 語法
#random.randrange(start, stop, step)
#Parameter：Values 參數值
#Parameter：Description
#start：Optional. An integer specifying at which position to start.
#Default 0
#自選。一個整數，指定從哪個位置開始。
#預設值0
#stop：Required. An integer specifying at which position to end.
#必填。一個整數，指定在哪個位置結束。
#不會出現stop的數字
#step：Optional. An integer specifying the incrementation.
#Default 1
#自選。指定增量的整數。
#預設值 1

