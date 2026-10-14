#Q1

numbers=[35,12,58,21,46,7]
minimum=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]<minimum:
        minimum=numbers[i]
print("Minimum",minimum)

#Q2
for i in range(len(numbers)):
    min_index=i
    for j  in range(i+1,len(numbers)):
        if numbers[j]<numbers[min_index]:
            min_index=j
    numbers[i],numbers[min_index]=numbers[min_index],numbers[i]
print("Sorted array:",numbers)

#Q3

for i in range(len(numbers)):
    max_index=i
    for j  in range(i+1,len(numbers)):
        if numbers[j]>numbers[max_index]:
            max_index=j
    numbers[i],numbers[max_index]=numbers[max_index],numbers[i]
print("Sorted array:",numbers)
