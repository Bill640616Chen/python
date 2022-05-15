#https://www.w3schools.com/python/ref_random_triangular.asp
#Random triangular() Method triangular()方法
#傳回兩個給定參數之間的隨機浮點數，您還可以設置模式參數以指定其他兩個參數之間的中點。
#Return a random number between, and included, 20 and 60, but most likely closer to 20:
#返回一個介於 20 和 60 之間且包含的隨機數，但很可能更接近 20：
from math import floor
import random
a = random.triangular(20, 60, 40)
print(floor(a))
#Definition and Usage 定義和用法
#The method returns a random floating number between the two specified numbers (both included), but you can also specify a third parameter, the parameter.triangular()mode
#該方法在兩個指定的數位（均包括在內）之間返回一個隨機的浮動數位，但您也可以指定第三個參數，即參數。triangular()mode
#The parameter gives you the opportunity to weigh the possible outcome closer to one of the other two parameter values.mode
#該參數使您有機會權衡可能的結果，使其更接近其他兩個參數值之一。mode
#The parameter defaults to the midpoint between the two other parameter values, which will not weigh the possible outcome in any direction.mode
#該參數預設為其他兩個參數值之間的中點，這不會在任何方向上權衡可能的結果。mode
#Syntax 語法
#random.triangular(low, high, mode)
#Parameter Values 參數值
#Parameter：Description
#low：Optional. A number specifying the lowest possible outcome.
#Default 0
#自選。指定最低可能結果的數位。
#預設值0
#high：Optional. A number specifying the highest possible outcome.
#Default 1
#自選。指定可能的最高結果的數位。
#預設值 1
#mode：Optional. A number used to weigh the result in any direction.
#Default the midpoint between the low and high values
#自選。用於在任何方向上權衡結果的數位。
#默認低值和高值之間的中點
#隨機輸出數值會接近MODE



