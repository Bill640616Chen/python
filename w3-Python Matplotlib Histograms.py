#https://www.w3schools.com/python/matplotlib_histograms.asp
#Python Matplotlib Histograms 繪圖庫直方圖
#Histogram 直方圖
#A histogram is a graph showing frequency distributions.
#直方圖是顯示頻率分佈的圖形。
#It is a graph showing the number of observations within each given interval.
#它是一張圖表，顯示每個給定間隔內的觀測次數。
#Example: Say you ask for the height of 250 people, you might end up with a histogram like this:
#範例：假設您要求 250 人的高度，您最終可能會獲得這樣的直方圖：
#You can read from the histogram that there are approximately:
#您可以從直方圖中讀到，大致如下：
#2 people from 140 to 145cm
#5 people from 145 to 150cm
#15 people from 151 to 156cm
#31 people from 157 to 162cm
#46 people from 163 to 168cm
#53 people from 168 to 173cm
#45 people from 173 to 178cm
#28 people from 179 to 184cm
#21 people from 185 to 190cm
#4 people from 190 to 195cm

print("-----------------------------------創建直方圖")
#Create Histogram 創建直方圖
#In Matplotlib, we use the hist() function to create histograms.
#在 Matplotlib 中，我們使用hist()功能創建直方圖。
#The hist() function will use an array of numbers to create a histogram, the array is sent into the function as an argument.
#hist()功能將使用一組數字創建直方圖，該陣列將作為參數發送到函數中。
#For simplicity we use NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10. Learn more about Normal Data Distribution in our Machine Learning Tutorial.
#對於簡單性，我們使用 NumPy 隨機生成具有 250 個值的陣列，其中值將集中在 170 左右，標準偏差為 10。在我們的機器學習教程中瞭解有關正常數據分佈的更多情況。
#A Normal Data Distribution by NumPy:
print("---------------------------NumPy 的正常數據分佈")
#NumPy 的正常數據分佈：
from matplotlib import colors
import numpy as np
x = np.random.normal(170, 10, 250)
print(x)
#nomal(集中值,標準差,值的總數)
#This will generate a random result, and could look like this:
#這將生成隨機結果，並且可能看起來像這樣：
#The hist() function will read the array and produce a histogram:
#hist()功能將讀取陣列並生成直方圖：
#A simple histogram:
print("-----------------------------------簡單的直方圖")
#簡單的直方圖：
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(170, 10, 250)
plt.hist(x,color="hotpink",histtype='step')
plt.show() 
#hist的函數:
#(x: ArrayLike | Sequence[ArrayLike], 
# bins: int | str | Sequence | None, 
# range: Tuple | None = ..., 
# density: bool | None = ..., 
# weights: ArrayLike | None = ..., 
# cumulative: bool = ..., 
# bottom: ArrayLike | Any | None = ..., 
# histtype: Literal['bar', 'barstacked', 'step', 'stepfilled'] = ..., 
# align: Literal['left', 'mid', 'right'] = ..., 
# orientation: Literal['vertical', 'horizontal'] = ..., 
# rwidth: Any | None = ..., log: bool = ..., 
# color: _ColorLike | Sequence[_ColorLike] | None = ..., 
# label: str | None = ..., 
# stacked: bool = ..., 
# normed: bool | None = ..., *, 
# data: Any | None = ..., 
# **kwargs: Any) -> Tuple[ArrayLike | List[ArrayLike], ArrayLike, List | List[List]]
