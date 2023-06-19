ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ivetns = list(filter(lambda i: i % 2 == 0, ten))
print(list(map(lambda i: i ** 2, ivetns)))


def get_ivents(ivents, ten1=1):
    while True:
        a = input("Введите индекс = ")
        if a == "exit":
            break
        elif a.isdigit():
            try:
                print(ivents[int(a)])
            except:
                print(f"Введите индекс от {ivents.index(ivents[0])} до {ivents.index(ivents[-1])}")
        else:
            print("Введите только числа")


get_ivents(ivetns)
