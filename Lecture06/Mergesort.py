def merge(result,p,q,r):
    a_top = 0
    b_top = 0
    sorted_a = result[p:q]
    sorted_b = result[q:r]
    for i in range(p,r):
        if a_top == len(sorted_a):
            result[i] = sorted_b[b_top]
            b_top += 1
            continue
        if b_top == len(sorted_b):
            result[i] = sorted_a[a_top]
            a_top += 1
            continue
        if sorted_a[a_top] >= sorted_b[b_top]:
            result[i] = sorted_b[b_top]
            b_top += 1
        else:
            result[i] = sorted_a[a_top]
            a_top += 1

def mergesort(input,p,r):
    if (r-p) > 1:
        q = (r + p) // 2
        mergesort(input,p,q)
        mergesort(input,q,r)
        merge(input,p,q,r)


# test:

x = [random.randint(1,100) for i in range(100)]
print("Original: ", x)
mergesort(x,0,len(x))
print("Sorted: ", x)
