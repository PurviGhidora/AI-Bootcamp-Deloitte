def fib(n):
    n1, n2 = 0, 1
    cnt = 0
    while cnt < n:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        cnt += 1

n_terms = int(input("How many terms? "))
fib(n_terms)
