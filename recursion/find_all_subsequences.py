


arr = [1,2,3]
result = []
def find_all_subsequences(arr, index, res):
      
    if index >= len(arr):
      result.append(res[:])
      return

    # Take
    res.append(arr[index])
    find_all_subsequences(arr, index + 1, res)
    res.pop()
    # Not Take
    find_all_subsequences(arr, index + 1, res)
    # res.pop()

res = []
find_all_subsequences(arr, 0, res)
print(result)
print(len(result))