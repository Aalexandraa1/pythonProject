A = int(input('Введите первое число'))
B = int(input('Введите второе число'))
C = int(input('Введите третье число'))
if ((A < 45) and (B >= 45) and (C >= 45)) or \
        ((A >= 45) and (B < 45) and (C >= 45)) or \
        ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')