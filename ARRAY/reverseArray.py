def reverseArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

print("Đảo ngược mảng (Reverse Array) không sử dụng hàm đệ quy")
A = [12, 2, 4, 112, 213,42]
print("Mảng A:", A)
reverseArray(A, 0, 5)
print("Mảng A sau khi đảo ngược:", A)

print("--------------------------------------------------")

print("Đảo ngược mảng (Reverse Array) sử dụng hàm đệ quy")
def reverseArrayRecursive(A, start, end):
    if start >= end:
        return;
    A[start], A[end] = A[end], A[start]
    reverseArrayRecursive(A, start + 1, end - 1)