#https://www.w3schools.com/python/ref_random_seed.asp
#Random seed() Method seed（）方法
#初始化隨機數產生器。
#Set the seed value to 10 and see what happens:
#將種子值設置為 10，看看會發生什麼情況：
import random
random.seed(10)
print(random.random())
#Definition and Usage 定義和用法
#The seed() method is used to initialize the random number generator.
#隨機數生成器需要一個以數位開頭的數位（種子值），以便能夠生成隨機數。
#The random number generator needs a number to start with (a seed value), to be able to generate a random number.
#預設情況下，隨機數產生器使用目前系統時間。
#By default the random number generator uses the current system time.
#預設情況下，隨機數產生器使用目前系統時間。
#Use the seed() method to customize the start number of the random number generator.
#使用 seed（） 方法自訂隨機數產生器的起始編號。
#Note: If you use the same seed value twice you will get the same random number twice. See example below
#注意：如果兩次使用相同的種子值，則兩次將獲得相同的隨機數。請參閱下面的範例
#Syntax 語法
#random.seed(a, version)
#Parameter參數：Values值
#Parameter：Description
#a：Optional. The seed value needed to generate a random number.
#If it is an integer it is used directly, if not it has to be converted into an integer.
#Default value is None, and if None, the generator uses the current system time.
#自選。生成隨機數所需的種子值。
#如果它是整數，則直接使用，如果不是，則必須將其轉換為整數。
#默認值為 None，如果為 None，則產生器使用當前系統時間。
#version：An integer specifying how to convert the a parameter into a integer.
#Default value is 2
#一個整數，指定如何將 a 參數轉換為整數。
#預設值為 2
#Demonstrate that if you use the same seed value twice, you will get the same random number twice:
#證明如果兩次使用相同的種子值，您將獲得兩次相同的隨機數：
import random
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
