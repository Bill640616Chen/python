#https://www.w3schools.com/python/ref_random_getstate.asp
#Random getstate() Method getstate()方法
#傳回隨機數生成器的當前內部狀態。
#Return the current state of the random generator:
#傳回隨機產生器的目前狀態：
import random
print(random.getstate())
#Definition and Usage 定義和用法
#The method returns an object with the current state of the random number generator.getstate()
#該方法返回具有隨機數生成器當前狀態的物件。getstate()
#Use this method to capture the state, and use the method, with the captured state, to restore the state setstate()
#使用此方法捕獲狀態，並將該方法與捕獲的狀態結合使用來還原狀態 setstate()
#Syntax 語法
#random.getstate()
#Parameter Values 參數值
#No parameter values 無參數值