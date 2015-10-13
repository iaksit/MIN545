# Our first sandbox

# The following counts as a comment
'''x = 0
# a_flag = True

if x is 1:
    if a_flag:
        print('something')
        y = 4
    else:
        print('something else')
        y = 0'''

total = 0
x = None
while x != 0:
    x = int(input("Enter a number"))
    total += x
print('Total: {0}'.format(total))

mylist = [1.1, 2.3, 5, 4.2, 8, -1.3, 2]
minimum = float('inf')
for fred in mylist:
    if fred < minimum:
        minimum = fred
print('Minimum: {0}'.format(minimum))

def hello(name, times):
    print('hello {0} '.format(name) * times)
    return times

def contains(data, target):
    for item in data:
        if item == target:
            return True
    return False
