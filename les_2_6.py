goods, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Вы не ввели название товара')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('значение не является числом')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    goods.append((
        order,
        {
            'название': title,
            'цена': price,
            'колличество': amount,
            'единицы измерения': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(goods)

    q = input('Продолжить формирование списка? (y/N)) ')
    if q.lower() == 'y':
        break

analitics = {
    'название': [],
    'цена': [],
    'стоимость': [],
    'единицы измерения': set()
}

for _, item in goods:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['стоимость'].append(item['стимость'])
    analitics['единицы измерения'].add(item['единицы измерения'])

print(analitics)

