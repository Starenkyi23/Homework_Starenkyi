# Списки, кортежі та множини
#Task 1
import random
i= random.sample(range(0, 1000), 10)
print(i,'\n',max(i))

#Task 2 (Я не придумал как сделать с помощью While)
import random
a= random.sample(range(0, 20), 10)
b= random.sample(range(0, 20), 10)
z=[]
for i in a:
    for j in b:
        if i == j:
            z.append(i)
print(a,'\n',b,'\n',z)

#Task 3
lst= list(range(0, 101))
lst_1=[]
num = 0
while num < len(lst):
    if lst[num] %7 == 0:
        if lst[num] %5 != 0:
            lst_1.append(num)
    num += 1
print(lst_1)
