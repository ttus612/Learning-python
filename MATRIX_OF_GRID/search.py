def search(arr, x):
    for i in range(0,3):
        for j in range(0,3):
            if(arr[i][j] == x):
                return 1
    return 

x = 99
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if(search(arr, x)):
    print("Yes")
else:   
    print("No")