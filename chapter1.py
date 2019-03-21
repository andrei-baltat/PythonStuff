

for i in range(1,21):
    if i == 4 or i == 13:
        print("{} is unlucky".format(i))
    elif i % 2 == 0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))