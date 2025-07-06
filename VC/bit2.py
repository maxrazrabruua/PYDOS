def intToBytes2(x: int) -> bytes:
    a = [0, 0]
    i = x
    while i > 0:
        if a[1] == 255:
            a[1] = 0
            a[0] += 1
        else:
            a[1] += 1
        i -= 1
    return bytes(a)

def bytes2toint(x: bytes) -> int:
    l = list(x)
    return (l[0] * 256) + l[1]