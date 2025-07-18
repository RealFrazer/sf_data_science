"""Игра угадай числа. Играет сам компьютер"""

import numpy as np

def random_predict(number:int=1) -> int:
    """ Случайно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла, если угадали
        
    return count

def score_game(random_predict) -> int:
    """За какое количество в среднем угадывает наш подход за 1000 подходов

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # Загадаем список 1000 чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)