# # Задание 1
# # Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

# students = [
#   {'first_name': 'Вася'},
#   {'first_name': 'Петя'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Маша'},
#   {'first_name': 'Петя'},
# ]

# names = {
# 	# 'Маша': 2,
# 	# 'Петя': 1,
# }

# for pupil in students:
# 	# print(pupil['first_name'])
# 	# ???
	
# 	if pupil['first_name'] not in names:
# 		names[pupil['first_name']] = 1
# 	else:
# 		names[pupil['first_name']] += 1


# # Задание 2
# # Дан список учеников, нужно вывести самое часто повторящееся имя.

# # for key, value in names.items():
# # 	print('{}: {}'.format(key, value))
# max_repetitions = max(names.values())

# for key, value in names.items():
# 	if value == max_repetitions:
# 		print('Самое частое имя среди учеников: {}'.format(key))

# # Задание 3
# # Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# school_students = [
#     [  # это – первый класс
#         {'first_name': 'Вася'},
#         {'first_name': 'Вася'},
#   ],

#     [  # это – второй класс
#         {'first_name': 'Маша'},
#         {'first_name': 'Маша'},
#         {'first_name': 'Оля'},
#   ]
# ]
# # ???

# # # Пример вывода:
# # # Самое частое имя в классе 1: Вася
# # # Самое частое имя в классе 2: Маша

# for each_class in school_students:

#     names = {}

#     for pupil in each_class:
        
#         if pupil['first_name'] not in names:    
#             names[pupil['first_name']] = 1
#         else: 
#             names[pupil['first_name']] += 1

#     max_repetitions = max(names.values())	

#     for key, value in names.items():
#         if value == max_repetitions:
            
#                  print('Самое частое имя в группе {}: {}'.format(school_students.index(each_class) + 1, key))



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print(school[0]['students'][1]['first_name'])


for key, value in is_male.items():
    print(value)














