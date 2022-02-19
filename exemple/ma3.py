#1
list_1 = [2, 66, 54, 75, 57, 3]
index = 0
sum = 0
while index < len(list_1):
    sum += list_1[index]
    index += 1
avg = sum/len(list_1)
print(f'Average result is: {avg}')


#2
firstList = [1,2,3]
secondList=[]

counter = len(firstList)-1

while counter >= 0:
    secondList.append(firstList[counter])
    counter -= 1
    continue
print(secondList)


#3
firstList_1 = [1,2,3]
secondList_1=[]

counter_1 = 0

while counter_1 < len(firstList_1):
    secondList_1.append(firstList_1[counter_1])
    counter_1 += 1
    continue
print(secondList_1)
