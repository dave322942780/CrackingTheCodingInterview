def insertion(orig, replace, start_idx, end_idx):
    mask = ((-1 << end_idx + 1) | (~(-1 << start_idx)))
    res = orig
    res &= mask
    res |= replace << start_idx
    return res


def binary_to_str(real):
    if real < 0 or real > 1:
        raise Exception("Invalid input")

    res = ["0."]
    remainder = 1
    for i in range(32):
        remainder /= 2.
        if remainder <= real:
            res.append("1")
            if remainder == real:
                return "".join(res)
            else:
                real -= remainder
        else:
            res.append("0")
    raise Exception("Unable to represent string with 32 digits")
