while 0 < 1:

    n = int(input("Введите число: "))
    count = 0
    for i in range(1, n + 1):
        d = sum(list(map(int, str(i))))
        if i % 9 == 0:
            count += 1
        elif d == 15:
            count += 1
    print(count)
