print ("Введите количество игроков")
N = int(input())
print ("Хорошо, вас", N,", а теперь назовитесь")
min_name = "я"
for i in range(N):
    name = input()
    if min_name == "я":
        min_name = name
    elif name < min_name:
          min_name = name
          print (min_name)

