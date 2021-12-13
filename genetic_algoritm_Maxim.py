# 20 Описать функционирование одной эпохи генетического алгоритма на
# примере произвольной задачи (не менее пяти признаков закодировать
# случайным образом, начальная популяция содержит не менее 10 особей).
# Использовать следующие параметры генетического алгоритма: фитнессфункция – сумма всех бит особи, деленная на количество особей в популяции;
# метод отбора – отбор усечением с использованием принципа элитизма; оператор
# скрещивания – двухточечный кроссовер; оператор мутации – одноточечная
# мутация.
from random import choices, randint, random
from pprint import pprint
from tabulate import tabulate


def select_rand():
    return choices(
        list(range(10)))


def breed(first, second):
    first = first['feath']
    second = second['feath']
    fbreed = ""
    sbreed = ""

    points = (randint(1, len(first)), randint(1, len(first)))
    fpoint, spoint = min(points), max(points)

    for i in range(len(first)):
        if i > fpoint and i < spoint:
            fbreed += second[i]
            sbreed += first[i]
        else:
            fbreed += first[i]
            sbreed += second[i]
    return fbreed, sbreed


def mutate(item: str):
    r = randint(0, len(item))
    replacement = '0' if item[r] == '1' else '1'
    ans = item[0:r] + replacement + item[r + 1:]
    return ans


mass = [1, 2, 13, 14, 12]

feathures = [{"bin": "", "dec": i} for i in mass]

for i in feathures:
    i["bin"] = bin(i["dec"])[2:]
    i["gray"] = bin(i["dec"] ^ (i["dec"] >> 1))[2:]
    i['bin'] = i['bin'].rjust(4, "0")

indivs = [
    {'num': 1, 'feath': '11000001'},
    {'num': 2, 'feath': '00010001'},
    {'num': 3, 'feath': '11010010'},
    {'num': 4, 'feath': '00101110'},
    {'num': 5, 'feath': '11100010'},
    {'num': 6, 'feath': '11001110'},
    {'num': 7, 'feath': '11100001'},
    {'num': 8, 'feath': '00100010'},
    {'num': 9, 'feath': '00100001'},
    {'num': 10, 'feath': '11011101'}
]

for i in indivs:
    i['weight'] = i["feath"].count("1") / len(indivs)
print('start_population')
print(tabulate(indivs, headers={'num': 'num', 'feath': 'Feathure'}))

feaths = [i['weight'] for i in indivs]
avg = sum(feaths) / len(feaths)
print(f'avg = {round(avg, 2)}')

# отбор
print('\nотбор')
T = 0.5
selected_nums = []
for i in indivs:
    if i['weight'] >= 0.4:
        selected_nums.append(i['num'])

pairs = []
for i in range(int(len(indivs) / 2)):
    pairs.append(choices(selected_nums, k=2))

pairs = [(7, 3), [4, 6], [3, 10], [4, 7], [3, 6]]

print(tabulate(pairs))

# скрещивание
print('\nскрещивание')
breeded_pairs = []
for i, j in pairs:
    breeded_pairs.append(breed(indivs[i - 1], indivs[j - 1]))

breeded_arr = []
for i, j in breeded_pairs:
    breeded_arr.append([i, i.count('1') / len(indivs)])
    breeded_arr.append([j, j.count('1') / len(indivs)])

print(tabulate(breeded_arr))


# мутация
print('\nмутация')
mutated_arr = []
for i in indivs:
    mutated = mutate(i['feath'])
    mutated_arr.append([mutated, mutated.count('1') / len(indivs)])

print(tabulate(mutated_arr))
