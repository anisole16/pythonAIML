from functools import reduce

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

lst = list(map(int, input("Enter numbers: ").split()))

f = list(filter(prime, lst))
print("List after filter =", f)

m = list(map(lambda x: x * 2, f))
print("List after map =", m)

r = reduce(lambda x, y: x if x > y else y, m)
print("Output of reduce =", r)