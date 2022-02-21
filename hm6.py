# Словники та оператор циклу for. Генератори списків/словників та інших колекцій
#Task 1
a = 'I am robot, you are potato'
dict_1 = {}
for i in a:
    dict_1.update({i:a.index(i)})
print(dict_1)

#Task 2
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
z=[]
for key in stock:
    z.append(stock[key] * prices[key])
print(sum(z))

#Task 3
t=tuple(i for i in range(1, 11))
z=tuple(i ** 2 for i in range(1, 11))
print(t,'\n',z,sep='')