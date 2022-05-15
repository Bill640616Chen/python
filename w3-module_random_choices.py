#https://www.w3schools.com/python/ref_random_choices.asp
#Random choices() Method choices()方法
#傳回一個清單，其中包含給定序列中的隨機選擇。
#Return a list with 14 items.
#返回包含14個項目的清單。
#The list should contain a randomly selection of the values from a specified list, and there should be 10 times higher possibility to select "apple" than the other two:
#該清單應包含從指定清單中隨機選擇的值，並且選擇「apple」的可能性應比其他兩個高10倍：
import random
mylist = ["apple", "banana", "cherry","melon"]
print(random.choices(mylist, weights=[1, 2, 3,2], k = 5))
print(random.choices(mylist, k = 5))
import random
mylist = ["apple", "banana", "cherry","melon"]
print(random.choices(mylist, cum_weights=[2, 1, 3,4], k = 5))
import random
mylist = ["apple", "banana", "cherry","melon"]
print(random.choices(mylist))

#weights =[裡面的個數要與清單相同]
#Definition and Usage 定義和用法
#The method returns a list with the randomly selected element from the specified sequence.choices()
#該方法返回一個清單，其中包含從指定序列中隨機選擇的元素。choices()
#You can weigh the possibility of each result with the weights parameter or the cum_weights parameter.
#您可以使用權重參數或cum_weights參數來權衡每個結果的可能性。
#The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
#序列可以是字串、範圍、清單、元組或任何其他類型的序列。
#Syntax 語法
#random.choices(sequence, weights=None, cum_weights=None, k=1)
#Parameter：Values 參數值
#Parameter：Description
#sequence：Required. A sequence like a list, a tuple, a range of numbers etc.
#必填。清單、元組、數位範圍等序列。
#weights：Optional. A list were you can weigh the possibility for each value.
#Default None
#自選。一個清單是你可以權衡每個值的可能性。
#默認無
#cum_weights：Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
#Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
#Default None
#自選。一個清單是你可以權衡每個值的可能性，只有這次的可能性是累積的。
#示例：正常權重清單：[2， 1， 1] 與此cum_weights清單相同;[2, 3, 4].
#默認無
#k：Optional. An integer defining the length of the returned list
#自選。定義返回清單長度的整數

