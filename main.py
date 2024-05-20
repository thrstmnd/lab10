import json

def zadacha1():
    with open('C:\Users\user\PycharmProjects\lab10\продукты.json', encoding='utf-8') as f:
        file = json.load(f)
    for products in file['products']:
        print('Название: ' + products['name'])
        print('Цена: ' + products['price'])
        print('Вес: ' + products['weight'])
        if products['available'] == 'да':
            print('В наличии')
        else:
            print('Нет в наличии!')
        print('')

def zadacha2():
    with open('C:\Users\user\PycharmProjects\lab10\продукты.json', encoding='utf-8') as f:
        file = json.load(f)
    newproducts = {}
    newproducts['name'] = input('Название: ')
    newproducts['price'] = input('Цена: ')
    newproducts['weight'] = input('Вес: ')
    newproducts['available'] = input('Наличие(да/нет): ')
    file['products'].append(newproducts)
    with open('C:\Users\user\PycharmProjects\lab10\продукты.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, allow_nan=False, indent = 2)
    with open('C:\Users\user\PycharmProjects\lab10\продукты.json', encoding='utf-8') as f:
        file = json.load(f)
    for products in file['products']:
        print('Название: ', products['name'])
        print('Цена: ', products['price'])
        print('Вес: ', products['weight'])
        if products['available'] == 'да':
            print('В наличии')
        else:
            print('Нет в наличии!')
        print('')

def zadacha3():
    with open('C:\Users\user\PycharmProjects\lab10\en-ru.txt', 'r', encoding='utf-8') as f:
        rufile = {}
        for filelines in f:
            eng, rusw = filelines.strip()
            eng, rusw = filelines.split('-')
            for rus in rusw.split(','):
                if rus not in rufile:
                    rufile[rus] = [eng]
                else:
                    rufile[rus].append(eng)
    with open('for10/ru-en.txt', 'w', encoding='utf-8') as f:
        for rus in sorted(rufile.keys()):
            engw = ','.join(sorted(rufile[rus]))
            f.write(f'{rus} - {engw}\n')
    with open('for10/en-ru.json', 'w', encoding='utf-8') as f:
        json.dump(rufile, f, allow_nan=False, indent=2)