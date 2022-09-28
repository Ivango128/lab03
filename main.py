def bubble(array):
    N = len(array)
    for i in range(N-1):
        for j in range(N-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff
    return array

array = input("Введите числа через пробел\n")
array = array.split(" ")
print(array)
print(bubble(array))