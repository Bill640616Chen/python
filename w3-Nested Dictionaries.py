#https://www.w3schools.com/python/python_dictionaries_nested.asp
#Python Nested Dictionaries 嵌套字典(字典裡字典)
#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
#字典裡可以包含很多字典,稱為嵌套字典(字典裡的字典)
#一個字典裡有三個字典
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#Or, if you want to add three dictionaries into a new dictionary:
#或者,如果想再加3個字典到一到新的字典裡：
#三個字典如何加到一個新的字典裡
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "Emil":{"read": "book","ball":"baseball"}, 
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#裡面可以很多字典放裡頭