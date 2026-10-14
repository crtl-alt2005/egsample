numbers=[35,12,58,21,46,7]
minimum=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]<minimum:
        minimum=numbers[i]
print("Minimum",minimum)