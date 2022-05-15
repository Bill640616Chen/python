#https://www.w3schools.com/python/pandas/pandas_plotting.asp
#Pandas Plotting 繪圖
#Pandas uses the plot() method to create diagrams.
#pandas使用plot()方法創建圖表。
#We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.
#我們可以使用 Pyplot，一個 Matplotlib 庫的子模組來可視化螢幕上的圖表。
#Read more about Matplotlib in our Matplotlib Tutorial.
#在我們的馬特普洛特利布教程中閱讀更多關於Matplotlib的內容。
#Import pyplot from Matplotlib and visualize our DataFrame:
#Matplotlib (Matrix plot library，矩陣繪圖庫)
print("---從Matplotlib導入 pyplotlib 並可視化我們的數據框架")
#從Matplotlib導入 pyplotlib 並可視化我們的數據框架：
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data2.csv')
df.plot()
plt.show()
#The examples in this page uses a CSV file called: 'data.csv'.
#此頁面中示例使用稱為「數據2.csv」的 CSV 檔。

#Scatter Plot散佈圖
#Specify that you want a scatter plot with the kind argument:
#指定您要一個帶有親切參數的散射繪圖：
#kind = 'scatter' 種類 = "散射"
#A scatter plot needs an x- and a y-axis.
#散射圖需要 x 軸和 y 軸。
#In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
#在下面的示例中，我們將使用 x 軸的"持續時間"和 y 軸的"卡路里"。
#Include the x and y arguments like this:
#包括這樣的 x 和 y 參數：
#x = 'Duration', y = 'Calories'
print("------------------------良好的相關性----散佈圖")
#x = "持續時間"， y = "卡路里"
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data2.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
#Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we conluded with the fact that higher duration means more calories burned.
#記住：在上一個示例中，我們瞭解到"持續時間"和"卡路里"之間的相關性為 0.922721，我們同意這樣一個事實，即持續時間越長意味著消耗的卡路里越多。
#By looking at the scatterplot, I will agree.
#通過觀察散射圖，我同意。不良相關性
#Let's create another scatterplot, where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403:
#讓我們創建另一個散射圖，其中列之間有一個壞關係，如「持續時間」和「最大脈衝」，相關性 0.009403：
#A scatterplot where there are no relationship between the columns:
print("-------------------------不良相關性----散佈圖")
#列之間沒有關係的散射圖：
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data2.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

print("--------------------------------------直方圖")
#Histogram 直方圖
#Use the kind argument to specify that you want a histogram:
#使用親切的參數來指定您想要直方圖：
#kind = 'hist'
#種類 = 直方
#A histogram needs only one column.
#直方圖只需要一個欄。
#A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
#直方圖向我們顯示每個間隔的頻率，例如，多少鍛煉持續 50 到 60 分鐘？
#In the example below we will use the "Duration" column to create the histogram:
#在下面的示例中，我們將使用「持續時間」列創建直方圖：
df["Duration"].plot(kind = 'hist')
plt.show()
#Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.
#筆記：直方圖告訴我們，有超過100次鍛煉，持續50至60分鐘。


