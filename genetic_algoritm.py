from random import choices, randint, random


def select_rand(data):
    return choices(
        list(range(10)), weights=list(i["weight"] for i in data), k=1)

def breed(first,second):
    fbreed = ""
    sbreed = ""
    for i in range(len(first)):
        if random() > 0.5:
            fbreed += first[i]
            sbreed += second[i]
        else:
            fbreed += second[i]
            sbreed += first[i]
    return fbreed, sbreed

def mutate(item):
    r1,r2 = randint(0,len(item)), randint(0,len(item))
    pos1 = min(r1,r2)
    pos2 = max(r1,r2)

    reversable = item[pos1:pos2]
    newitem = item[:pos1] + reversable[::-1] + item[pos2:]
    # print(item)
    # print(newitem)
    return newitem


mass = [1, 2, 13, 14, 12]

feathures = [{"bin": "", "dec": i} for i in mass]

for i in feathures:
    i["bin"] = bin(i["dec"])[2:]
    i["gray"] = bin(i["dec"] ^ (i["dec"] >> 1))[2:]
    i['bin'] = i['bin'].rjust(4, "0")

# print(feathures)

# indivs = [{"feathure_s" : f"{feathures[random.randint(0,4)]['bin']}{feathures[random.randint(0,4)]['bin']}"} for i in range(10)]
# for i in indivs:
#     print(i)
indivs = [
    {'feath': '01011101'},
    {'feath': '01010111'},
    {'feath': '01111101'},
    {'feath': '11010001'},
    {'feath': '11001100'},
    {'feath': '00011101'},
    {'feath': '01010001'},
    {'feath': '11010111'},
    {'feath': '01110001'},
    {'feath': '11010001'}
]
for i in indivs:
    i['weight'] = i["feath"].count("1")/8
print('start_population')
for i in indivs:
    print(i)

feaths = [i['weight'] for i in indivs]
avg = sum(feaths)/len(feaths)
print(f'avg = {avg}')

pairs = []
for item in range(0, 8, 2):
    pairs.append((select_rand(indivs)[0],select_rand(indivs)[0]))

# pairs = [(7, 9), (4, 9), (5, 8), (4, 6)]



breeded_d = []
for i in pairs:
    breeded_d.append(breed(first=indivs[i[0]]['feath'], second= indivs[i[1]]['feath']))

print("\nbreeded")
print(breeded_d)

breeded_m = []
for i in breeded_d:
    breeded_m.append(i[0])
    breeded_m.append(i[1])


mutated = []
for i in breeded_m:
    mutated.append({"feath": mutate(i), "weight": mutate(i).count("1")/8})

print('\nmutated')
for i in mutated:
    print(i)

feaths_evolved = [i['weight'] for i in mutated]
avg_evolved = sum(feaths_evolved)/len(feaths_evolved)
print(f'avg_evolved = {avg}')

