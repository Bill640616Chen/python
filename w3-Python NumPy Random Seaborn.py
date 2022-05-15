#https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp
#Random Seaborn 隨機資料視覺化(以圖表顯示)
#Visualize Distributions With Seaborn
#用seaborn來顯示視覺化分佈
#Seaborn is a library that uses Matplotlib underneath to 
# plot graphs. It will be used to visualize random 
# distributions.
#Seaborn是一個庫使用Matplotlib(建立一個圖表的概念)下面繪製圖形。
# 它將用於可視化隨機分佈。
#Install Seaborn. 安裝Seaborn
#If you have Python and PIP already installed on a system, install it using this command:
#pip install seaborn
#If you use Jupyter, install Seaborn using this command:
#!pip install seaborn

#Distplots 地標
#Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.
#Distplot 代表分布圖，它用作輸入陣列並繪製與陣列中點分佈對應的曲線。
#Import Matplotlib 導入Matplotlib
#Import the pyplot object of the Matplotlib module in your code using the following statement:
#使用以下語句匯入代碼中 Matplotlib 模組的 pyplot 物件：
import matplotlib.pyplot as plt
#You can learn about the Matplotlib module in our Matplotlib Tutorial.
#您可以在我們的Matplotlib教程中了解Matplotlib模組。

#Import Seaborn
#Import the Seaborn module in your code using the following statement:
import seaborn as sns

print("-----------------------------------------繪製繪圖")
#Plotting a Displot
#繪製繪圖
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

print("---------------------------------繪製繪圖沒有直方圖")
#Plotting a Distplot Without the Histogram 繪製繪圖沒有直方圖
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
#hist是Histogram直方圖的縮寫
#Note: We will be using: sns.distplot(arr, hist=False) 
# to visualize random distributions in this tutorial.
#注意：我們將使用：sns.distplot（arr，hist=False）
# 來可視化本教程中的隨機分佈。
#https://ithelp.ithome.com.tw/articles/10186624
#使用 matplotlib 建立一個圖表的概念是組裝它提供的基礎元件，
# 像是圖表類型、圖例或者標籤等元件。
