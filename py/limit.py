def get_indices_of_item_weights(arr, limit):
    result = []

    l = len(arr) - 1
    for i in range(0, l):
        num = limit - arr[i]

        if num in arr:
            result.append(arr.index(num, i+1))
            result.append(arr.index(arr[i]))
            break

    return result

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 21))
print(get_indices_of_item_weights([4,4], 8))
print(get_indices_of_item_weights([4,4,1], 5))


# function getIndicesOfItemWeights(arr, limit):
#     m  = new Map()

#     for index from 0 to arr.length - 1:
#         w = arr[index]
#         complementIndex = m.findKey(limit - w)
#         if (complementIndex != null):
#             return [index, complementIndex]
#         else:
#             m.insert(w, index)

#     return null