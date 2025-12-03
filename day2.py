from itertools import zip_longest


test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

with open("day2_input") as file:
    day2_input = file.read().strip()

# day2_input = test_input


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    iterators = [iter(iterable)] * n
    match incomplete:
        case "fill":
            return zip_longest(*iterators, fillvalue=fillvalue)
        case "strict":
            return zip(*iterators, strict=True)
        case "ignore":
            return zip(*iterators)
        case _:
            raise ValueError("Expected fill, strict, or ignore")


result = []

for rangeinput in day2_input.split(","):
    a, b = rangeinput.split("-")
    numbers = range(int(a), int(b) + 1)
    for number in numbers:
        if len(str(number)) % 2 == 1:
            continue
        num1, num2 = grouper(str(number), len(str(number)) // 2)
        if num1 == num2:
            result.append(number)
print(sum(result))


result = []
for rangeinput in day2_input.split(","):
    a, b = rangeinput.split("-")
    numbers = range(int(a), int(b) + 1)
    for number in numbers:
        for group_number in range(len(str(number)) // 2 + 1):
            group = list(grouper(str(number), group_number))
            if len(set(group)) == 1:
                result.append(number)
                break

print(sum(result))
