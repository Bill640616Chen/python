#https://www.w3schools.com/python/python_ml_decision_tree.asp
#Python Machine Learning - Decision Tree 機器學習- 決策樹
#Decision Tree 決策樹
#In this chapter we will show you how to make a "Decision Tree". A Decision Tree is a Flow Chart, and can help you make decisions based on previous experience.
#在本章中，我們將向您展示如何製作"決策樹"。決策樹是流程圖，可以説明您根據以前的經驗做出決策。
#In the example, a person will try to decide if he/she should go to a comedy show or not.
#在示例中，一個人將嘗試決定他/她是否應該去看喜劇表演。
#Luckily our example person has registered every time there was a comedy show in town, and registered some information about the comedian, and also registered if he/she went or not.
#幸運的是，我們的例子人已經註冊了每次有一個喜劇節目在城裡，並註冊了一些有關喜劇演員的資訊，也登記，如果他/她去與否。
#Now, based on this data set, Python can create a decision tree that can be used to decide if any new shows are worth attending to.
#現在，基於此數據集，Python 可以創建一個決策樹，用於決定是否有任何新節目值得關注。
#How Does it Work? 它是如何工作的？
#First, import the modules you need, and read the dataset with pandas:
#首先，導入所需的模組，並閱讀熊貓的數據集：
#Read and print the data set:
print("-----------------------------------閱讀並列印資料集")
#閱讀並列印資料集：
import pandas
from pydotplus.graphviz import Graph
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
df = pandas.read_csv("shows.csv")
print(df)
#To make a decision tree, all data has to be numerical.
#要做出決策，所有數據必須是數位的。
#We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.
#我們必須將非數位列「國籍」和「去」轉換為數位值。
#Pandas has a map() method that takes a dictionary with information on how to convert the values.
#Pandas有一個map()方法，它需要一本字典，其中提供了如何轉換值的資訊。
#{'UK': 0, 'USA': 1, 'N': 2}
#Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.
#意思是將"UK"值轉換為 0，"美國"轉換為 1，將"N"轉換為 2。
#Change string values into numerical values:
print("------------------------map()----將字串值變更為數值")
#將字串值變更為數值：
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df)
#Then we have to separate the feature columns from the target column.
#然後，我們必須將功能欄與目標欄分開。
#The feature columns are the columns that we try to predict from, and the target column is the column with the values we try to predict.
#功能欄是我們嘗試預測的欄，目標欄是具有我們嘗試預測值的欄。
#X is the feature columns, y is the target column:
print("----------------------------X 是功能欄，y 是目標欄")
#X 是功能欄，y 是目標欄：
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
print(X)
print(y)
#Now we can create the actual decision tree, fit it with our details, and save a .png file on the computer:
#現在，我們可以創建實際決策樹，將其與我們的詳細資訊相符，並在計算機上保存一個.png檔：
#Create a Decision Tree, save it as an image, and show the image:
print("----------------創建決策樹，將其保存為圖像，並顯示圖像")
#創建決策樹，將其保存為圖像，並顯示圖像：
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg
df = pandas.read_csv("shows.csv")
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
graph = plt.figure( figsize=[10,10])
img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
#plt.figure( figsize=[8,8])
plt.show()

#Result Explained 結果解釋
#The decision tree uses your earlier decisions to calculate the odds for you to wanting to go see a comedian or not.
#決定樹使用你之前的決定來計算你是否想去看喜劇演員的可能性。
#Let us read the different aspects of the decision tree:
#讓我們閱讀決策樹的不同方面：

#Rank 排名
#Rank <= 6.5 means that every comedian with a rank of 6.5 or lower will follow the True arrow (to the left), and the rest will follow the False arrow (to the right).
#排名 <= 6.5 表示每個排名為 6.5 或更低的喜劇演員將遵循真箭頭（左側），其餘的將遵循假箭頭（右側）。
#gini = 0.497 refers to the quality of the split, and is always a number between 0.0 and 0.5, where 0.0 would mean all of the samples got the same result, and 0.5 would mean that the split is done exactly in the middle.
#gini = 0.497 是指拆分的質量，並且始終是 0.0 和 0.5 之間的數位，其中 0.0 表示所有樣本都得到了相同的結果，0.5 表示拆分完全在中間完成。
#samples = 13 means that there are 13 comedians left at this point in the decision, which is all of them since this is the first step.
#樣本 = 13 意味著在決定的這個階段還剩下 13 個喜劇演員， 這是所有喜劇演員， 因為這是第一步。
#value = [6, 7] means that of these 13 comedians, 6 will get a "NO", and 7 will get a "GO".
#值 = [6， 7] 意味著在這 13 個喜劇演員中， 6 個將獲得 "否"， 7 個將獲得 "GO" 。

