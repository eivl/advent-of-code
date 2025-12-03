from collections import deque
from itertools import groupby, tee, islice
from operator import itemgetter


test_input = """\
987654321111111
811111111111119
234234234234278
818181911112111"""

with open("day3_input") as file:
    day3_input = file.read().splitlines()

# day3_input = test_input.splitlines()


def unique_justseen(iterable, key=None):
    "Yield unique elements, preserving order. Remember only the element just seen."
    if key is None:
        return map(itemgetter(0), groupby(iterable))
    return map(next, map(itemgetter(1), groupby(iterable, key)))


def lookahead(tee_iterator):
    "Return the next value without moving the input forward"
    [forked_iterator] = tee(tee_iterator, 1)
    return next(forked_iterator)


def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def largest(block, length=12):
    if length == 1:
        return max(block)
    candidate = max(["".join(number) for number in sliding_window(block, length)])
    next_block = block[block.find(candidate[0]) :][1:]
    return candidate[0] + largest(next_block, length=length - 1)


iterator = iter("987654321")
[iterator] = tee(iterator, 1)

# wht was i thinking.. jeeses christ eivl


result = []
part2 = []
for block in day3_input:
    max_a = max(block[:-1])
    max_a_index = block.index(max_a)
    max_b = max(block[max_a_index + 1 :])
    result.append(int(max_a + max_b))
    part2.append(int(largest(block)))

print(sum(result))
print(sum(part2))
