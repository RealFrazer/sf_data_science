"""Игра угадай числа. Играет сам компьютер"""

import numpy as np

def predict(number:int=1) -> int:
    """ Угадывает число от 1 до 100 за минимальное количество попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        count (int): Число попыток
    """
    
    count = 0 # Счетчик попыток
    upper_bound = 101 # Верхняя граница
    lower_bound = 1 # Нижняя граница
    
    while True:
        count+=1
        predict_number = np.random.randint(lower_bound, upper_bound) # Предполагаемое число
        if predict_number < number: # Если предполагаемое число меньше загаданного
            lower_bound = predict_number + 1 # Увеличиваем нижнюю границу
        elif predict_number > number: # Если предполагаемое число больше загаданного
            upper_bound = predict_number # Уменьшаем верхнюю границу
        else: # Если угадали
            break # Выход из цикла
        
    return count

def score_game(predict) -> int:
    """За какое количество в среднем угадывает наш алгоритм за 1000 подходов

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        score (int): Среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # Загадаем список 1000 чисел

    for number in random_array: # Перебираем каждое число из списка
        count_ls.append(predict(number)) # Вызываем функцию угадывания для каждого числа из списка
        
    score = int(np.mean(count_ls)) # Считаем среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(predict)