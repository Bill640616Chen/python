#https://www.w3schools.com/python/scipy/scipy_statistical_significance_tests.php
#SciPy Statistical Significance Tests 
#SciPy統計意義測試
#What is Statistical Significance Test?
#什麼是統計意義測試？
#In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.
#在統計學中，統計學意義意味著產生的結果背後有其原因，它不是隨機產生的，也不是偶然產生的。
#SciPy provides us with a module called scipy.stats, which has functions for performing statistical significance tests.
#SciPy 為我們提供了一個名為 scipy.stats 的模組，它具有執行統計意義測試的功能。
#Here are some techniques and keywords that are important when performing such tests:
#以下是一些在執行此類測試時非常重要的技術和關鍵字：
#Hypothesis in Statistics 統計學中的假設
#Hypothesis is an assumption about a parameter in population.
#假說是對人口參數的假設。
#Null Hypothesis 空假設
#It assumes that the observation is not stastically significant.
#它假定觀察並不具有停滯意義。
#Alternate Hypothesis 替代假設
#It assumes that the observations are due to some reason.
#它假定觀測是由於某種原因造成的。
#Its alternate to Null Hypothesis.
#它替代了空假設。
'Example:'
#For an assessment of a student we would take:
#對於學生的評估，我們將採取：
#"student is worse than average" - as a null hypothesis, and:
#"學生比一般人差" - 作為一個空假設， 和：
#"student is better than average" - as an alternate hypothesis.
#"學生比一般人好" - 作為另一種假設。
#One tailed test 一個尾部測試
#When our hypothesis is testing for one side of the value only, it is called "one tailed test".
#當我們的假設只測試價值的一側時，它被稱為「尾部測試」。
#For the null hypothesis:
'Example:'
#對於空假設：
#"the mean is equal to k", we can have alternate hypothesis:
#"平均等於 k"，我們可以有替代假設：
#"the mean is less than k", or:
#"平均值小於 k"，或：
#"the mean is greater than k"
#"平均值大於 k"
#Two tailed test 兩個尾部測試
#When our hypothesis is testing for both side of the values.
#當我們的假設是測試值的兩面。
'Example:'
#For the null hypothesis:
#對於空假設：
#"the mean is equal to k", we can have alternate hypothesis:
#"平均等於 k"，我們可以有替代假設：
#"the mean is not equal to k"
#"平均值不等於 k"
#In this case the mean is less than, or greater than k, and both sides are to be checked.
#在這種情況下，平均值小於或大於 k，並且要檢查雙方。
#Alpha value 阿爾法值
#Alpha value is the level of significance.
#阿爾法值是意義的級別。
'Example:'
#How close to extremes the data must be for null hypothesis to be rejected.
#數據必須離極端有多近才能拒絕空假設。
#It is usually taken as 0.01, 0.05, or 0.1.
#它通常被用作 0.01、0.05 或 0.1。
#P value P 值
#P value tells how close to extreme the data actually is.
#P 值告訴數據實際上離極端有多近。
#P value and alpha values are compared to establish the statistical significance.#
#比較P值和阿爾法值，以確定統計意義。
#If p value <= alpha we reject the null hypothesis and say that the data is statistically significant. otherwise we accept the null hypothesis.
#如果 p 值<+ alpha，我們拒絕空假設，並說數據具有統計學意義。否則我們接受空假設。

#T-Test T 測試
#比較兩個平均值（均值），然後告訴你它們彼此是否有差異
#T-tests are used to determine if there is significant difference  between means of two variables. and lets us know if they belong to the same distribution.
#T 測試用於確定兩個變數的平均之間是否存在顯著的差異。並讓我們知道他們是否屬於相同的分佈。
#It is a two tailed test.
#這是一個兩尾測試。
#The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.
#該函數ttest_ind（）採集兩個大小相同的示例，並生成一個tuple t-統計和 p-值。
#Find if the given values v1 and v2 are from same distribution:
print("-------該函數ttest_ind（）採集兩個大小相同的示例，並生成一個tuple t-統計和 p-值")
#尋找給定值 v1 和 v2 是否來自相同的分佈：
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2)
print(res)
print("-------如果您只想要返回 p 值，請使用 p 值屬性")
#If you want to return only the p-value, use the pvalue property:
#如果您只想要返回 p 值，請使用 p 值屬性：
import numpy as np
from scipy.stats import ttest_ind
v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
res = ttest_ind(v1, v2).pvalue
print(res)

