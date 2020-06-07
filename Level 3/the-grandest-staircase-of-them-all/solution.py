def solution(n):

    staircase_ways = [[0 for i in range(n + 2)] for i in range(n + 2)]
    return staircase_combinations_generator(1, n, staircase_ways) - 1

def staircase_combinations_generator(higher, lower, staircase_ways):
    if staircase_ways[higher][lower] != 0:
        return staircase_ways[higher][lower]
    if lower == 0:
        return 1
    if lower < higher:
        return 0
    staircase_ways[higher][lower] = staircase_combinations_generator(higher + 1, lower, staircase_ways) + staircase_combinations_generator(higher + 1, lower - higher, staircase_ways)
    return staircase_ways[higher][lower]