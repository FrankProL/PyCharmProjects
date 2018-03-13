# encoding: utf-8
simpDat = [['r', 'z', 'h', 'j', 'p'],
           ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
           ['z'],
           ['r', 'x', 'n', 'o', 's'],
           ['y', 'r', 'x', 'z', 'q', 't', 'p'],
           ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]

from fp_growth import find_frequent_itemsets
for itemset in find_frequent_itemsets(simpDat, 3):
    print itemset

for i in range(5):
	print i
for i in range(1,5):
	print i
