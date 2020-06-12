'''
Input: a List of integers
Returns: a List of integers
'''



# for each number in array
# create a dict entry with key is the index of that number
# and the value is the product of all the other numbers

# return the values into a list
# list(my_dict.values())

# input: [1, 7, 3, 4]
# output: [84, 12, 28, 21]



def multiply(nums, skip_index):
    total = 1

    for i in range(len(nums)):
        if i == skip_index:
            total *= 1
            # nums.next() # doesn't work, how to do that?
        else:
            total *= nums[i]

    return total
    

def product_of_all_other_numbers(arr):

    products = {}

    for i in range(len(arr)):
        products[i] = multiply(arr, i)

    return list(products.values())




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]

    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    # print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

    arr = [1, 7, 3, 4]
    print(product_of_all_other_numbers(arr))