#Gini
#There are many ways to split the samples, we use the GINI method in this tutorial.
#有許多方法來分割樣本，我們在此教程中使用 GINI 方法。
#The Gini method uses this formula:
#吉尼方法使用此公式：
#Gini = 1 - (x/n)2 - (y/n)2 #2是平方
#n是sample數,xy是value的值
#Where x is the number of positive answers("GO"), n is the number of samples, and y is the number of negative answers ("NO"), which gives us this calculation:
#x 是正答案數（"GO"），n 是樣本數，y 是否定答案數（"否"），這給了我們這樣的計算：
#1 - (7 / 13)2 - (6 / 13)2 = 0.497

#The next step contains two boxes, one box for the comedians with a 'Rank' of 6.5 or lower, and one box with the rest.
#下一步包含兩個盒子，一個盒子給"排名"在6.5或以下的喜劇演員，一個盒子，其餘的盒子。
#True - 5 Comedians End Here: 正確 - 5 喜劇演員結束在這裡：
#gini = 0.0 means all of the samples got the same result.
#gini = 0.0 表示所有樣品的結果相同。
#samples = 5 means that there are 5 comedians left in this branch (5 comedian with a Rank of 6.5 or lower).
#樣本 = 5 表示本分支中還剩下 5 個喜劇演員（5 個喜劇演員的排名為 6.5 或更低）。
#value = [5, 0] means that 5 will get a "NO" and 0 will get a "GO".
#值 = [5， 0] 表示 5 將獲得 "否"， 0 將獲得 "GO" 。
#False - 8 Comedians Continue: 錯誤 - 8 喜劇演員繼續：
#Nationality 國籍
#Nationality <= 0.5 means that the comedians with a nationality value of less than 0.5 will follow the arrow to the left (which means everyone from the UK, ), and the rest will follow the arrow to the right.
#國籍<=0.5表示國籍價值小於0.5的喜劇演員將跟隨箭頭向左（這意味著來自英國的每個人），其餘的將跟隨箭頭向右。
#gini = 0.219 means that about 22% of the samples would go in one direction.
#gini = 0.219 表示大約 22% 的樣本將朝一個方向移動。
#samples = 8 means that there are 8 comedians left in this branch (8 comedian with a Rank higher than 6.5).
#樣本 = 8 表示本分支中還剩下 8 個喜劇演員 （8 個排名高於 6.5 的喜劇演員） 。
#value = [1, 7] means that of these 8 comedians, 1 will get a "NO" and 7 will get a "GO".
#值 = [1， 7] 意味著這 8 個喜劇演員中， 1 個將獲得 "否"， 7 個將獲得 "GO" 。

#True - 4 Comedians Continue: 正確 - 4 喜劇演員繼續：
#Age年齡
#Age <= 35.5 means that comedians at the age of 35.5 or younger will follow the arrow to the left, and the rest will follow the arrow to the right.
#年齡<=35.5意味著35.5歲或以下的喜劇演員將沿著箭頭向左走，其餘的將沿著箭頭向右走。
#gini = 0.375 means that about 37,5% of the samples would go in one direction.
#gini = 0.375 表示大約 37，5% 的樣本將朝一個方向移動。
#samples = 4 means that there are 4 comedians left in this branch (4 comedians from the UK).
#樣本 = 4 表示這個分支還剩下 4 個喜劇演員 （4 個來自英國的喜劇演員） 。
#value = [1, 3] means that of these 4 comedians, 1 will get a "NO" and 3 will get a "GO".
#值 = [1， 3] 意味著這 4 個喜劇演員中， 1 個將獲得 "否"， 3 個將獲得 "GO" 。
#False - 4 Comedians End Here: 錯誤 - 4 喜劇演員結束在這裡：
#gini = 0.0 means all of the samples got the same result.
#gini = 0.0 表示所有樣品的結果相同。
#samples = 4 means that there are 4 comedians left in this branch (4 comedians not from the UK).
#樣本 = 4 意味著這個分支還剩下 4 個喜劇演員 （4 個喜劇演員不是來自英國） 。
#value = [0, 4] means that of these 4 comedians, 0 will get a "NO" and 4 will get a "GO".
#值 = [0， 4] 意味著這 4 個喜劇演員中， 0 將獲得 "否"， 4 將獲得 "GO" 。

