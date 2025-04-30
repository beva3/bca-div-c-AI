# in this file i just write the algorithm,

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def revers_string(s):
    return s[::-1]

# main
if __name__ == "__main__":
    print(revers_string("hello world"))