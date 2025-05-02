def Ordburbuja (arr):
    n = len(arr)
    for act in range(n):
        for sig in range(0, n - 1 - act):
            if arr[sig] > arr[sig + 1]: 
                arr[sig], arr[sig + 1] = arr[sig + 1], arr[sig] 
    return arr
    
num = [9,4,5,2,7,3,1]
print("ORDENAMIENTO POR BURBUJA") 
print("Lista: ", num)
Ordburbuja(num)
print("Lista Ordenada:",num)            
            