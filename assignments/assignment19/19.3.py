# program of filter() map() reduce() filter number 70- 90 add 10 using map and reduce using reduce fun

from functools import reduce
n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    num = int(input("Enter elements:"))
    lst.append(num)
print("input list: ",lst)    



f = list(filter(lambda x: x >= 70 and x <= 90,lst))
print("List after filter= ",f)


m = list(map(lambda x: x + 10,f))

print("List after map= ",m)

r = reduce(lambda x,y: x*y,m)
print("Output of reduce :",r)