print("----------------------檢驗數據是否符合某種分佈")
#KS-Test KS 測試
#Kolmogorov-Smirnov test 檢驗數據是否符合某種分佈
#KS test is used to check if given values follow a distribution.
#KS 測試用於檢查給定值是否隨分佈而後。
#The function takes the value to be tested, and the CDF as two parameters.
#該函數將要測試的值和CDF作為兩個參數。
#A CDF can be either a string or a callable function that returns the probability.
#CDF 可以是返回概率的字串或可調用功能。
#It can be used as a one tailed or two tailed test.
#它可以用作一尾或兩尾測試。
#By default it is two tailed. We can pass parameter alternative as a string of one of two-sided, less, or greater.
#默認情況下，它是兩尾。我們可以通過參數替代作為雙面，更少，或更大的字串之一。
#Find if the given value follows the normal distribution:
#尋找給定值是否遵循正常分佈：
import numpy as np
from scipy.stats import kstest
v = np.random.normal(size=100)
res = kstest(v, 'norm')
print(res)

#Statistical Description of Data 數據統計描述
#In order to see a summary of values in an array, we can use the describe() function.
#為了查看陣列中值的摘要，我們可以使用describe()功能。
#It returns the following description:
#它傳回以下描述：
#number of observations (nobs) 觀測次數（無名）
#minimum and maximum values = minmax
#最小值和最大值=數據歸一
#mean 平均值
#variance 方差
#應用數學裡的專有名詞。在機率論和統計學中，一個隨機變數
# 的變異數描述的是它的離散程度，也就是該變數離其期望值
# 的距離。一個實隨機變數的變異數也稱為它的二階動差或二
# 階主動差，恰巧也是它的二階累積量。意即，將各個誤差之
# 平方（而非取絕對值，使之肯定為正數），相加之後再除以
# 總數，透過這樣的方式來算出各個數據分布、零散（相對中
# 心點）的程度。繼續延伸的話，變異數的正平方根稱為該隨
# 機變數的標準差（此為相對各個數據點間），變異數除以期
# 望值歸一化的值叫分散指數，標準差除以期望值歸一化的值
# 叫變異係數。
#skewness 偏度
#在機率論和統計學中衡量實數隨機變數概率分布的不對稱性。
# 偏度的值可以為正，可以為負或者甚至是無法定義。在數量上，
# 偏度為負（負偏態；左偏）就意味著在概率密度函數左側的
# 尾部比右側的長，絕大多數的值（不一定包括中位數在內）
# 位於平均值的右側。偏度為正（正偏態；右偏）就意味著在
# 概率密度函數右側的尾部比左側的長，絕大多數的值（不一定
# 包括中位數）位於平均值的左側。偏度為零就表示數值相對
# 均勻地分布在平均值的兩側，但不一定意味著其為對稱分布。
#kurtosis 峰度
#在統計學中衡量實數隨機變數機率分布的峰態。峰度高就意味著
# 變異數增大是由低頻度的大於或小於平均值的極端差值引起的
print("------變異數增大是由低頻度的大於或小於平均值的極端差值引起的")
# 變異數增大是由低頻度的大於或小於平均值的極端差值引起的。
#Show statistical description of the values in an array:
import numpy as np
from scipy.stats import describe
v = np.random.normal(size=100)
res = describe(v)
print(res)

print("--------------------在陣列中查找值的偏度和峰度")
#Normality Tests (Skewness and Kurtosis)
#正常性測試（偏度和峰度）
#Normality tests are based on the skewness and kurtosis.
#正常性測試基於偏度和峰度。
#The normaltest() function returns p value for the null hypothesis:
#normaltest()函數傳回空假設的 p 值：
"x comes from a normal distribution"
#"x 來自正常分佈"。
#Skewness: 偏度 (確保資料中的總和)
#A measure of symmetry in data.
#衡量數據對稱性的指標。
#For normal distributions it is 0.
#對於正常分佈，它是 0。
#If it is negative, it means the data is skewed left.
#如果是負數，則表示數據偏左。
#If it is positive it means the data is skewed right.
#如果它是正的，則意味著數據偏右。
#Kurtosis: 峰度
#A measure of whether the data is heavy or lightly tailed to a normal distribution.
#衡量數據是重還是輕尾，以達到正常分佈。
#Positive kurtosis means heavy tailed.
#正值峰度代表高狹峰（leptokurtic）
#Negative kurtosis means lightly tailed.
#負值峰度代表低闊峰（platykurtic）
#Find skewness and kurtosis of values in an array:
#在陣列中查找值的偏度和峰度：
import numpy as np
from scipy.stats import skew, kurtosis
v = np.random.normal(size=100)
print(skew(v))
print(kurtosis(v))
#Find if the data comes from a normal distribution:
print("--------------------------------正常性測試")
#尋找資料是否來自正常分佈：
import numpy as np
from scipy.stats import normaltest
v = np.random.normal(size=100)
print(normaltest(v))