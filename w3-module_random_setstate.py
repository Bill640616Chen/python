#https://www.w3schools.com/python/ref_random_setstate.asp
#Random setstate() Method setstate()方法
#恢復隨機數生成器的內部狀態。
#Capture and restore the state of the random number generator:
#擷取並恢復隨機數產生器的狀態：
import random
#print a random number:
print(random.random())
#capture the state:
state = random.getstate()
#print another random number:
print(random.random())
#restore the state:
random.setstate(state)
#and the next random number should be the same as when you captured the state:
print(random.random())
#Definition and Usage 定義和用法
#The method is used to restore the state of the random number generator back to the specified statesetstate()
#該方法用於將隨機數產生器的狀態恢復到指定的狀態setstate()
#Use the method to capture the stategetstate()
#使用該方法捕獲狀態getstate()
#Syntax 語法
#random.setstate(state)
#Parameter：Values 參數值
#Parameter：Description
#state：Required. A state object. the setstate() method will restore the state of  the random number generator back to this sate.
#必填。狀態物件。setstate（） 方法會將隨機數產生器的狀態恢復到此 sate。

