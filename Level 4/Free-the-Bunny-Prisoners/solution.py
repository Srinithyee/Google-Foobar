from itertools import combinations

def solution(num_buns, num_required):
    key_distribution = [[] for num in range(num_buns)]
    available_copy_each_key = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), available_copy_each_key)):
        for bunny in bunnies:
            key_distribution[bunny].append(key)

    return key_distribution