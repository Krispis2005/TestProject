toys = []
unique = {}

for _ in range(int(input())):
    name, str = input().split(': ')
    toys.extend(set(str.split(', ')))  # убрать set для поиска действительно уникальных игрушек  # nopep8 # noqa

for toy in sorted(toys):
    unique[toy] = unique.get(toy, 0) + 1

for toy in unique:
    if unique[toy] == 1:
        print(toy)
