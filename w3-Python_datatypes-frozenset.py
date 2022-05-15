x = ({"apple", "banana", "cherry"}) #frozenset凍集合
print(x)
#(class) frozenset(iterable: Iterable[str] = ...)凍結集（可重置：可重置[str]
x = {"apple", "banana", "cherry"} #set集合
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)
#{'apple', 'cherry', 'banana'}
#{'apple', 'cherry', 'banana'}
#frozenset({'banana', 'cherry', 'apple'})
#每次輸出的順序都不一樣