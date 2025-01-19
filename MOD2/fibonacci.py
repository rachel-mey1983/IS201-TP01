######## 2)	Write a program that asks the user how many Fibonacci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions.

# The Fibonacci Sequence is the series of numbers:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The next number is found by adding up the two numbers before it.

# •	Fibonacci(0) is 0, Fibonacci(1) is 1
# •	The 2 is found by adding the two numbers before it (1+1)
# •	The 3 is found by adding the two numbers before it (1+2),
# •	And the 5 is (2+3),
# •	and so on!
# Input
# >>> What position of Fibonacci number you want to see?
# >>> 5
# Output
# >>> 3

########
# Input	

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

num = int(input("How many Fibonacci numbers to generate? "))
print(fibonacci(num))


# Output
