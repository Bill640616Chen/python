#https://www.w3schools.com/python/ref_random_choice.asp
#Random choice() Method choice()方法
#傳回給定序列中的隨機元素。
#Return a random element from a list:
#從清單中傳回隨機元素：
import random
mylist = [["apple", "banana", "cherry"],["apple"],["banana", "cherry"]]
print(random.choice(mylist))
#Definition and Usage 定義和用法
#The choice() method returns a randomly selected element from the specified sequence.
#該方法返回從指定序列中隨機選擇的元素。choice()
#The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
#序列可以是字串、範圍、清單、元組或任何其他類型的序列。
#Syntax 語法
#random.choice(sequence)
#Parameter：Values 參數值
#Parameter：Description
#sequence：Required. A sequence like a list, a tuple, a range of numbers etc.
#必填。清單、元組、數位、也可以是n維陣列範圍等序列。
#序列不可是set,dict
#Return a random character from a string:
#從字串中傳回隨機字元：
import random
x = "WELCOME"
print(random.choice(x))
