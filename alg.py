son1 = int(input('Birinchi son: '))
son2 = int(input('Ikkinchi son: '))
son3 = int(input('Uchinchi son: '))


if son1 > son2:
    if son1 > son3:
        print(f'Birinchi son eng kattasi')
    else:
        print('Uchinchi son eng kattasi')
if son2 > son1:
    if son2 > son3:
        print('Ikkinchi son eng kattasi')
    else:
        print('Uchinchi son eng kattasi')
        