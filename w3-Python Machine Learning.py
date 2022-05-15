#https://www.w3schools.com/python/python_ml_getting_started.asp
#Python Machine Learning 機器學習
#Machine Learning is making the computer learn from studying data and statistics.
#機器學習使計算機從研究數據和統計學中學習。
#Machine Learning is a step into the direction of artificial intelligence (AI).
#機器學習是朝著人工智慧 （AI） 方向邁出的一步。
#Machine Learning is a program that analyses data and learns to predict the outcome.
#機器學習是一個分析數據並學會預測結果的程式。
#Where To Start?從哪裡開始？
#In this tutorial we will go back to mathematics and study statistics, and how to calculate important numbers based on data sets.
#在此教程中，我們將回到數學和學習統計，以及如何根據數據集計算重要數位。
#We will also learn how to use various Python modules to get the answers we need.
#我們還將學習如何使用各種 Python 模組來獲得我們需要的答案。
#And we will learn how to make functions that are able to predict the outcome based on what we have learned.
#我們將學習如何使功能能夠根據我們學到的知識預測結果。
#Data Set 數據集合
#In the mind of a computer, a data set is any collection of data. It can be anything from an array to a complete database.
#在計算機的頭腦中，數據集是任何數據集。它可以是任何東西，從陣列到一個完整的資料庫。
#Example of an array: 陣列示例：
[99,86,87,88,111,86,103,87,94,78,77,85,86]
#Example of a database:
'''
Carname	Color	Age	    Speed	AutoPass
BMW	    red	    5	    99	    Y
Volvo	black	7	    86	    Y
VW	    gray	8	    87	    N
VW	    white	7	    88	    Y
Ford	white	2	    111	    Y
VW  	white	17	    86	    Y
Tesla	red	    2	    103	    Y
BMW	    black	9	    87	    Y
Volvo	gray	4	    94	    N
Ford	white	11	    78  	N
Toyota	gray	12	    77      N
VW	    white	9	    85  	N
Toyota	blue	6	    86  	Y
'''
#By looking at the array, we can guess that the average value is probably around 80 or 90, and we are also able to determine the highest value and the lowest value, but what else can we do?
#通過查看陣列，我們可以猜到平均值大概在80或90左右，我們還能夠確定最高值和最低值，但我們還能做什麼呢？
#And by looking at the database we can see that the most popular color is white, and the oldest car is 17 years, but what if we could predict if a car had an AutoPass, just by looking at the other values?
#通過查看資料庫，我們可以看到，最流行的顏色是白色，最老的汽車是17年，但如果我們可以預測，如果一輛車有自動通行證，只是看看其他值呢？
#That is what Machine Learning is for! Analyzing data and predicting the outcome!
#這就是機器學習的意義！分析數據並預測結果！
#In Machine Learning it is common to work with very large data sets. In this tutorial we will try to make it as easy as possible to understand the different concepts of machine learning, and we will work with small easy-to-understand data sets.
#在機器學習中，通常與非常大的數據集配合用。在此教程中，我們將嘗試盡可能容易地理解機器學習的不同概念，我們將處理易於理解的小數據集。
#Data Types數據類型
#To analyze data, it is important to know what type of data we are dealing with.
#要分析數據，瞭解我們正在處理的是什麼類型的數據非常重要。
#We can split the data types into three main categories:
#我們可以將資料類型分為三個主要類別：
#Numerical   數值的
#Categorical 分類
#Ordinal     序數
#Numerical data are numbers, and can be split into two numerical categories:
#數位資料是數位，可分為兩個數字類別：
#Discrete Data離散數據
#- numbers that are limited to integers. Example: The number of cars passing by.
#- 僅限於整數的數位。示例：經過的汽車數量。
#Continuous Data 連續數據
#- numbers that are of infinite value. Example: The price of an item, or the size of an item
#- 具有無限價值的數位。範例：項目的價格或專案大小
#Categorical data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.
#分類數據是無法相互測量的值。示例：顏色值或任何是/否值。
#Ordinal data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.
#普通數據就像絕對數據，但可以相互測量。例如：A 優於 B 等的學校成績。
#By knowing the data type of your data source, you will be able to know what technique to use when analyzing them.
#通過了解數據源的數據類型，您將能夠知道在分析數據源時使用什麼技術。
#You will learn more about statistics and analyzing data in the next chapters.
#在接下來的幾章中，您將詳細了解統計數據和分析數據。

