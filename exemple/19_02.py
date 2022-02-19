#1
# list_1 = [2, 66, 54, 75, 57, 3]
# index = 0
# sum = 0
# while index < len(list_1):
#     sum += list_1[index]
#     index += 1
# avg = sum/len(list_1)
# print(f'Average result is: {avg}')


#2
# firstList = [1,2,3]
# secondList=[]
#
# counter = len(firstList)-1
#
# while counter >= 0:
#     secondList.append(firstList[counter])
#     counter -= 1
#     continue
# print(secondList)


#3
# firstList_1 = [1,2,3]
# secondList_1=[]
#
# counter_1 = 0
#
# while counter_1 < len(firstList_1):
#     secondList_1.append(firstList_1[counter_1])
#     counter_1 += 1
#     continue
# print(secondList_1)

#4
# def Remove(tuples):
#     tuples = [t for t in tuples if t]
#     return tuples
# tuples = [(), ('ram'), (), ('laxman', 'sita'),
# ('krishna', 'akbar', '45'), ('', ''), ()]
# print(Remove(tuples))

#5
# x= [i for i in range(700, 4000, 130)]
# print(x)

#6
# dict = {'artem': '0931111111', 'igor': '0932222222'}
# while 1:
#     name = (input('type name to view or type "q" to exit: '))
#     name = name.lower()
#     if name == 'q':
#         break
#     if name in dict.keys():
#         print(f'{name.capitalize()}: tel.:{dict.get(name)}')
#         del_c = input('What to do? Delete? (yes/no)')
#         if del_c.lower() == 'yes':
#             dict.pop(name)
#         else:
#             pass
#     else:
#         number_add = input('There no contact in address book, please type its nuber: ')
#         if number_add.isdigit():
#             dict[name] = number_add
#         else:
#             number_add= input('Please, type correct number with digits only')
#             dict[name] = number_add

#7
# tpl_1 = ('hello', 3, 5, 'world')
# tpl_2 = ('he','he','he','he')
# def compare_f (tpl):
#     for i in tpl:
#         for j in tpl:
#             if j !=i:
#                 return False
#     return True
# print(compare_f(tpl_1))
# print(compare_f(tpl_2))

#8
# set_1={1,5,7,9}
# set_2={5,6,8,1}
# set_3= set()
# for i in set_1:
#     if i in set_2:
#         pass
#     else:
#         set_3.add(i)
# for i in set_2:
#     if i in set_1:
#         pass
#     else:
#         set_3.add(i)
# print(set_3)
#
# A = {'a', 'b', 'c', 'd'}
# B = {'c', 'd', 'e' }
# print(A.symmetric_difference(B))

#9
# print([(x,y) for x in [1,2,3,4,5,6,7] for y in [1,2,3,4,5,6,7] if x==y])

#10
# a= [1,2,3,4,5,6,7,8,9,10]
# b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
#         a.remove(i)
#     else:
#         pass
# print(a)
# print(b)
#
# c= [1,2,3,4,5,6,7,8,9,10]
# d= ([i for i in c if i%2!=0 ])
# e= ([j for j in c if j%2==0 ])
# print(d)
# print(e)
#
# print(f'{[i for i in [1,2,3,4,5,6,7,8,9,10] if i%2!=0]}, {[j for j in [1,2,3,4,5,6,7,8,9,10] if j%2==0 ]}')