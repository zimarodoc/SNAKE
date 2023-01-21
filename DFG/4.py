a = int(input("Введите 7 значное число: "))
cht = 0
n_cht = 0
summ = 0
b = []
for i in str(a):
    i = int(i)
    if i % 2 == 0:
        cht += 1
    else:
        n_cht += 1
if cht > n_cht:
    for i in str(a):
        i = int(i)
        summ += i
    print("Сумма:", summ)
else:
    for i in str(a):
        i = int(i)
        b.append(i)
    pr = b[0] * b[2] * b[5]
    print("Произведение 1, 3, 6 цифры : ", pr)