def rearrange(A, n):
    for i in range(n):
        for j in range(n):
          if(A[j] == i):
            A[j], A[i] = A[i], A[j]

    for i in range(n):
        if(A[i] != i):
            A[i] = -1


arr = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
arr2 = [0,5,7,1]
n = len(arr)
n2 = len(arr2)
print("Original array: ", arr)
rearrange(arr, n)
print("Rearranged array: ", arr)