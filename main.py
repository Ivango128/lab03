def bubblevoz(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array

def bubblevub(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] < array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j] = buff
    return array


answer = int(input("Введите 1- По убыванию, 2 - по возврастанию.\n"))

array = input("Введите числа через пробел\n")
array = array.split(" ")
print(array)
if answer == 1:
    print(bubblevub(array))
else:
    print(bubblevoz(array))