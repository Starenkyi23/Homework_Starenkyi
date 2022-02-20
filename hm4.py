# Task 1
import random
lst=[1,2,3,4,5,6,7,8,9,10]
ran= random.choice(lst)
que=input('Угадайте число, которое загадала программа от 1 до 10.Ваш вариат: ')
print(f'Ваш вариант {que}, а правльный вариант {ran}')

# Task 2
y=input('Введите ваше имя: ')
x=int(input('Введите ваш возраст: '))
z=x+1
print(f'Hello {y}, on your next birthday you’ll be {z} years')

# Task 3
import random
a=input('Введите слово: ')
for i in range(5):
    b=random.sample(a, len(a))
    b1= ''.join(random.sample(a, len(a)))
    print(b)
    print(b1)



# Task 4
r = input('Сколько будет 7 умножить на 8?\n Ответ: ')
h = 56
while r.isdigit():
    if int(r) == h:
        print('Молодец')
        break
    else:
        print('Попробуй еще!')
        break
else:
    print('Введите число')
#