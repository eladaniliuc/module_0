import numpy as np

number = np.random.randint(1,101)      # загадали число
print ("Загадано число от 1 до 100")
                
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = 50 #первое загаданое число всегда равно 50
    while number != predict:
        count+=1
        if number > predict:
            for i in range(6): 
                if predict+i*10 > number: #подсчитываем сумму десяток, чтобы превысить number
                    break
            predict += (i)*10   
            if number < predict: 
                predict -= 5
        elif number < predict:
            for i in range(6): 
                if predict-i*10 < number: 
                    break
            predict -= (i-1)*10   
            if number < predict: 
                predict -= 1
    return(count) # выход из цикла, если угадали

#Проверяем
score_game(game_core_v2)