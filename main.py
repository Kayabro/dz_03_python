# line = int(input('Длина спсика: '))
# from random import randint
# list = [randint(0, 100) for i in range(line)]
#
# x = int(input('Искомое: '))
# diff_min = x - list[0]
# counter = 0
# result = 0
#
# if x in list:
#     for i in list:
#         if i == x:
#             counter += 1
# elif x not in list:
#     for i in list:
#         if abs(x - i) <= abs(diff_min):
#             diff_min = x - i
#             result = i
#
# if counter > 0:
#     print(f' число {x} в списке {list}, встречается {counter}')
# else:
#     print(f'Максимально близкое к {x} число в списке {list}, будет {result}')
#



# Вторая Задача

# import re
# en = {1: 'AEIOULNSTR',
#       2: 'DG',
#       3: 'BCMP',
#       4: 'FHVWY',
#       5: 'K',
#       8: 'JZ',
#       10: 'QZ'}
# ru = {1: 'АВЕИНОРСТ',
#       2: 'ДКЛМПУ',
#       3: 'БГЁЬЯ',
#       4: 'ЙЫ',
#       5: 'ЖЗХЦЧ',
#       8: 'ШЭЮ',
#       10: 'ФЩЪ'}
# text = input('Укажите текст для подсчета очков :')
# flag = False
# if re.search('[А-Я]', text.upper()):
#     flag = True
#
# if flag == True:
#     print(sum([k for i in text for k, v in ru.items() if i in v]))
# else:
#     print(sum([k for i in text for k, v in en.items() if i in v]))


