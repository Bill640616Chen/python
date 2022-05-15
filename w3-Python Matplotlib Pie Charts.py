#https://www.w3schools.com/python/matplotlib_pie_charts.asp
#Python Matplotlib Pie Charts 繪圖庫直方圖
#Creating Pie Charts 創建餅圖
#With Pyplot, you can use the pie() function to draw pie charts:
#使用 Pyplot，您可以使用pie()功能繪製餅圖：
#A simple pie chart:
print("---------------------------------一個簡單的餅圖")
#一個簡單的餅圖：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([31, 25, 25, 12, 1.5, 10.2])
plt.pie(y)
plt.show()
#餅圖都由陣列最後一個值開始,再逆時針顯示
#As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).
#正如您所看到的，餅圖為陣列中的每個值繪製一個條（稱為楔形）（在此例中[31, 25, 25, 12, 1.5, 10.2]）。
#By default the plotting of the first wedge starts from the x-axis and move counterclockwise:
#默認情況下，第一個楔形的繪圖從 x 軸開始，逆時針移動：
#Note: The size of each wedge is determined by comparing the value with all the other values, by using this formula:
#注意：每個楔子的大小通過使用此公式將值與所有其他值進行比較來確定：
#The value divided by the sum of all values: x/sum(x)
#值除以所有值的總和：x/sum（x）

print("-------------------------------------Labels 標籤")
#Labels 標籤
#Add labels to the pie chart with the label parameter.
#在餅圖上添加標籤，並添加標籤參數。
#The label parameter must be an array with one label for each wedge:
#標籤參數必須是每個楔形必須具有一個標籤的陣列：
#A simple pie chart:
#一個簡單的餅圖：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([31, 25, 25, 12, 1.5, 10.2])
mylabels = ["Apples", "Bananas", "Cherries", "Dates",'gram','kg']
plt.pie(y, labels = mylabels)
plt.show() 
#餅圖都由陣列最後一個值開始,再逆時針顯示

print("-----------------------------Start Angle 開始角度")
#Start Angle 開始角度
#As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
#如前所述，預設起始角度位於 x 軸，但您可以通過指定起始參數來更改起始角度。
#The startangle parameter is defined with an angle in degrees, default angle is 0:
#起始參數以度度角度定義，預設角度為 0：
#Start the first wedge at 90 degrees:
#在 90 度下啟動第一個楔子：
# (預設為0度,在圓的右邊,然後角度再逆時針走)
import matplotlib.pyplot as plt
import numpy as np
y = np.array([31, 25, 25, 12, 1.5, 10.2])
mylabels = ["Apples", "Bananas", "Cherries", "Dates",'gram','kg']
plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 
#餅圖都由陣列最後一個值開始,再逆時針顯示

print("--------------------------------------Explode 爆炸")
#Explode 爆炸
#Maybe you want one of the wedges to stand out? The explode parameter allows you to do that.
#也許你想讓其中一個楔子脫穎而出？爆炸參數允許你這樣做。
#The explode parameter, if specified, and not None, must be an array with one value for each wedge.
#爆炸參數（如果指定，而不是"無"）必須是每個楔形具有一個值的陣列。
#Each value represents how far from the center each wedge is displayed:
#每個值表示每個楔子顯示的中心距離：
#Pull the "Apples" wedge 0.2 from the center of the pie:
#從餡餅中心拉出「蘋果」楔子 0.2：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0.05, 0.001]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 
#餅圖都由陣列最後一個值開始,再逆時針顯示

print("--------------------------------------Shadow 影子")
#Shadow 影子
#Add a shadow to the pie chart by setting the shadows parameter to True:
#將陰影參數設置為 True，從而在餅圖中添加陰影：
#Add a shadow:
#新增陰影：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, 
labels = mylabels, 
explode = myexplode, 
shadow = True)
plt.show() 

print("--------------------------------------Colors 顏色")
#Colors 顏色
#You can set the color of each wedge with the colors parameter.
#您可以用顏色參數設定每個楔子的顏色。
#The colors parameter, if specified, must be an array with one value for each wedge:
#顏色參數（如果指定）必須是每個楔形具有一個值的陣列：
#Specify a new color for each wedge:
#為每個楔子指定新顏色：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["#a365b8", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 
#顏色名稱及六價色值
#https://www.w3schools.com/colors/colors_names.asp
#https://www.w3schools.com/colors/colors_hexadecimal.asp
#You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:
#您可以使用六價色值、140 個支援顏色名稱中的任何一個或以下快捷方式之一：
'''
'r' - Red
'g' - Green
'b' - Blue
'c' - Cyan
'm' - Magenta
'y' - Yellow
'k' - Black
'w' - White
'''

print("---------------------------------Legend 標籤圖例")
#Legend 標籤圖例
#To add a list of explanation for each wedge, use the legend() function:
#要添加每個楔子的解釋清單，請使用legend()功能：
#Add a legend:
#新增圖例：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

print("-------------------------title =--圖例的標題")
#Legend With Header 圖例的標題
#To add a header to the legend, add the title parameter to the legend function.
#要在圖例中添加標題，在圖例函數中添加標題參數。
#Add a legend with a header:
#添加帶有標題的圖例：
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.rcParams["figure.figsize"] = (8, 8 )
plt.rcParams['image.interpolation'] = 'nearest'
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:",loc = 0)
plt.show()
#plt.rcParams["figure.figsize"] = (8, 8 )
#把預設的圖形大小,變大成8*8
#rcParams [‘figure. figsize’]#图片像素
#legend()title標題,loc圖例的位置=str or int,
#borderpad邊框板,從loc位置開始 = int
'''
        ===============   =============
        Location String   Location Code
        ===============   =============
        'best'            0
        'upper right'     1
        'upper left'      2
        'lower left'      3
        'lower right'     4
        'right'           5
        'center left'     6
        'center right'    7
        'lower center'    8
        'upper center'    9
        'center'          10
        ===============   =============
'''

print("---------------測試-----title =--圖例的標題")
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.figure( figsize=[8,8], dpi=100) #dpi可有可無
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()