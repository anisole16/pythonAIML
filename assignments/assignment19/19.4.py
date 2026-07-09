# filter even number, square using map, return addition 


from functools import reduce

n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    num = int(input("Enter elements: "))
    lst.append(num)

f = list(filter(lambda x: x % 2 == 0, lst))
print("List after filter", f)

m = list(map(lambda x: x ** 2, f))
print("list after appensd: ",m)

r = reduce(lambda x, y: x+y, m)
print("Output of reduce :",r)



