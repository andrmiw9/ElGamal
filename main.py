import random


def isPrime(num):
    counter = abs(num) // 2
    if (counter == 1):
        return True
    while (counter > 1):
        if (num % counter == 0):
            return False
        counter -= 1
    return True


def Multipliers(num):
    ls = []
    num = abs(num)
    while num != 1:
        i = num // 2 + 1
        print(f'i на итерации {i}')
        if (i == 1):
            break
        while i != 1:
            if num % i == 0:
                ls.append(i)
                break
            i -= 1
        num /= i
        print(f'Найден множитель {i}')
    print(f'Финальный список множителей: {ls}')
    return ls


def Checker(num):
    j = 2
    flag = False
    while True:
        for i in range(1, num - 1):
            if (j ** i % num == 0):
                flag = False
                break
            else:
                flag = True
        if (flag):
            return j
        j += 1
    pass


class Abonent:
    def __init__(self, name, p, g):
        self.name = name
        self.x = self.chooseX(p)
        self.y = g ** self.x % p

    def chooseX(self, p):
        return random.randint(1, p - 1)

    def choose_sessionK(self, p):
        self.k = random.randint(2, p - 2)
        return self.k

    pass


def main():
    while True:
        q = random.randint(50, 1000)
        p = 2 * q + 1
        if not isPrime(q) or not isPrime(p):
            # print(f'Число q и/или p не простое число!')
            continue
        else:
            break

    print(f'p: {p}, q: {q}')
    g = -1
    for i in range(2, p - 1):
        if i ** q % p != 1:
            g = i
            break
    if g == -1:
        print(f'Число g найти не удалось :(')
        exit(-1)
    print(f'p: {p}, q: {q}, g: {g}')

    abonents = []
    Abont1 = Abonent('Abonent1', p, g)
    abonents.append(Abont1)
    Abont2 = Abonent('Abonent2', p, g)
    abonents.append(Abont2)
    print(f'{Abont1.name}: '
          f'p:{p}, g:{g}, x:{Abont1.x}, y:{Abont1.y}, session key: пока неизвестен')
    print(f'{Abont2.name}: '
          f'p:{p}, g:{g}, x:{Abont2.x}, y:{Abont2.y}, session key: пока неизвестен')

    to_enc = r"some really cool m6ss4g6"
    print(f'Изначальный текст: {to_enc}')

    if len(to_enc) >= p:
        print(f'Извините, сообщение слишком длинное для текущего p ({p})')
        exit(-1)

    to_enc = [ord(char) for char in to_enc.lower()]
    print(f'Текст в виде цифр: {to_enc}')

    for ab in abonents:  # шифровка
        ab.choose_sessionK(p)
        ab.r = g ** ab.k % p
        e = []
        # e = (to_enc * ab.y ** ab.k) % p
        for num in to_enc:
            if (num == -64):
                e.append(num)
                continue
            e.append((num * ab.y ** ab.k) % p)

        ab.e = e
        print(f'Abonent: {ab.name}, r:{ab.r}, e (шифротекст):{ab.e}')
        # условный send_to_abonent(abonent)

    for ab in abonents:  # расшифровка
        Mmod = []
        for num in ab.e:
            if num == -64:
                Mmod.append(num)
                continue
            Mmod.append((num * ab.r ** (p - 1 - ab.x)) % p)
        print(f'Абонент {ab.name}, полученные числа после расшифровки: {Mmod}')
        decoded = [chr(n) for n in Mmod]
        print(f'Абонент {ab.name}, полученный текст после расшифровки: {decoded}')

    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
