def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n - 1)

def fact_iter(n):
    ret = 1
    while n != 0:
        ret *= n
        n -= 1
    return ret

def fib_rec(n):
    if n in (0, 1):
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    stack = [n]
    ret = 0
    while stack:
        n = stack.pop()
        if n in (0, 1):
            ret += 1
            continue
        stack.append(n-1)
        stack.append(n-2)
    return ret

print(fact_rec(5), fact_iter(5))
print()
for i in range(10):
    print(fib_rec(i), fib_iter(i))
