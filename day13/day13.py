with open("day13/input.txt") as file:
    target = int(file.readline().rsplit()[0])
    times = set([int(x) for x in file.read().split(',') if x != 'x'])

print(target)
print (times)


current_time = target

def get_factors(n):
    factors = set()
    for i in range(1, n + 1):
       if n % i == 0:
           factors.add(i)
    return factors

while True:
    factors = get_factors(current_time)
    time_factors = times.intersection(factors)
    if time_factors != set():
        (time,) = time_factors
        break
    current_time += 1

print (time, current_time)

print((current_time - target) * time)