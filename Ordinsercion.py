def Ordinsercion (arr):
    for act in range(1, len(arr)):
        sig=act
        while sig >0 and arr[sig-1]>arr[sig]:
            arr[sig], arr[sig-1]=arr[sig-1],arr[sig]
            sig=sig-1
    return arr

num = [7,2,4,6,1,9,3]        
print("ORDENAMIENTO POR INSERCION") 
print("Lista: ", num)
Ordinsercion(num)
print("Lista Ordenada:",num)  