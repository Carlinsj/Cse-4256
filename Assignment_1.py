def maximum(li):
    max_val = float('-inf')
    for num in li:
        if num > max_val:
            max_val = num
    return max_val
def maximum_index(li):
    max_val = float('-inf')
    max_idx = -1           
    for idx in range(len(li)):
        if li[idx] > max_val:
            max_val = li[idx]
            max_idx = idx
    return max_idx
li=[1,2,3,5,4]
print(maximum(li))
print(maximum_index(li))
