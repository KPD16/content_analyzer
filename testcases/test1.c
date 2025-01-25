#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    /**
     * Finds two numbers in the array `nums` that add up to the `target`.
     * Returns their indices.
     *
     * @param nums Array of integers
     * @param numsSize Size of the array
     * @param target Target sum
     * @param returnSize Pointer to return the size of the result array
     * @return Array of two indices
     */
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            // Check if the sum matches the target
            if (nums[i] + nums[j] == target) { 
                int* result = (int*)malloc(2 * sizeof(int));
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                // Return the indices
                return result; 
            }
        }
    }
    // Return size as 0 if no solution is found
    *returnSize = 0; 
    return NULL;
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, 4, target, &returnSize);
    if (returnSize == 2) {
        printf("Indices: [%d, %d]\n", result[0], result[1]); // Output: [0, 1]
        free(result);
    } else {
        printf("No solution found.\n");
    }
    return 0;
}
