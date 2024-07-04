print("Введите количество игроков")
N = int(input())
print("Хорошо, вас", N,", а теперь назовитесь")
min = "яяяяяяя"
for i in range(N):
    name = input()
    if name < min:
        min = name

print(min)

