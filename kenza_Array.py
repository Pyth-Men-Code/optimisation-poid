import numpy as np
import matplotlib.pyplot as plt

tab = [
    {'1': [15, 4]},
    {'2': [20, 10]},
    {'3': [3, 5]},
    {'4': [3, 6]},
    {'5': [4, 2]},
    {'6': [9, 1]},
    {'7': [8, 200]},
    {'8': [8, 4]},
    {'9': [8, 4]},
    {'10': [8, 100]},
    {'11': [8, 4]},
    {'12': [8, 40]},
    {'13': [8, 4]},
    {'14': [8, 48]},
    {'15': [8, 4]},
    {'16': [8, 1000]},
    {'17': [8, 4]},
    {'18': [8, 4]},
    {'19': [100, 4]},
    {'20': [13, 4]},
    {'21': [8, 4]},
    {'21': [2, 4]},
    {'22': [22, 4]},
    {'23': [56, 4]}
]

def get_declaration(array):
    for element in array:
        valeur = list(element.values())[0]
        util = valeur[0] / valeur[1]
        element['p/u'] = util
    ranged_array = sorted(array, key=lambda d: d['p/u'], reverse=True)
    return ranged_array

def get_minorant(tableau, N):
    sac = []
    poid_total = 0
    nombre_object = 0
    tableau = sorted(tableau, key=lambda d: d['p/u'], reverse=True)
    while (poid_total < N):

     for element in tableau:
            poid_object = element[next(iter(element))][0]
            rapport = element[next(iter(element))][1]
            rapport_obj = element['p/u']
            if (poid_object > N ) :
                continue
            if poid_object + poid_total < N:
                sac.append((next(iter(element)), poid_object, rapport, rapport_obj))
                poid_total += poid_object
                poid_rest = N - poid_total

            if poid_total == N:
                break
     return f'le poid restant dans le sac est {poid_rest}',\
            sac ,\
            f"il y'a exactement :{len(sac)} objets dans le sac"

def get_majorant(tableau, N):
        sac = []
        poid_total = 0
        nombre_object = 0
        tableau = sorted(tableau, key=lambda d: d['p/u'], reverse=True)
        while (poid_total < N):

            for element in tableau:
                poid_object = element[next(iter(element))][0]
                rapport = element[next(iter(element))][1]
                rapport_obj = element['p/u']
                if (poid_object > N):
                    continue
                if poid_object + poid_total < N:
                    sac.append((next(iter(element)), poid_object, rapport, rapport_obj))
                    poid_total += poid_object
                    if poid_total < N:
                        poid_rest = N - poid_total
                        poid_objet_restant = poid_object - poid_rest
                        sac.append((next(iter(element)), poid_rest, rapport, rapport_obj))
                        poid_total += poid_rest
                        if poid_objet_restant % 100 == 0:
                            element[next(iter(element))][0] = poid_objet_restant
                        else:
                            return False

                    if poid_total == N:
                      break


            return f'le poid restant dans le sac est {poid_rest}', \
                   sac, \
                   f"il y'a exactement :{len(sac)} objets dans le sac"

ranged_array = get_declaration(tab)
print(ranged_array)

print(get_minorant(ranged_array, 50))
print(get_majorant(ranged_array, 150))
