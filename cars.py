import json
from copy import deepcopy

# Попробуем загрузить базу данных машин
try:
    with open("carsbase.json", "r") as cars:
        d = json.load(cars)  
except (FileNotFoundError, json.JSONDecodeError):
    d = {}

def display_cars():
    print(f"{'№':<5}{'Марка машины':<15}{'Цвет':<10}{'Модель двигателя':<20}{'Двери открыты?':<15}{'Фары включены?':<15}{'Место на парковке':<15}")
    print("-" * 145)
    for i in sorted(d.keys(), key=int):
        print(f"{str(int(i) + 1):<5}{d[i][0]:<15}{d[i][1]:<10}{d[i][2]:<20}{d[i][3]:<15}{d[i][4]:<15}{d[i][5]:<15}")

def print_menu():
    print('1. Вывести список машин')
    print('2. Добавить машину')
    print('3. Изменить характеристики машины')
    print('4. Поиск')
    print('5. Удалить машину')
    print('6. Выйти')

def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input

# Функция для проверки, является ли ввод корректным
def is_yes_no(value):
    return value in ["Yes", "No"]

vsm = 0
while vsm != 6:
    print_menu()
    while True:
        try:
            vsm = int(input("Выберите действие: "))
            if 1 <= vsm <= 6:
                break 
            else:
                print('Некорректный ввод. Введите число от 1 до 6.')
        except ValueError:
            print('Некорректный ввод. Попробуйте еще раз.')

    if vsm == 1:
        display_cars() 
    elif vsm == 2:
        new_car = []
        new_car.append(input('Введите марку машины: '))  
        new_car.append(input('Введите цвет машины: '))
        new_car.append(input('Введите модель двигателя: '))  

        # Состояние фар
        new_car.append(get_valid_input('Фары включены? (Yes/No): ', is_yes_no))

        # Состояние дверей
        new_car.append(get_valid_input('Двери открыты? (Yes/No): ', is_yes_no))

        new_car.append(input('Введите место на парковке: '))
        
        # Добавление автомобиля в словарь d
        d[len(d)] = new_car

        # Сохраняем изменения в файл
        with open("carsbase.json", "w") as cars:
            json.dump(d, cars, indent=2)
    elif vsm == 3:
        print('Выберите машину для изменения характеристик:')
        display_cars() 
        while True:
            try:
                hr = input("Введите номер машины: ")
                hr = str(int(hr) - 1)
                if hr in d.keys():
                    carhr = deepcopy(d[hr])
                    break 
                else:
                    print('Некорректный ввод. Выберите номер от 1 до', len(d))
            except (ValueError, IndexError):
                print('Некорректный ввод. Попробуйте еще раз.')

        while True:
            print('Какую характеристику изменить?')
            print('1. Марка машины')
            print('2. Цвет')
            print('3. Модель двигателя')
            print('4. Состояние фар')
            print('5. Состояние дверей')
            print('6. Место на парковке')
            print('7. Выйти')
            while True:
                try:
                    pn = int(input())
                    if 1 <= pn <= 7:
                        break
                    else:
                        print('Некорректный ввод. Введите число от 1 до 7.')
                except ValueError:
                    print('Некорректный ввод. Попробуйте еще раз.')
            
            if pn == 1:
                carhr[0] = input('Введите марку машины: ')
            elif pn == 2:
                carhr[1] = input('Введите цвет машины: ')
            elif pn == 3:
                carhr[2] = input('Введите модель двигателя: ')
            elif pn == 4:
                carhr[3] = get_valid_input('Фары включены? (Yes/No): ', is_yes_no)
            elif pn == 5:
                carhr[4] = get_valid_input('Двери открыты? (Yes/No): ', is_yes_no)
            elif pn == 6:
                carhr[5] = input('Введите новое место на парковке: ')
            elif pn == 7:  
                break

            d[hr] = carhr  
            with open("carsbase.json", 'w') as car1:
                json.dump(d, car1, indent=2) 

    elif vsm == 4:
        search = input('Введите искомый объект: ')
        found = False
        for i in d:
            cars = d[i]
            if search in cars: 
                found = True
                print(f"Найденная машина: {', '.join(cars)}")
        if not found:
            print('Такой машины не найдено!')
    
    elif vsm == 5:
        display_cars() 
        while True:
            try:
                dell = input('Выберите машину для удаления: ')
                dell = str(int(dell) - 1)
                if dell in d:  
                    del d[dell] 
                    print('Машина удалена.')

                    # Обновляем ключи в словаре
                    updated_d = {}
                    for idx, key in enumerate(sorted(d.keys(), key=int)):
                        updated_d[idx] = d[key]
                    d = updated_d

                    # Сохраняем изменения в файл
                    with open("carsbase.json", 'w') as car1:
                        json.dump(d, car1, indent=2) 
                    break
                else:
                    print('Некорректный номер машины.')
            except ValueError:
                print('Некорректный ввод. Попробуйте еще раз.')