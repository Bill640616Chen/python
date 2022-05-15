#https://www.w3schools.com/python/ref_stat_harmonic_mean.asp
#statistics.harmonic_mean()：Calculates the harmonic mean (central location) of the given data
#計算給定資料的諧波均值（中心位置）
#Calculate the harmonic mean of the given data:
#計算給定數據的諧波均值：
# Import statistics Library
import statistics
# Calculate harmonic mean
print(statistics.harmonic_mean([40, 60, 80]))
print(statistics.harmonic_mean([10, 30, 50, 70, 90]))
#Definition and Usage 定義和用法
#The statistics.harmonic_mean() method calculates the harmonic mean (central location) of the given data set.
#該方法計算給定數據集的諧波平均值（中心位置）。statistics.harmonic_mean()
#Harmonic mean = The reciprocal of the arithmetic mean() of the reciprocals of the data.
#諧波均值 = 數據倒數的算術均值（）的倒數。
#The harmonic mean is calculated as follows:
#諧波均值的計算方法如下：
#If you have four values (a, b, c and d) - it will be equivalent to 4 / (1/a + 1/b + 1/c + 1/d).
#如果您有四個值（a，b，c和d） - 它將等效於4 / （1 / a + 1 / b + 1 / c + 1 / d）。
#Syntax 語法
#statistics.harmonic_mean(data)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator). Note: Cannot contain negative values!
#必填。要使用的數據值（可以是任何序列、清單或反覆運算器）。注意：不能包含負值！
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details　技術細節
#Return Value:	A float value, representing the harmonic mean of the given data
#返回值：	一個值，表示給定數據的諧波平均值float
#Python Version:	3.6

