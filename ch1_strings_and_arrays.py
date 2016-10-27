def is_unique_1_1(string):
    """
    Return whether or not there's a duplicate in the string.
    """

    string_chars = [False, ] * 248
    for char in string:
        if string_chars[ord(char)]:
            return False
        string_chars[ord(char)] = True
    return True


def is_unique_bit_array_1_1(string):
    """
    Return whether or not there's a duplicate in the string.
    """

    # Since python's long uses at most 32 bits, for the purpose of this
    # exercise, let's assume we only have sequential alphabets a-z, all
    # in lower case.
    bit_array = 0
    max_num_bits = 32
    for char in string:
        if bit_array & (1 << ord(char) % max_num_bits) != 0:
            return False
        bit_array |= 1 << ord(char) % max_num_bits
    return True


def is_permutation_1_2(string1, string2):
    """
    Return whether or not one string is a permutation of another's substring..
    """

    if string1 > string2:
        string1, string2 = string2, string1

    string1_char_counters = [0, ] * 248
    for char in string1:
        string1_char_counters[ord(char)] += 1
    hashed_string1_char_counters = hash(tuple(string1_char_counters))
    for i in range(len(string2) - len(string1) + 1):
        string2_char_counters = [0, ] * 248
        for j in range(i, i + len(string1)):
            string2_char_counters[ord(string2[j])] += 1
        hashed_string2_char_counters = hash(tuple(string2_char_counters))
        if hashed_string2_char_counters == hashed_string1_char_counters:
            return True
    return False


def URLify_1_3(url):
    """
    Replace encode url by replacing " " with "%20", optimal way.
    """

    # python's syntatic sugar for doing quick append for lists
    string_lst = [char if char != " " else "%%20" for char in url]
    return "".join(string_lst)


def palindrome_permutation_1_4(string):
    """
    Return whether or not the permutation of the string is a palindrome.
    Hint: a palindrome has at most 1 char that occurs odd number of times.
    """

    # Since python's long uses at most 32 bits, for the purpose of this
    # exercise, let's assume we only have sequential alphabets a-z, all
    # in lower case(26 consecutive sequence).
    xord_prod = 0
    for char in string:
        xord_prod ^= ord(char)
    if xord_prod == 0:
        return True
    else:
        count = 0
        for char in string:
            if ord(char) == xord_prod:
                return True
    return False


def one_way_1_5(string1, string2):
    """
    Return whether or not the 2 strings can be the same by either deleting one char, inserting one char, or
    modifying exactly one char.
    """

    i = 0
    while i < len(string1) and i < len(string2) and string1[i] == string2[i]:
        i += 1
    if i == len(string1):
        return True
    elif (string1[i:] and string1[i + 1:] == string2[i:]) \
            or string1[i:] == string2[i + 1:] \
            or string1[i + 1:] == string2[i + 1:]:
        return True
    return False


def string_compression_1_6(string):
    """
    If a string can be can be compressed in length by replacing consecutive repeating chars with only the char
    and number of consecutive occurrences, then return the new string.
    i.e.
    abc3d3ada is a shorter representation of abcccdddada.
    """

    i = 0
    res = []
    while i < len(string):
        cur_char = string[i]
        j = i
        while j < len(string) and string[j] == cur_char:
            j += 1
        if j - i == 1:
            res.append(cur_char)
        else:
            res.extend([cur_char, str(j - i)])
        i = j
    if len(string) == len(res):
        return string
    return "".join(res)


def rotate_matrix_1_7(matrix):
    """
    Rotate a N x N matrix by 90 degrees.
    """
    def rotate_at_index(matrix, x, y, n):
        tmp = matrix[x][y]
        matrix[x][y] = matrix[n - y][x]
        matrix[n - y][x] = matrix[n - x][n - y]
        matrix[n - x][n - y] = matrix[y][n - x]
        matrix[y][n - x] = tmp

    n = len(matrix)
    for i in range(n / 2):
        for j in range(i, n - i - 1):
            rotate_at_index(matrix, i, j, n - 1)
    return matrix


def zero_matrix_1_8(matrix):
    """
     Mark all the rows and columns where 0's occur all 0's.
    """

    # for the purpose of this exercise, we only consider tables within size 32
    x_zeros = 0
    y_zeros = 0
    n = len(matrix)
    assert n <= 32
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                x_zeros |= 1 << i
                y_zeros |= 1 << j
    for i in range(n):
        if x_zeros & (1 << i) != 0:
            for j in range(n):
                matrix[i][j] = 0
        if y_zeros & (1 << i) != 0:
            for j in range(n):
                matrix[j][i] = 0
    return matrix


def string_rotation_1_9(string1, string2):
    """
    Check whether or not a string is rotated version of another
    """
    if len(string1) != len(string2):
        return False
    for i in range(len(string1)):
        if string1[:i] == string2[len(string2) - i:] and string1[i:] == string2[: len(string2) - i]:
            return True
    return False
