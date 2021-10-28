# 6. Просчитать одну итерацию цикла обучения по Δ-правилу однослойной
# бинарной неоднородной нейронной сети, состоящей из 2 нейронов и имеющей
# функции активации: сигмоидальную (k=1) и линейную (k=0,6). В качестве
# обучающей выборки использовать таблицу истинности для операций импликации
# и конъюнкции (не использовать первую строчку таблицы).
# Синаптические веса задать случайным образом.
from math import exp, tan
from random import random


class Neuron:
    def __init__(self, func_type, k=None, T=None):
        self.func_type = func_type
        if k:
            self.k = k
        if T:
            self.T = T

    def activate(self, S):
        res = 0
        if self.func_type == 'Пороговая':
            res = 1 if S >= self.T else 0

        elif self.func_type == 'Линейная':
            res = self.k * S

        elif self.func_type == 'Сигмоидальная':
            res = 1 / (1 + exp(-S * self.k))

        elif self.func_type == 'Гиперболический тангенс':
            res = tan(S / self.k)

        return res


double_mass = [0, 1]
data_dict = {
    (0, 0): (1, 0),
    (0, 1): (1, 0),
    (1, 0): (0, 0),
    (1, 1): (1, 1)

}

train_dict = data_dict
train_dict.pop((0, 0))
print("train_dict")
for k, v in train_dict.items():
    print(k, ":", v)

neuron_mass = []

neuron_mass.append(Neuron('Сигмоидальная', k=1))
neuron_mass.append(Neuron('Линейная', k=0.6))

# Рандомные веса
# w1 = {i: {j: random().__round__(2) for j in range(len(neuron_mass))} for i in range(len(neuron_mass))}
#
w1 = {0: {0: 0.74, 1: 0.65}, 1: {0: 0.92, 1: 0.0}}
print("\nweights")
for k, v in w1.items():
    print(k, ':', v)

ans = {}
for i in data_dict:
    ans[i] = (
        neuron_mass[0].activate(i[0] * w1[0][0] + i[1] * w1[0][1]),
        neuron_mass[1].activate(i[0] * w1[1][0] + i[1] * w1[1][1]),
    )
print('\nans')
for key, value in ans.items():
    print(key, ":", value)
    break

eps = {}
print('\neps')
for key, value in ans.items():
    eps[key] = ((train_dict[key][0] - value[0]).__round__(2), (train_dict[key][1] - value[1]).__round__(2))
    print(key, ":", eps[key])
    break

n = 0, 8

w2 = {
    0: {},
    1: {}
}

print('\nweights changed')
for k1 in w1:
    for k2 in w1[k1]:
        w2[k1][k2] = (w1[k1][k2] - eps[(0,1)][k1]).__round__(2)

for k, v in w2.items():
    print(k, ':', v)


print('\nError')
print(sum(pow(i,2) for i in eps[(0,1)]))




# ans = {}
# for i in data_dict:
#     ans[i] = (
#         neuron_mass[0].activate(i[0] * w2[0][0] + i[1] * w2[0][1]),
#         neuron_mass[1].activate(i[0] * w2[1][0] + i[1] * w2[1][1]),
#     )
# print('\nans2')
# for key, value in ans.items():
#     print(key, ":", value)
#     break
#
# eps = {}
# print('\neps')
# for key, value in ans.items():
#     eps[key] = ((train_dict[key][0] - value[0]).__round__(2), (train_dict[key][1] - value[1]).__round__(2))
#     print(key, ":", eps[key])
#     break
#
# print('\nError2')
# print(sum(pow(i,2) for i in eps[(0,1)]))