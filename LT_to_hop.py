def c(arr, k, curr = [], start = 0):
    if k == 0:
        print(curr)
        return
    for i in range(start, len(arr)):
        curr.append(arr[i])
        c(arr, k-1, curr, i+1)
        curr.pop()
    
a = [i for i in range(5)]

c(a, 2)