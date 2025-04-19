print("Добро пожаловать в игру Виселица")
a = input()
b = 5
d = "аоэеиыуёюяaeouyi"
while b > 0:
    c = 0
    for i in a:
            if i in d:
                print(i, end=" ")
            else: 
                print("_", end=" ")
                c += 1
    if c == 0:
        print("\nТы выиграл(а)!")
        break
    f = input("\nНазови бувку:")
    d += f
    if f not in a:
        b -= 1
        print("Не угадал(а)")
        print("Осталось попыток:", b)
        if b < 5:
            print(" | ")
        if b < 4:
            print(" O ")
        if b < 3:
            print("/|\ ")
        if b < 2:
            print(" | ")
        if b < 1:
            print("/'\ ")
        if b == 0:
            print("Это слово:", a)
