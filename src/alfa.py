days = ['Манная', 'Гречневая', 'Пшеная', 'Овсяная', 'Рисовая']
print("Введите количество дней")
N = int(input())
for i in range(N) :
      print(days[i%len(days)])