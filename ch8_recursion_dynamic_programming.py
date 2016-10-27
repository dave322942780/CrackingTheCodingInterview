def triple_step(n):
    semanti_ary = [1, 2, 4]
    for i in range(3, n):
        semanti_ary.append(semanti_ary[i - 3] + semanti_ary[i - 2] + semanti_ary[i - 1])
    return semanti_ary[n - 1]


def robot_in_grid(map, x=0, y=0):
    width = len(map[0])
    height = len(map)

    if x == width - 1 and y == height - 1:
        return [(x, y)]
    elif x < width and y < height and map[y][x] == 1:
        return None

    path = None if x >= width else robot_in_grid(map, x=x + 1, y=y)

    if path is None and y < height:
        path = robot_in_grid(map, x=x, y=y + 1)

    if path:
        path.insert(0, (x, y))
    return path


def magic_idx(ary):
    def _magic_idx(start, end):
        if start == end + 1:
            return start if ary[start] == start else None
        elif start == end:
            return None

        half_size = (end - start) / 2
        mid = start + half_size
        if ary[mid] == mid:
            return mid
        else:
            return _magic_idx(start, mid) if ary[mid] > mid else _magic_idx(mid, end)

    return _magic_idx(0, len(ary))


def power_set(input_set):
    if not input_set:
        return [{}]
    elem = input_set.pop()
    sets = power_set(input_set)
    i = len(sets) - 1
    while i >= 0:
        new_set = set(sets[i])
        new_set.add(elem)
        sets.append(new_set)
        i -= 1
    return sets


def recursive_multiply(n1, n2):
    def _recursive_multiply(num1, num2):
        if num1 == 0:
            return 0
        else:
            div_two = num1 >> 1  # divide by 2
            div_two_reminder = num2 if num1 & 1 == 1 else 0  # remainder
            div_two_res = _recursive_multiply(div_two, num2)
            return div_two_reminder + div_two_res + div_two_res

    return _recursive_multiply(n1, n2) if n1 < n2 else _recursive_multiply(n2, n1)


def towers_of_hanoi(n):
    moves = []

    def _towers_of_hanoi(from_tower, to_tower, n):
        if n == 1:
            moves.append((1, from_tower, to_tower))
        else:
            [other_tower] = [i for i in [1, 2, 3] if i != from_tower and i != to_tower]
            _towers_of_hanoi(from_tower, other_tower, n - 1)
            moves.append((n, from_tower, to_tower))
            _towers_of_hanoi(other_tower, to_tower, n - 1)

    _towers_of_hanoi(1, 3, n)
    return moves


def permutation_without_dups(input_str):
    if not input_str:
        return [""]
    else:
        input_str, last_char = input_str[:-1], input_str[-1]
        permutations = permutation_without_dups(input_str)
        i = len(permutations) - 1
        length = len(input_str)
        while i >= 0:
            permutation = permutations.pop(i)
            for j in range(length + 1):
                permutations.append(permutation[:j] + last_char + permutation[j:])
            i -= 1
        return permutations


def permutation_without_dups_2(input_str):
    if not input_str:
        return [""]
    else:
        res = []
        for i in range(len(input_str)):
            res.extend([input_str[i] + permutation for permutation in
                        permutation_without_dups_2(input_str[:i] + input_str[i + 1:])])
        return res


import copy


def permutation_with_dups(input_str):
    count = {}
    for i in input_str:
        count.setdefault(i, 0)
        count[i] += 1

    def _permutation_with_dups(count):
        res = []
        if not count:
            return [""]
        for char in count.keys():
            new_count = copy.deepcopy(count)
            new_count[char] -= 1
            if new_count[char] == 0:
                del new_count[char]
            res.extend(char + permutation for permutation in _permutation_with_dups(new_count))
        return res

    return _permutation_with_dups(count)


def permutation_with_dups_2(input_str):
    if not input_str:
        return [""]
    else:
        res = []
        used = set()
        for i in range(len(input_str)):
            if input_str[i] not in used:
                used.add(input_str[i])
                res.extend([input_str[i] + permutation
                            for permutation in permutation_with_dups_2(input_str[:i] + input_str[i + 1:])])
        return res


def parens(n):
    parens_lst = []
    parans_str = [""] * (n * 2)

    def _parens(pos, parens_left, parens_right):
        if parens_right == 0:
            parens_lst.append("".join(parans_str))

        else:
            if parens_left > 0:
                parans_str[pos] = "("
                _parens(pos + 1, parens_left - 1, parens_right)
            if parens_right > parens_left:
                parans_str[pos] = ")"
                _parens(pos + 1, parens_left, parens_right - 1)

    _parens(0, n, n)
    return parens_lst


def paint_fill(painting, x_coord, y_coord, color):
    if not painting or not painting[0]:
        return
    height = len(painting)
    width = len(painting[0])
    painting_copy = copy.deepcopy(painting)

    def _paint_fill(painting, x, y, old_color, new_color):
        if 0 <= x < width and 0 <= y < height and painting[y][x] == old_color:
            painting[y][x] = new_color
            _paint_fill(painting, x - 1, y, old_color, new_color)
            _paint_fill(painting, x + 1, y, old_color, new_color)
            _paint_fill(painting, x, y - 1, old_color, new_color)
            _paint_fill(painting, x, y + 1, old_color, new_color)

    _paint_fill(painting_copy, x_coord, y_coord, painting_copy[y_coord][x_coord], color)
    return painting_copy


def coin_exchange(amount):
    cache = [[] for i in range(amount + 1)]
    options = [25, 10, 5, 1]
    cache[0] = [[0] * len(options)]
    for i in range(1, amount + 1):
        for coin_idx, coin in enumerate(options):
            quantity = 1
            amount_left = i - quantity * coin
            while amount_left >= 0:
                for change in cache[amount_left]:
                    max_coin_idx = len(options) + 1
                    for j in range(len(change)):
                        if change[j] != 0:
                            max_coin_idx = j
                            break
                    if coin_idx < max_coin_idx:
                        new_change = copy.deepcopy(change)
                        new_change[coin_idx] = quantity
                        cache[i].append(new_change)
                quantity += 1
                amount_left = i - quantity * coin
    return [{options[i]: change[i] for i in range(len(change)) if change[i] != 0} for change in cache[amount]]


print coin_exchange(11)
