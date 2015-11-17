def foo(n):
    return n + some_fun(n)


def fib(n):  # iff we are guaranteed that
             # n is a nat. number
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def n_binary(n, accumulated=""):
    ## base case
    if n == 0:
        return [accumulated]
    else:
         ## Recursion
        return (n_binary(n-1 , "0" + accumulated ) +
                n_binary(n-1 , "1" + accumulated ))

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0:1]

    
def n_binary_alt(n):
    if n == 1:
        return ['0','1']
    elif n == 0:
        return []
    else:
        temp = n_bin_alt(n-1)
        result = []
        for s in temp:
            result += [s+'1']
            result += [s+'0']
        return result

def password_gen(n):
    if n == 1:
        return ['a','b','c','d','e','f','g']
    elif n == 0:
        return []
    else:
        temp = password_gen(n-1)
        result = []
        for s in temp:
            for l in  ['a','b','c','d','e','f','g']:
                result += [s+l]
        return result


def binary_search(data, target, low, high):
    # base case #1
    if low > high:
        return False
    mid = (low + high) // 2
    # base case #2
    if data[mid] == target:
        return mid
    # Recursion
    if data[mid] > target:
        # if mid is after target, use first half
        return binary_search(data,target, low=low, high=mid-1)
    else:
        # otherwise, use second half
        return binary_search(data,target, low=mid+1, high=high)







    
