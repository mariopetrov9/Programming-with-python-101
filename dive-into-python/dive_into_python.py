import copy


def is_number_balanced(n):
    n = str(n)
    leftSide = ""
    rightSide = ""
    leftSide = n[0: len(n) // 2]
    rightSide = n[len(n) // 2 + len(n) % 2: len(n)]
    leftSide, rightSide = list(leftSide), list(rightSide)
    leftSide, rightSide = map(int, leftSide), map(int, rightSide)
    return sum(leftSide) == sum(rightSide)


def is_increasing(seq):
    for i in range(1, len(seq)):
        if seq[i] <= seq[i - 1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(1, len(seq)):
        if seq[i] >= seq[i - 1]:
            return False
    return True


def palindrome(obj):
    obj = str(obj)
    return obj == obj[::-1]


def get_largest_palindrome(n):
    n -= 1
    while n:
        if palindrome(n):
            break
        n -= 1

    return n


def prime_numbers(n):
    all_numbers = [x for x in range(2, n + 1)]
    for i in range(2, n + 1):
        not_prime = [x for x in range(i * 2, n + 1, i)]
        all_numbers = set(all_numbers) - set(not_prime)
    return sorted(list(all_numbers))


def char_histogram(string):
    histogram = {}
    for char in string:
        if char not in histogram:
            histogram[char] = 1
        else:
            histogram[char] += 1
    return histogram


def is_anagram(a, b):
    a, b = a.lower(), b.lower()
    anagram = {}
    if(len(a) != len(b)):
        return False
    else:
        a += b
        anagram = char_histogram(a)
        for key in anagram:
            if anagram[key] % 2:
                return False
        return True


def birthday_ranges(birthdays, ranges):
    result = []

    for rang in ranges:
        counter = 0

        for day in birthdays:
            if day in range(rang[0], rang[1] + 1):
                counter += 1

        result.append(counter)

    return result


def sum_matrix(m):
    rows = len(m)
    cols = len(m[0])
    s = 0
    for i in range(0, rows):
        for j in range(0, cols):
            s += m[i][j]
    return s


def is_transversal(transversal, family):

    for group in family:

        it = [x for x in group if x in transversal]

        if len(it) == 0 or len(it) > 1:
            return False

    return True


NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True


def bomb(m, at):
    if not within_bounds(m, at):
        return m

    target_value = m[at[0]][at[1]]
    dx, dy = 0, 1

    for position in NEIGHBORS:
        position = (at[dx] + position[dx], at[dy] + position[dy])

        if within_bounds(m, position):
            position_value = m[position[dx]][position[dy]]
            m[position[dx]][position[dy]] -= min(target_value, position_value)
    return m


def matrix_bombing_plan(m):
    result = {}

    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            bombed = bomb(copy.deepcopy(m), (i, j))
            result[(i, j)] = sum_matrix(bombed)

    return result
