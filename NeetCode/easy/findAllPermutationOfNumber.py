#solution using recursion

def permute( arr):
    result = []
    if len(arr) == 1:
        return [arr.copy()]

    for i in range(len(arr)):
        n = arr.pop[0]
        