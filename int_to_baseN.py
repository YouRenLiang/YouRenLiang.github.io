#int_to_baseN
def int_to_baseN(num, base_chars):
    base = len(base_chars)
    if num == 0:
        return base_chars[0]
    s = ""
    while num > 0:
        s = base_chars[num % base] + s
        num //= base
    return s

