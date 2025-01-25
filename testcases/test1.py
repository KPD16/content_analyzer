def two_sum(nums, target):
    """
    Finds two numbers in the list `nums` that add up to the `target`.
    Returns their indices.

    :param nums: List of integers
    :param target: Target sum
    :return: List of two indices
    """
    # Dictionary to store numbers and their indices
    num_map = {}  
    for i, num in enumerate(nums):
        complement = target - num  # Find the complement
        if complement in num_map:  # Check if complement exists in the dictionary
            return [num_map[complement], i]  # Return the indices
        num_map[num] = i  # Store the current number and its index
    return []  # Return empty list if no solution is found

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
