#Approach 1: Assign every element with its previous element and first element with the last element 
def rotate(A, n):
    array_last_el = A[n-1]
    for i in range(n-1, 0, -1):
        A[i] = A[i-1]
    A[0] = array_last_el

#Approach 2: We can use two pointers, As we know in cyclic rotation we will bring last element to 
#first and shift rest in forward direction, we can do this by swapping every element with last element till we get to the last point.
def rotate2(A, n):
    i = 0
    j = n-1
    while i != j:
        A[i], A[j] = A[j], A[i]
        i += 1

A = [1, 2, 3, 4, 5]
n = len(A)
print("Original array: ", A)
rotate(A, n)
print("Rotated array: ", A)