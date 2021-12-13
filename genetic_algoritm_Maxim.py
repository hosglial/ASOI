# Описать функционирование одной эпохи генетического алгоритма на
# примере произвольной задачи (не менее пяти признаков закодировать
# случайным образом, начальная популяция содержит не менее 10 особей).
# Использовать следующие параметры генетического алгоритма: фитнессфункция – сумма всех бит особи, деленная на количество особей в популяции;
# метод отбора – отбор усечением с использованием принципа элитизма; оператор
# скрещивания – двухточечный кроссовер; оператор мутации – одноточечная
# мутация.


from random import choices, randint, random


def select_rand(data):
    return choices(
        list(range(10)), weights=list(i["weight"] for i in data), k=1)


def breed(first, second):
    fbreed = ""
    sbreed = ""

    points = (randint(1, len(first)), randint(1, len(first)))
    print(points)
    fpoint, spoint = min(points), max(points)

    for i in range(len(first)):
        if i > fpoint and i < spoint:
            fbreed += first[i]
            sbreed += second[i]
        else:
            fbreed += second[i]
            sbreed += first[i]
    return fbreed, sbreed


def mutate(item):
    r1, r2 = randint(0, len(item)), randint(0, len(item))
    pos1 = min(r1, r2)
    pos2 = max(r1, r2)

    reversable = item[pos1:pos2]
    newitem = item[:pos1] + reversable[::-1] + item[pos2:]
    return newitem


mass = [1, 2, 13, 14, 12]

feathures = [{"bin": "", "dec": i} for i in mass]

for i in feathures:
    i["bin"] = bin(i["dec"])[2:]
    i["gray"] = bin(i["dec"] ^ (i["dec"] >> 1))[2:]
    i['bin'] = i['bin'].rjust(4, "0")

# print(feathures)
#
# indivs = [{"feath": f"{feathures[randint(0, 4)]['bin']}{feathures[randint(0, 4)]['bin']}"} for i in range(10)]
# for i in indivs:
#     print(i)

indivs = [
    {'feath': '11000001'},
    {'feath': '00010001'},
    {'feath': '11010010'},
    {'feath': '00101110'},
    {'feath': '11100010'},
    {'feath': '11001110'},
    {'feath': '11100001'},
    {'feath': '00100010'},
    {'feath': '00100001'},
    {'feath': '11011101'}
]
