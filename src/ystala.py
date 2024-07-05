N = int(input())
dict = []
rar = {}
for i in range(N):
    name, toy = input().split(', ')  # надо норм написать имя и игрушки
    dict.extend(( set(toy.split(': '))))
for vse in sorted(dict):
    if rar[vse] == 1:
        print(vse)