#True - 2 Comedians End Here: 正確 - 2 喜劇演員結束在這裡：
#gini = 0.0 means all of the samples got the same result.
#gini = 0.0 表示所有樣品的結果相同。
#samples = 2 means that there are 2 comedians left in this branch (2 comedians at the age 35.5 or younger).
#樣本 = 2 表示本分支中還剩下 2 名喜劇演員（2 名 35.5 歲或以下的喜劇演員）。
#value = [0, 2] means that of these 2 comedians, 0 will get a "NO" and 2 will get a "GO".
#值 = [0， 2] 意味著在這 2 個喜劇演員中， 0 將獲得 "否"， 2 將獲得 "GO" 。
#False - 2 Comedians Continue: 錯誤 - 2 喜劇演員繼續：
#Experience 經驗
#Experience <= 9.5 means that comedians with 9.5 years of experience, or less, will follow the arrow to the left, and the rest will follow the arrow to the right.
#經驗<= 9.5 意味著擁有 9.5 年或更少經驗的喜劇演員將沿著箭頭向左走，其餘的將沿著箭頭向右走。
#gini = 0.5 means that 50% of the samples would go in one direction.
#gini = 0.5 表示 50% 的樣品將朝一個方向移動。
#samples = 2 means that there are 2 comedians left in this branch (2 comedians older than 35.5).
#樣本 = 2 表示本分支中還剩下 2 個喜劇演員 （2 個年齡超過 35.5 歲的喜劇演員） 。
#value = [1, 1] means that of these 2 comedians, 1 will get a "NO" and 1 will get a "GO".
#值 = [1， 1] 意味著在這 2 個喜劇演員中， 1 個將獲得 "否"， 1 個將獲得 "GO" 。

#True - 1 Comedian Ends Here: 正確 - 1 喜劇演員結束在這裡：
#gini = 0.0 means all of the samples got the same result.
#gini = 0.0 表示所有樣品的結果相同。
#samples = 1 means that there is 1 comedian left in this branch (1 comedian with 9.5 years of experience or less).
#樣本 = 1 表示本分支中還剩下 1 個喜劇演員（1 個具有 9.5 年或更少經驗的喜劇演員）。
#value = [0, 1] means that 0 will get a "NO" and 1 will get a "GO".
#值 = [0， 1] 表示 0 將獲得 "否"， 1 將獲得 "GO" 。
#False - 1 Comedian Ends Here: 錯誤 - 1 喜劇演員結束在這裡：
#gini = 0.0 means all of the samples got the same result.
#gini = 0.0 表示所有樣品的結果相同。
#samples = 1 means that there is 1 comedians left in this branch (1 comedian with more than 9.5 years of experience).
#樣本 = 1 表示本分支中還剩下 1 個喜劇演員（1 個具有超過 9.5 年經驗的喜劇演員）。
#value = [1, 0] means that 1 will get a "NO" and 0 will get a "GO".
#值 = [1， 0] 表示 1 將獲得"否"，0 將獲得"GO"。

#Predict Values 預測值
#We can use the Decision Tree to predict new values.
#我們可以使用決策樹來預測新的值。
#Example: Should I go see a show starring a 40 years old American comedian, with 10 years of experience, and a comedy ranking of 7?
#例子：我應該去看一個40歲的美國喜劇演員主演的節目嗎？
#Use predict() method to predict new values:
print("------------------------------使用predict()方法預測新值")
#使用predict()方法預測新值：
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
df = pandas.read_csv("shows.csv")
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
print(dtree.predict([[40, 10, 7, 1]]))
print("[1] means 'GO'")
print("[0] means 'NO'")

print("----------------------如果喜劇排名是 6， 答案會是什麼？")
#What would the answer be if the comedy rank was 6?
#如果喜劇排名是 6， 答案會是什麼？
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
df = pandas.read_csv("shows.csv")
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
print(dtree.predict([[40, 10, 6, 1]]))
print("[1] means 'GO'")
print("[0] means 'NO'")

#Different Results 不同結果
#You will see that the Decision Tree gives you different results if you run it enough times, even if you feed it with the same data.
#您將看到，決策樹會為您提供不同的結果，如果您運行了足夠的時間，即使您用相同的數據饋送它。
#That is because the Decision Tree does not give us a 100% certain answer. It is based on the probability of an outcome, and the answer will vary.
#這是因為決策樹沒有給我們一個100%肯定的答案。它基於結果的概率，答案會有所不同。
