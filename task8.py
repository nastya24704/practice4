print('Здравствуйте! Как Вас зовут?')
name=input()
print('Очень приятно,', name, '!', 'Меня зовут Марк')
print('Сколько Вам лет?')
age=int(input())
if age<78:
    print('Да,', name, 'я старше Вас на', 78-age, 'лет.')
else:
    print('Да,', name, 'Вы старше меня на', age-78, 'лет.')
print('Вам нравится программировать?')
answer=input()
if answer=='да':
    print('Превосходно! Уверен, у Вас получится написать множество полезных и хороших программ.')
else:
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня.')
