#%與{}的用法
product = 'apple'
price = 55
sentence = 'the %s is %s dollars.' % (product, price)
print(sentence)
#the apple is 55 dollars.
r = 'the {0} is {1} dollars.'.format('apple',55)
print(r)
n = f'the {product} is {price} dollars.'
print(n)