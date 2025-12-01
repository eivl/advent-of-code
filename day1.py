from itertools import accumulate, zip_longest, pairwise


def add_mod(a, b, m=100):
    return (a + b) % m


with open("day1_input") as file:
    result = file.read().replace("L", "-").replace("R", "").splitlines()

numbers = [int(number) for number in result]
result = list(accumulate(numbers, func=add_mod, initial=50))

print(result.count(0))


def calculate(start, direction, end):
    d = 1 if direction > 0 else 0
    if d:
        # rotate right
        c = 1 if start > end else 0
        return (direction // 100) + c
    else:
        # rotate left
        c = 1 if start < end else 0
        return (abs(direction) // 100) + c


pairs = [(a, b) for a, b in zip_longest(result, numbers)]
print(
    sum(
        calculate(start, direction, end)
        for (start, direction), (end, _) in pairwise(pairs)
    )
)
