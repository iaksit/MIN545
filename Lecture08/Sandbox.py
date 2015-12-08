


f = open('MyText.txt','r')

i= 1
for line in f:
    print("Line {0}: ".format(i), line.strip())
    i += 1

f.close()

f = open('Output.txt','w')

f.write("Hello this is my first file!\n")
f.write("The first 10 even numbers are:\n")

for i in range(0,19,2):
    f.write(str(i) + "\n")

f.close()

y=7

def foo(x):
    print(y)

foo(6)


