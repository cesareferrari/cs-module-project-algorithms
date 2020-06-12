'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    result = []

    for i in range(len(arr)):
        if arr[i] == 0:
            result.append(arr[i]) 
        else:
            result.insert(0, arr[i])

    return result



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

    arr2 = [0, 0, 0, 0, 3, 2, 1] 
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr2)}")
