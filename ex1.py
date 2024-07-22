def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    while count < n:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

n_terms = int(input("How many terms? "))
fibonacci(n_terms)
