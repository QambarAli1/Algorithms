list=[18,22,14,17,26,50,30,40]
def quickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivotElement = list.pop()
    graterNums = []
    smallerNums = []
    for nums in list:
        if nums > pivotElement:
            graterNums.append(nums)
        else:
            smallerNums.append(nums)
    return quickSort(smallerNums) + [pivotElement] + quickSort(graterNums)
print(quickSort(list))