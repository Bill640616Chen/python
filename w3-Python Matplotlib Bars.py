#https://www.w3schools.com/python/matplotlib_bars.asp
#Python Matplotlib Bars 繪圖庫柱狀圖(直方圖)
#Creating Bars 創建條形
#With Pyplot, you can use the bar() function to draw bar graphs:
#使用 Pyplot，您可以使用條形圖（）功能繪製條形圖：
print("---------------------------bar(x,y)-繪製 4 條：")
#Draw 4 bars:繪製 4 條：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()
#The bar() function takes arguments that describes the layout of the bars.
#bar()功能採用描述條形布局的參數。
#The categories and their values represented by the first and second argument as arrays.
print("-----------第一個和第二個參數作為陣列表示的類別及其值")
#第一個和第二個參數作為陣列表示的類別及其值。
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y)
plt.show()

print("----------------------------Horizontal Bars 水平條")
#Horizontal Bars 水平條
#If you want the bars to be displayed horizontally instead of vertically, use the barh() function:
#如果您希望將條形水平顯示而不是垂直顯示，請使用 barh（） 功能：
#Draw 4 horizontal bars:
#繪製 4 個水平條：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y)
plt.show()

print("----------------------------------------條狀顏色")
#Bar Color 條狀顏色
#The bar() and barh() takes the keyword argument color to set the color of the bars:
#bar()和 barh() 採用關鍵字參數顏色來設定條形圖的顏色：
#Draw 4 red bars:
#繪製 4 個紅條：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "red")
plt.show()

print("----------------------------------------顏色名稱")
#Color Names 顏色名稱
#You can use any of the 140 supported color names.
#您可以使用 140 個支援中的顏色名稱中的任何一個。
#https://www.w3schools.com/colors/colors_names.asp
#Draw 4 "hot pink" bars:
#繪製4個「熱粉紅色」條形：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "hotpink")
plt.show()

print("----------------------------------------顏色六價")
#Color Hex 顏色六價
#Or you can use Hexadecimal color values:
#或者您可以使用六價顏色值：
#https://www.w3schools.com/colors/colors_hexadecimal.asp
#Draw 4 bars with a beautiful green color:
#繪製 4 條帶有美麗綠色的條形：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color = "#4CAF50")
plt.show()
#color不能shorter為c

print("----------------------------------------條形寬度")
#Bar Width 條形寬度
#The bar() takes the keyword argument width to set the width of the bars:
#bar() 採用關鍵字參數寬度來設置條形圖的寬度：
#Draw 4 very thin bars:
#繪製 4 個非常薄的條形：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, width = 0.1)
plt.show()
#width不能shorter為w
#The default width value is 0.8
#默認寬度值為 0.8
#Note: For horizontal bars, use height instead of width.
#注意：對於水平條，使用高度而不是寬度。

print("----------------------------------------條形高度")
#Bar Height 條形高度
#The barh() takes the keyword argument height to set the height of the bars:
#barh()水平條採取關鍵字參數高度來設置條形圖的寬度：
#Draw 4 very thin bars:
#繪製 4 個非常薄的條形：
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x, y,color='#5376cd',height = 0.1)
plt.show()
#The default height value is 0.8
#預設高度值為 0.8


