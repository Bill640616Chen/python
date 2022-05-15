#https://www.w3schools.com/python/module_random.asp
#Removing Items from a Dictionary 在字典中新增項目
#Python has a built-in module that you can use to make random numbers.
#Python 有一個可用於製作隨機數的內建模組。
#The random module has a set of methods:
#random 模組有一組如下的方法：
#Method方法	        Description描述
#seed()	            Initialize the random number generator
#seed（）           初始化隨機數產生器。
#getstate()	        Returns the current internal state of the random number generator
#getstate（）       傳回隨機數生成器的當前內部狀態。
#setstate()	        Restores the internal state of the random number generator
#setstate（）       恢復隨機數生成器的內部狀態。
#getrandbits()	    Returns a number representing the random bits
#getrandbits（）    傳回表示隨機位的數位。
#randrange()	    Returns a random number between the given range
#randrange（）      傳回給定範圍之間的隨機數。
#randint()	        Returns a random number between the given range
#randint（）        傳回給定範圍之間的隨機數。
#choice()	        Returns a random element from the given sequence
#choice（）         傳回給定序列中的隨機元素。
#choices()	        Returns a list with a random selection from the given sequence
#choices（）        傳回一個清單，其中包含給定序列中的隨機選擇。
#shuffle()	        Takes a sequence and returns the sequence in a random order
#shuffle（）        接受一個序列，並以隨機順序返回此序列。
#sample()	        Returns a given sample of a sequence
#sample（）         傳回序列的給定樣本。
#random()	        Returns a random float number between 0 and 1
#random（）         傳回 0 與 1 之間的浮點數。
#uniform()	        Returns a random float number between two given parameters
#uniform（）        傳回兩個給定參數之間的隨機浮點數。
#triangular()	    Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters
#triangular（）     傳回兩個給定參數之間的隨機浮點數，您還可以設置模式參數以指定其他兩個參數之間的中點。
#betavariate()	    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
#betavariate（）    基於 Beta 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。
#expovariate()	    Returns a random float number based on the Exponential distribution (used in statistics)
#expovariate（）    基於指數分佈（用於統計學），返回 0 到 1 之間的隨機浮點數，如果參數為負，則返回 0 到 -1 之間的隨機浮點數。
#gammavariate()  	Returns a random float number based on the Gamma distribution (used in statistics)
#gammavariate（）   基於 Gamma 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。
#gauss()	        Returns a random float number based on the Gaussian distribution (used in probability theories)
#gauss（）          基於高斯分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#lognormvariate()	Returns a random float number based on a log-normal distribution (used in probability theories)
#lognormvariate（） 基於對數正態分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#normalvariate()	Returns a random float number based on the normal distribution (used in probability theories)
#normalvariate（）  基於正態分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#vonmisesvariate()	Returns a random float number based on the von Mises distribution (used in directional statistics)
#vonmisesvariate（）基於 von Mises 分佈（用於定向統計學）返回 0 到 1 之間的隨機浮點數。
#paretovariate() 	Returns a random float number based on the Pareto distribution (used in probability theories)
#paretovariate（）  基於 Pareto 分佈（用於概率論）返回 0 到 1 之間的隨機浮點數。
#weibullvariate()	Returns a random float number based on the Weibull distribution (used in statistics)
#weibullvariate（） 基於 Weibull 分佈（用於統計學）返回 0 到 1 之間的隨機浮點數。