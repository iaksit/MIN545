def say(s):
    print(s)

yell = say

def double_and_say(s):
    print(s*2)

yell("HELLO")

def do_to_list(l, f):
    for i in l:
        f(i)

def make_incrementor(n):
    return lambda x: x + n

def print_and_return(s):
    print("I print: {0}".format(s))
    return s

todo = [round, abs, make_incrementor(2),
        print_and_return]
value = -3.14
for f in todo:
    value = f(value)

def even_numbers(upto=-1):
    n = 0
    while True:
        if upto != -1:
            if n >= upto:
                break
        n += 2
        yield n
        
en = even_numbers()
for i in en:
    print(i)
    if (i > 100):
        break