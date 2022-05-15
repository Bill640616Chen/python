#https://www.w3schools.com/python/pandas/pandas_correlations.asp
#Pandas Data Correlations 數據相關性
#Finding Relationships 查找關係
#A great aspect of the Pandas module is the corr() method.
#熊貓模組的一大方面是相關性（）方法。
#The corr() method calculates the relationship between each column in your data set.
#corr（） 方法計算數據集中每個列之間的關係。
#The examples in this page uses a CSV file called: 'data.csv'.
#此頁面中示例使用稱為「數據.csv」的 CSV 檔。
#Download data.csv. or Open data.csv
#下載數據.csv。或打開數據.csv
#Show the relationship between the columns:
print("-----------返回真實的每一行是重複的， 否則錯誤")
#顯示列之間的關係：
import pandas as pd
df = pd.read_csv('data1.csv')
print(df.corr())
#Note: The corr() method ignores "not numeric" columns.
#注意：corr（） 方法忽略"非數字"欄。
#Result Explained 結果解釋
#The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.
#corr（） 方法的結果是一個表，其中有很多數字，表示兩列之間的關係有多好。
#The number varies from -1 to 1.
#數字從 -1 到 1 不等。
#1 means that there is a 1 to 1 relationship 
# (a perfect correlation), and for this data set, 
# each time a value went up in the first column, 
# the other one went up as well.
#1 表示存在 1 到 1 關係（完美關聯），對於此數據集，
# 每次第一列中值上升時，另一列也會上升。
#0.9 is also a good relationship, and if you 
# increase one value, the other will probably 
# increase as well.
#0.9 也是一個很好的關係，如果你增加一個值，另一個
# 可能也會增加。
#-0.9 would be just as good relationship as 0.9, 
# but if you increase one value, the other will 
# probably go down.
#-0.9 將和 0.9 一樣好的關係， 但如果你增加一個值， 
# 另一個可能會下降。
#0.2 means NOT a good relationship, meaning that 
# if one value goes up does not mean that the 
# other will.
#0.2 表示關係不好，這意味著如果一個值上升並不意味著
# 另一個值會上升。
#What is a good correlation? It depends on the 
# use, but I think it is safe to say you have to 
# have at least 0.6 (or -0.6) to call it a good 
# correlation.
#什麼是良好的相關性？這取決於使用， 但我認為可以肯定
# 地說， 你必須有至少 0.6 （或 - 0.6） 來稱之為良好
# 的相關性。

#Perfect Correlation: 完美關聯：
#We can see that "Duration" and "Duration" got 
# the number 1.000000, which makes sense, each 
# column always has a perfect relationship with 
# itself.
#我們可以看到，"持續時間"和"持續時間"得到了數字
#1.000000，這是有道理的，每個列總是與自己有一個完美的關係。

#Good Correlation: 良好的相關性：
#"Duration" and "Calories" got a 0.922721 
# correlation, which is a very good correlation, 
# and we can predict that the longer you work 
# out, the more calories you burn, and the other 
# way around: if you burned a lot of calories, 
# you probably had a long work out.
#"持續時間"和"卡路里"的相關性為0.922721，這是一個
# 很好的相關性，我們可以預測，你鍛煉的時間越長，你
# 燃燒的卡路里就越多，相反：如果你燃燒了大量的卡路里
# ，你可能有一個漫長的工作。

#Bad Correlation: 不良相關性
#"Duration" and "Maxpulse" got a 0.009403 
# correlation, which is a very bad correlation, 
# meaning that we can not predict the max pulse 
# by just looking at the duration of the work out, 
# and vice versa.
#"持續時間"和"最大脈衝"的相關性為0.009403，這是一個
# 非常糟糕的相關性，這意味著我們無法通過僅僅查看工作
# 持續時間來預測最大脈衝，反之亦然。