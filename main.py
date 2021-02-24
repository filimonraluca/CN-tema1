r = 0
m = 0
while r != 1:
    r = 1.0 + pow(10, -m)
    m += 1
# 1.0 + pow(10, -(m-1)) = 1.0
m -= 2
u = pow(10, -m)
print(1.0 + u)
print(u)

a = 1.0
b = c = u / 10
print((a + b) + c == a + (b + c), (a + b) + c, a + (b + c))

a = 1.0
m = 0
b = c = pow(10, m)
while (a * b) * c == a * (b * c):
    b = c = pow(10, m)
    m += 1
print(a, b, c)
print('%.25f %.25f' % ((a * b) * c, a * (b * c)))
