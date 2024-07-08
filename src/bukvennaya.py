text = input()
dict = {i: text.count(i) for i in text.split()}
print (dict)