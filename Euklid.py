"""
Program to find the greatest common divisor
"""
def gcd(u, v):
    u = int(u)
    v = int(v)
    count = 0
    while u > 0:
        count = count + 1
        if u < v:
            t = v
            v = u
            u = t
        u = u - v
    print(count)
    return v

def gcd2(u, v):
    u = int(u)
    v = int(v)
    count = 0
    while v > 0:
        count = count + 1
        h = u % v
        u = v
        v = h
    print(count)
    return u

x = input('x: ')
y = input('y: ')
print('x: ', x, 'y: ', y, 'gcd: ', gcd(x, y), gcd2(x, y))
