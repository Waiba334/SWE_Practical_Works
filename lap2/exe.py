#fibonacci_list
def fibonacci_list(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

print(fibonacci_list(10)) 

#index_of_first_fib_exceeding
def index_of_first_fib_exceeding(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

print(index_of_first_fib_exceeding(10))

#is_fibonacci
def is_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

print(is_fibonacci(8)) 
print(is_fibonacci(10))  

#fibonacci_ratios
def fibonacci_ratios(n):
    ratios = []
    a, b = 0, 1
    for _ in range(n):
        if a != 0:  # Prevent division by zero
            ratios.append(b / a)
        a, b = b, a + b
    return ratios

# Example usage:
print(fibonacci_ratios(10))