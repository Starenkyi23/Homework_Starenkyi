#Task 1
y=str(input("str: "))
if len(y) >= 2:
    print(y[0:2],y[-2:len(y)],sep="")
else: len(y) < 2,
print(" ")

#Task 2
x=int(input("phone number: "))
if len(str(x)) < 10:
    print("please, write correct number")
elif len(str(x)) == 10:
    print("OK")

#Task 3
z='nick'
t=input('Введите имя: ')
if t.lower() == z:
    print(True)
else:
    print(False)
