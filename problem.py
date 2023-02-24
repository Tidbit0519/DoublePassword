count = 0

password = input()
array1 = []
array2 = []

for i in range(len(password)):
    if(i < 4):
        array1.append(password[i])
    elif(password[i] == " " or password[i] == "/n"):
        continue
    else:
        array2.append(password[i])

for i in range(len(array1)):
    if(array1[i] == array2[i]):
        continue
    else:
        count += 2

count += 1

print(count)