#https://www.w3schools.com/python/ref_stat_pvariance.asp
#statistics.pvariance()：Calculates the variance of an entire population
#計算整個總體的方差
#Calculate the variance of an entire population:
#計算整個總體的方差：
# Import statistics Library
import statistics
# Calculate the variance of an entire population
print(statistics.pvariance([1, 3, 5, 7, 9, 11]))
print(statistics.pvariance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print(statistics.pvariance([-11, 5.5, -3.4, 7.1]))
print(statistics.pvariance([1, 30, 50, 100]))
#Definition and Usage 定義和用法
#The statistics.pvariance() method calculates the variance of an entire population.
#該方法計算整個總體的方差。statistics.pvariance()
#A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean.
#較大的方差表示數據分散 ， 較小的方差表示數據緊密圍繞均值聚類。
#Tip: To calculate the variance from a sample of data, look at the statistics.variance() method.
#提示：若要計算數據樣本的方差，請查看該方法。statistics.variance()
#Syntax 語法
#statistics.pvariance(data, xbar)
#Parameter Values 參數值
#Parameter：Description
#data：Required. The data values to be used (can be any sequence, list or iterator)
#必填。要使用的資料值（可以是任何序列、清單或反覆運算器）
#xbar：Optional. The mean of the given data (can also be a second moment around a point that is not the mean). If omitted (or set to None), the mean is automatically calculated
#自選。給定數據的平均值（也可以是圍繞非平均值的點的第二個時刻）。如果省略（或設置為"無"），則會自動計算平均值
#Note: If data is empty, it returns a StatisticsError.
#注意：如果數據為空，則返回統計信息錯誤。
#Technical Details 技術細節
#Return Value:	A float value, representing the population variance of the given data
#返回值：	一個值，表示給定數據的總體方差float
#Python Version:	3.4
