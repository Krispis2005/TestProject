text = input()
dict = {i: text.count(i) for i in set(text)}
print (dict)