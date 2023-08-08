def éprimo(k):
    if k == 2 or k == 3 or k == 5 or k == 7:
        return True
    elif k % 2 == 0 or k % 3 == 0 or k % 4 == 0 or k % 5 == 0 or k % 7 == 0:
        return False
    else:
        return True


def maior_primo(n):
    m = 1
    while m <= n:
        if éprimo(m):
            x = m
        m = m + 1
    return x

