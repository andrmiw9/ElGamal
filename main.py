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
        print(f'i на итерации ')
        if(i == 1):
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


def main():
    multls = []
    num = random.randint(1000, 20000)
    while True:
        if isPrime(num):
            multls = Multipliers(num - 1)
            break
        num = random.randint(1000, 20000)
    print(f'Found number {num}')

    print(f'')
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
