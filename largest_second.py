def largest_and_second(arr):
    if len(arr)<2:
        return "Array must have a least two elements"
    largest=float('-inf')
    second_largest= float('-inf')
    for num in arr:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num!=largest:
            second_largest=num
    return largest, second_largest
print("---Testing largest_and_second---")
print(largest_and_second([10,5,20,100,600,200,40]))