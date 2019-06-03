# 1) Analyze each line in isolation
# 2) Multiply any lines that occur in a loop
# 3) Add any lines that occur in sequence.


def foo(n):
    for i in range(n):
        print(i)


# foo(1)  # 1 sec
# foo(10)  # 10 seconds
# foo(100)  # 100 seconds


def foo(n):
    for i in range(n**2):
        print(i)


# foo(1)  # 1 sec
# foo(10)  # 100 seconds
# foo(100)  # 10000 seconds


def foo(n):
    sq_root = int(math.sqrt(n))  # O(1)
    for i in range(0, sq_root):  # O(sqrt n)
        print(i)  # O(1)


#   O(1) + O(sqrt n)

#   O(sqrt n)

def frotz(n):
    s = 0  # O(1)

    for i in range(n):  # O(n)
        for j in range(2*n):  # O(2*n)
            s += i*j  # O(1)

    return s  # O(1)


# 1 + ((n * (2 * n))*1)
# 1 + 2 * n * n * 1
# 1 + 2 * n ^ 2
# 2 * n ^ 2

# O(2 * n ^ 2)
# O(n ^ 2)
