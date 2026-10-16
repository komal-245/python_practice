def first_item(arr):
    return arr[0]

def first_max(arr):
    best= arr[0]
    for x in arr:
        if x>best:
            best=x
    return best

def has_pain_sum(arr,target):
    for x in arr:
        for y in arr:
            if x+y==target:
                return True
    return False
print("---Testing Big 0---")
print("first_item:")
print(first_item([2,4,6,8,10]))
print("first_max:")
print(first_max([1,5,9,17,667,8]))
print("has_pain_sum:")
print(has_pain_sum([1,2,3,4,5],9))