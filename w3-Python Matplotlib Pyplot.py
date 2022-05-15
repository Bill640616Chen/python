#https://www.w3schools.com/python/matplotlib_pyplot.asp
#Python Matplotlib Pyplot 繪圖庫Pyplot
#Pyplot
#Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
#大多數 Matplotlib 公用設施位於 pyplot 子模組下，通常以 plt 別名導入：
import matplotlib.pyplot as plt
#Now the Pyplot package can be referred to as plt.
#現在，Pyplot 包可以稱為 plt。
#Draw a line in a diagram from position (0,0) to position (6,250):
#在圖表中繪製一條線，從位置 （0，0） 到位置 （6，250）：
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()
#當plot(預設x軸,預設y軸),則plot(ypoints,xpoints)位置發生變化
#You will learn more about drawing (plotting) in the next chapters.
#在接下來的幾章中，您將瞭解更多有關繪圖（繪圖）的詳細情況。
