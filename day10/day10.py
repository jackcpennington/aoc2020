from collections import defaultdict

with open("day10/input.txt") as file:
    adapters = [int(line) for line in file.read().split('\n')]


def part_1(adapters):
    adapters.sort()
    adapters = [0] + adapters + [adapters[-1] + 3]
    adapter_gaps = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]
    gap_counts = dict((x,adapter_gaps.count(x)) for x in set(adapter_gaps))
    return (gap_counts[1] * gap_counts[3])

def part_2(adapters):
    def memoize(func):
        cache = dict()
        def memoized_func(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result
        return memoized_func

    @memoize
    def count_paths(i, j):
        if i == j:
            return 1
        else:
            result = sum(count_paths(c, j) for c in possible_next_adapters[i])
            return result
    
    adapters.sort()
    adapters = [0] + adapters + [adapters[-1] + 3]

    possible_next_adapters = dict()
    for i in range(len(adapters)):
        possible_next_adapters[adapters[i]] = [a for a in adapters[i+1:i+4] if a <= adapters[i] + 3]

    return count_paths(adapters[0], adapters[-1])

print ("Part 1: " + str(part_1(adapters)))
print ("Part 2: " + str(part_2(adapters)))
