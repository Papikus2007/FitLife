# Проект FitLife - MVP версия 1.0

# Запрашиваем имя

user_name = input('Здравствуйте! Как Вас зовут? ')
# Запрашиваем возраст и переводим в int
user_age = int(input('Сколько Вам лет? '))

# Запрашиваем вес и переводим во float
user_weight = float(input('Какой Ваш вес? '))
# Запрашиваем рост и переводим во float
user_height = float(input('Какой Ваш рост в метрах /(например 1.75/) '))

# Рассчитываем bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)

# Подсчет воды
water_needed = user_weight * 30 / 1000

# Вывод результатов
print()
print(f'Отчёт для пользователя: {user_name} (возраст - {user_age})')
print(f'Ваш Индекс Массы Тела: {round(bmi, 1)}')
print(f'Рекомендуемая норма воды: {round(water_needed, 1)} л. в день')
print()
print("Расчет окончен. Будьте здоровы!")
