def find_digits_sum_matches_to_target(array, target):
    result =[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array [j] == target:
                result.append((array[i], array[j]))
    return result

print(find_digits_sum_matches_to_target([1,2,3,4], 7))
