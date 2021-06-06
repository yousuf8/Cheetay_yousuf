from itertools import permutations
def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        lst.append("".join(map(str,i)))
    return max(lst)
 
print(largest([54, 546, 548, 60])) 
print(largest[3, 30, 34, 5, 9]))

 
