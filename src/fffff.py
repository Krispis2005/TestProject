N = int(input())
toys_count = {}
for i in range(N):
    name, toys = input().split(': ')
    toys = list(toys.split(','))
    for toy in toys:
        if toy in toys_count.keys():
            toys_count[toy] +=1
        else:
            toys_count[toy] = 1
for toy, count in toys_count.items():
    if count == 1:
        print(toy)