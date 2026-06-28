# Проект FitLife - MVP версия 1.0

# константа - количество воды (мл) на 1 кг веса
WATER_PER_KG = 30
# константа - количество мл в литре воды
ML_IN_LITRE = 1000

# Запрашиваем имя, удаляем пробелы, проверяем корректность ввода
while True:
    user_name = input('Здравствуйте! Как Вас зовут? ').strip()

    if user_name:
        break
    else:
        print('Пожалуйста, введите имя')

# Запрашиваем возраст и переводим в int, удаляем пробелы,
# проверяем корректность ввода
while True:
    user_age_input = input('Сколько Вам лет? ').strip()

    try:
        user_age = int(user_age_input)
        if 18 <= user_age <= 80:
            break
        else:
            print('Пожалуйста, введите возраст от 18 до 80')
    except ValueError:
        print('Пожалуйста, введите корректное целое число')

# Запрашиваем вес и переводим во float, проверяем корректность ввода
while True:
    user_weight_input = input('Ваш вес? ').strip()
    try:
        user_weight = float(user_weight_input)
        if user_weight > 0:
            break
        else:
            print('Вес должен быть больше 0')
    except ValueError:
        print('Пожалуйста, введите число (можно с точкой, например 77.7)')

# Запрашиваем рост и переводим во float, удаляем пробелы,
# проверяем корректность ввода
while True:
    user_height_input = input('Ваш рост в метрах /(например 1.75/)? ').strip()
    try:
        user_height = float(user_height_input)
        if user_height > 0:
            break
        else:
            print('Рост должен быть больше 0')
    except ValueError:
        print('Пожалуйста, введите число (можно с точкой, например 1.77)')

# Рассчитываем bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)

if bmi < 18.5:
    bmi_description = 'дефицит массы тела'
if 18.5 < bmi < 24.9:
    bmi_description = 'нормальная масса тела'
if 25.0 < bmi < 29.9:
    bmi_description = 'избыточная масса тела (предожирение)'
if bmi > 30:
    bmi_description = 'ожирение'

# Подсчет воды
water_needed = user_weight * WATER_PER_KG / ML_IN_LITRE

print()
print(f'Отчёт для пользователя: {user_name} (возраст - {user_age})')
print(f'Ваш Индекс Массы Тела: {round(bmi, 1)}. У Вас {bmi_description}')
print(f'Рекомендуемая норма воды: {round(water_needed, 1)} л. в день')
print()
print("Расчет окончен. Будьте здоровы!")
