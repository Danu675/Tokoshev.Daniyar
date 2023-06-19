# Работа с файлами.
# w - write
# a - add
# x - unique filename
# r - read
from random import choice

students = [14, 8, 12, 7, 17, 3, 4, 11, 13]

with open('results.txt', 'w') as results:
    results.write('RESULTS: 31-1')

while students:
    student_id = choice(students)
    name = input(f'name for {student_id}: ').title()
    with open('темы') as topics:
        random_topic = choice(topics.readlines())
    rate = int(input(f'rate for {name}: \n'
                     f'{random_topic}: '))
    with open('results.txt', 'a') as student_result:
        student_result.write(f'\n{name} {rate}')
    students.remove(student_id)






# with open('other.txt') as file:
#     print(file.readlines()[-2])


# with open('темы', 'r') as file:
#     print(file.read())
    # print(file.read())
    # for i in file.readlines():
    #     print(i)


# file = open('new.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан!')
# file.close()

# with open('new.txt', 'a') as file:
#     file.write('\n222')

# with open('other.txt', 'x') as new_file:
#     new_file.write('new data!!!')
