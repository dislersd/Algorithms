'''
What is an algorithm?
A set of instructions
A problem solving pattern

Polya's Problem Solving Technique

1) Understand the problem
2) Devise a plan
3) Carry out the plan, Implement
4) Analyze, Look back and refactor if possible
------------------------------------

Write a function that returns the factorial of a given integer

Understanding the problem
--------------------------

factorial 
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
0! = 1
n!, n must be non negative
n < 1000
4! == 4 * (4 - 1)!
4! == 4 * 4 * 3!

plan
----

recursive definition:

0! = 1
n! == n * (n-1)!

Add range checking 0...1000
Make sure it's an integer

'''

# Implement


def factorial(n):
    # TODO add range checking
    # TODO make sure it's an integer
    if n == 0:
        return 1

    return n * factorial(n - 1)


# print(factorial(5))


def factorial2(n):
    a = 1

    for i in range(n, 0, -1):
        a *= i

    return a

# print(factorial2(20000))


'''
Write algorithm to compute a^b

Analyze
-------

Recursive:
    O(n) time complexity
    O(n) space complexity

'''

"""
Power, exponents

Understand
----------

What is the range of input?
	a can range from 0 to inf
	b can range from 0 to inf
What about fractional or complex numbers?
	integer only
What about negative numbers?
	non-negative only
What about raising to the power of 0?
	n^0 == 1 for n > 0
	0^0 == 1, even though it's technically undefined
How much memory do we have?
	Enough

2^0 == 1
2^4 == 2 * 2 * 2 * 2
       |----2^4----|
	   2 * |--2^3--|

a^0 == 1
a^b == a * a^(b-1)

Plan
----

Analyze
-------
Iterative approach:

	O(n) time complexity
	O(1) space complexity

Recursive approach:
	O(n) time
	O(n) space


"""


# def power_recursive(a, b):
#     if b == 0:
#         return 1

#     return a * power_recursive(a, b - 1)


# def power_iter(a, b):
#     if b == 0:
#         return 1

#     x = 1

#     for i in range(b):  # O(b)
#         x *= a

#     return x


# print(power_recursive(10, 80))

'''
Fibonacci Sequence

Write a function that computes the nth Fibonacci number

Understand
----------

n = non negative integer.

0, 1, x will be sum of previous two numbers

0, 1, 1, 2, 3, 5, 8, 13, 21 and so on....

 1 + 1   2 + 3   5 + 8

f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2)
f(8) = f(7) + f(6)

Plan
----
def fib(n):
    if n == 0
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

for i in range(10):
    print(f'{i}: {fib(i)}')


Analyze
--------


'''

def fib(n):
    cache = {}

    def fib_inner(n): #O(2^n)
        nonlocal cache

        if n == 0:
            return 0
        if n == 1:
            return 1

        # if nth number in cache:
        #     return cache[n]
        if n not in cache:
            cache[n] = fib_inner(n-1) + fib_inner(n-2)

        return cache[n]

        # else its not in cache
        #     cache[n] = fib(n-1) + fib(n-2)

    return fib_inner(n)

for i in range(3000):
    print(f'{i}: {fib(i)}')
