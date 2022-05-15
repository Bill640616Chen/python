#https://www.w3schools.com/python/matplotlib_grid.asp
#Python Matplotlib Adding Grid Lines 繪圖庫添加格線
#Add Grid Lines to a Plot 將格線添加到繪圖中
#With Pyplot, you can use the grid() function to add grid lines to the plot.
#使用 Pyplot，您可以使用網格（）功能向繪圖添加網格線。
#Add grid lines to the plot:
print("-----------------------------在繪圖中新增格線")
#在繪圖中新增格線：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()

print("---------------------------指定要顯示的網格線")
#Specify Which Grid Lines to Display
#指定要顯示的網格線
#You can use the axis parameter in the grid() function to specify which grid lines to display.
#您可以使用 grid()功能中的軸參數來指定要顯示的網格線。
#Legal values are: 'x', 'y', and 'both'. Default value is 'both'.
#合法值是：「x」。、"y"和「兩者」。預設值為"兩者"。
#Display only grid lines for the x-axis:
#只顯示 x 軸的格線：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y,label='test')
plt.legend()
plt.grid(axis = 'x')
plt.show()
#axis = 'x'只顥示x軸的格線
#Display only grid lines for the y-axis:
#只顯示 y 軸的格線：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

print("---------------------------為網格設置線路屬性")
#Set Line Properties for the Grid 為網格設置線路屬性
#You can also set the line properties of the grid, 
# like this: grid(color = 'color', linestyle 
# = 'linestyle', linewidth = number).
#您還可以設定格線屬性，如：網格（顏色 = "顏色"， 線型 
# = "線型"， 線寬 = 數字） 。
#Set the line properties of the grid:
#設定格線屬性：
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(color = '#008B8B', linestyle = '--', linewidth = 0.5)
plt.show()
#color = 六價色值或顏色名稱
plt.grid(c ='Blue',ls ='--', lw = 2)
plt.show()
#valid keywords are
#['size', 'width', 'color', 'tickdir', 'pad', 
# 'labelsize', 'labelcolor', 'zorder', 'gridOn', 
# 'tick1On', 'tick2On', 'label1On', 'label2On', 
# 'length', 'direction', 'left', 'bottom', 'right', 
# 'top', 'labelleft', 'labelbottom', 'labelright', 
# 'labeltop', 'labelrotation', 'grid_agg_filter', 
# 'grid_alpha', 'grid_animated', 'grid_antialiased', 
# 'grid_clip_box', 'grid_clip_on', 'grid_clip_path', 
# 'grid_color', 'grid_contains', 'grid_dash_capstyle', 
# 'grid_dash_joinstyle', 'grid_dashes', 'grid_data', 
# 'grid_drawstyle', 'grid_figure', 'grid_fillstyle', 
# 'grid_gid', 'grid_in_layout','grid_label', 
# 'grid_linestyle', 'grid_linewidth', 'grid_marker', 
# 'grid_markeredgecolor', 'grid_markeredgewidth', 
# 'grid_markerfacecolor', 'grid_markerfacecoloralt', 
# 'grid_markersize', 'grid_markevery', 
# 'grid_path_effects', 'grid_picker', 
# 'grid_pickradius', 'grid_rasterized', 
# 'grid_sketch_params', 'grid_snap', 
# 'grid_solid_capstyle', 'grid_solid_joinstyle', 
# 'grid_transform', 'grid_url', 'grid_visible', 
# 'grid_xdata', 'grid_ydata', 'grid_zorder', 
# 'grid_aa', 'grid_c', 'grid_ds', 'grid_ls', 
# 'grid_lw', 'grid_mec', 'grid_mew', 'grid_mfc', 
# 'grid_mfcalt', 'grid_ms']