from model import attract
from data import data as goods
import json

sum = 0

for good in goods:
    good['Attract'] = attract(good)

goods = sorted(goods, key=lambda k: k['Attract'], reverse=True) 

byDep = {}

for good in goods :
    good_dep = good['Department']
    if good_dep not in byDep :
        byDep[good_dep] = {}
        byDep[good_dep]['list'] = []
        byDep[good_dep]['TotalAttraction'] = 0
    byDep[good_dep]['list'].append(good)
    byDep[good_dep]['TotalAttraction'] += good['Attract']

    good.pop('Department')

for dep in byDep :

    dict_cat = {}
    for good in byDep[dep]['list'] :
        good_cat = good['Category']
        if good_cat not in dict_cat :
            dict_cat[good_cat] = {}
            dict_cat[good_cat]['list'] = []
            dict_cat[good_cat]['TotalAttraction'] = 0
        dict_cat[good_cat]['list'].append(good)
        dict_cat[good_cat]['TotalAttraction'] += good['Attract']

        good.pop('Category')

    byDep[dep]['Category'] = dict_cat
    byDep[dep].pop('list')


    for cat in dict_cat : 
        dict_typ = {}

        for good in dict_cat[cat]['list'] :
    
            good_typ = good['Product Type']
            if good_typ not in  dict_typ :
                dict_typ[good_typ] = {}
                dict_typ[good_typ]['list'] = []
                dict_typ[good_typ]['TotalAttraction'] = 0
            dict_typ[good_typ]['list'].append(good)

            dict_typ[good_typ]['TotalAttraction'] += good['Attract']

            good.pop('Product Type')

        dict_cat[cat]['Type'] = dict_typ
        dict_cat[cat].pop('list')

# print(json.dumps(byDep, sort_keys=True, indent=4))

# def printgood (good) :
#     print(good['Product'])
#     print(good['Attract'])
#     print(good['Quantity'])
#     print(good['Regular Price'])


for d in byDep : 
    print(' ')
    print(d)
    for c in byDep[d]['Category'] :
        for t in byDep[d]['Category'][c]['Type'] :
            l = byDep[d]['Category'][c]['Type'][t]['list']
            print(l[0]['Product'])
            break 
