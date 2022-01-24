from itertools import permutations


def largest(l):
    list1 = []
    for i in permutations(l, len(l)):
        list1.append("".join(map(str, i)))
    return max(list1)


print(largest([54, 60, 8, 44, 5]))
