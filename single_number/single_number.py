'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):

    # initialize single list with first element of arr
    single = [arr[0]]

    # iterate through rest of arr
    for i in range(1, len(arr)):
        # if `single` contains num
        if arr[i] in single:
            # remove item  from `single`
            single.remove(arr[i])
        else:
            # else add num
            single.append(arr[i])

    # at the end of iteration what is left is the single number
    return single[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
