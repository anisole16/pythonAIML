import threading

sum_result = 0
product_result = 1

def find_sum(lst):
    global sum_result
    sum_result = sum(lst)

def find_product(lst):
    global product_result
    for i in lst:
        product_result *= i

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

t1 = threading.Thread(target=find_sum, args=(lst,))
t2 = threading.Thread(target=find_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum =", sum_result)
print("Product =", product_result)