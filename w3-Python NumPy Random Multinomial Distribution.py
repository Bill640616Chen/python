#https://www.w3schools.com/python/numpy/numpy_random_logistic.asp
#Random Multinomial Distribution 多元式分佈
#把二元分佈公式推廣至多種狀態，就得到了多元分佈。
#Multinomial Distribution 多元式分佈
#Multinomial distribution is a generalization of binomial distribution.
#多元式分佈是二元分佈的泛化。
#It describes outcomes of multi-nomial scenarios unlike 
# binomial where scenarios must be only one of two. e.g. 
# Blood type of a population, dice roll outcome.
#它描述了多提名場景的結果，不像二元方案，其中場景必須只是兩個場景
# 之一。例如，血型的人口，骰子捲的結果。
#It has three parameters:
#它有三個參數：
#n - number of possible outcomes (e.g. 6 for dice roll).
#n - n - 可能的結果數（例如骰子卷的6）。
#pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#pvals - 結果概率清單（例如骰子卷的 [1/6、1/6、1/6、1/6、1/6、1/6] ） 。
#size - The shape of the returned array.
#size - 傳回陣列的形狀。
print("---------multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(10,6)")
#Draw out a sample for dice roll:
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(10,6))
print(x)
#size=(10,6),輸出一個三維陣列,十個二維陣列,每個二維有六個一維
print("----測試1---multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(10)")
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(10))
print(x)
#size=(10),輸出一個二維陣列,十個一維陣列
print("----測試2---multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(3,2,5)")
from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(3,2,5))
print(x)
#size=(3,2,5),輸出一個4維,3個3維,每個3維有2個2維,每個2維有5個1維
print("----測試3---multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(3,2,5)")
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(3,2,5))
print(x)
sns.distplot(x)
plt.show()
#Note: Multinomial samples will NOT produce a single value! They will produce one value for each pval.
#注意：多名額樣品不會產生單一值！它們將為每個 pval 產生一個值。
#Note: As they are generalization of binomial distribution their visual representation and similarity of normal distribution is same as that of multiple binomial distributions.
#注意：由於它們是二元分佈的泛化，其視覺表現和正常分佈的相似性與多個二元分佈相同。