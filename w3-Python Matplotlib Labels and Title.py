#https://www.w3schools.com/python/matplotlib_labels.asp
#Python Matplotlib Labels and Title 繪圖庫標籤和標題
#Create Labels for a Plot
#With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.
#為繪圖創建標籤
print("---------------Add labels to the x- and y-axis")
#Add labels to the x- and y-axis:
#使用 Pyplot，您可以使用 xlabel （） 和 ylabel （） 功能為 x 軸和 y 軸設定標籤。
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

print("---------------------Create a Title for a Plot")
#Create a Title for a Plot 為繪圖創建標題
#With Pyplot, you can use the title() function to set a title for the plot.
#使用 Pyplot，您可以使用title()功能為繪圖設置標題。
#Add a plot title and labels for the x- and y-axis:
#為 x 軸和 y 軸添加繪圖示題和標籤：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()

print("-----Set Font Properties for Title and Labels")
#Set Font Properties for Title and Labels
#為標題和標籤設置字體屬性
#You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
#您可以使用 xlabel()、ylabel()和title()中的字體參數為標題和標籤設置字體屬性。
#Set font properties for the title and labels:
#標題與標籤設定字型屬性：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()
#font2 = {'family':'serif','color':'darkred','size':15}
#font2 = {字典格式,鍵:值,}{字型,顏色,大小}

print("-----------------Position the Title 標題位置")
#Position the Title 標題位置
#You can use the loc parameter in title() to position the title.
#您可以使用標題中的定位參數在title()裡來定位標題。
#Legal values are: 'left', 'right', and 'center'. Default value is 'center'.
#合法的值是：'left', 'right', and 'center'。默認值為'center'。
#Position the title to the left:
#將標題向左放置：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.show()