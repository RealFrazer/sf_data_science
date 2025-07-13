"""Игра угадай числа"""

import numpy as np

number = np.random.randint(1, 101) # Загадываем случайное число

# Количество попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадайте число от 1 до 100: "))
    
    if predict_number > number:
        print(f"Число должно быть меньше: {predict_number}")
        
    elif predict_number < number:
        print(f"Число должно быть больше: {predict_number}")
        
    else:
        print(f"Вы угадали число: {predict_number} за {count} попыток!")
        break # Выход из цикла
        