from itertools import combinations
list=[2,-3,6,-7]
print("Positive numbers are")
for i in range(1,len(lst)+1):
    for combo in combinations (lst,i):
        if all(x>o for x in combo):
            print(combo)