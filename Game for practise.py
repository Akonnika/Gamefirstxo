from colorama import init, Fore
init(autoreset=True)
print(Fore.BLUE + 'Привет! давай сыграем в крестики нолики?')
c = input('Ваш ответ: да / нет: ')
if c == 'да':
    print(Fore.GREEN + 'Отлично, начинай!')
elif c != 'да' and c !='нет':
    print(Fore.RED + 'Балуешься? Тогда начнем игру! \n ХА-ХА')
else:
   import sys
   sys.exit(Fore.RED + "Ладно, в другой раз :(")

#объявляем поле
field = [['-'] * 3 for _ in range(3)]
def print_field(f):
    print(' ', 0, 1, 2)
    for i in range(len(field)):
        print(str(i), *field[i])
print_field(field)
def users_beh(f):
    while True:
        place = input("Введи координаты через пробел: ").split()
        if len(place)!=2:
            print('Внимательнее! Нужны 2 координаты :)')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Нужно ввести числа от 0 до 2')
            continue
        x,y = map(int, place)
        if not (x < 3 and x >= 0 and y < 3 and y >= 0):
            print('Нужно ввести числа от 0 до 2')
            continue
        if f[x][y] != '-':
            print('Координата уже занята')
            continue
        break
    return x,y
print(users_beh(field))

def win_var(f, users):
    def check_winer(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range (3):
        if check_winer(f[n][0], f[n][1], f[n][2], user) or \
            check_winer(f[0][n], f[1][n], f[2][n], user) or \
            check_winer(f[0][n], f[1][n], f[2][n], user) or \
            check_winer(f[0][0], f[1][1], f[2][2], user) or \
            check_winer(f[2][0], f[1][1], f[0][2], user):
                return True
    return False

turn = 0
while True:
    if turn % 2 == 0:
        user = 'x'
    else:
        user = 'o'
    print_field(field)
    x,y = users_beh(field)
    field[x][y] = user

    if turn == 9:
        print ("Победила дружба")
    if win_var(field, user):
        print(f'урааааа! Выиграл {user}!!!!!!!!!!')
        print_field(field)
        break
    turn += 1



