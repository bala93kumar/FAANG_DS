

arr = [10,4,5,2,6,7,11,3]


max_value = arr[0]
sec_max_value = arr[0]

# use less solution provided by unify interviewer
def  second_max(arr):
  for i in range(len(arr)):
    if arr[i] > max_value:
      sec_max_value = max_value
      max_value  = arr[i]
    elif sec_max_value < arr[i]:
        sec_max_value = arr[i]