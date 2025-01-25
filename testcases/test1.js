/**
 * Finds two numbers in the array `nums` that add up to the `target`.
 * Returns their indices.
 *
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target sum
 * @return {number[]} - Array of two indices
 */
function twoSum(nums, target) {
    const numMap = new Map(); // Map to store numbers and their indices
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]; // Find the complement
        if (numMap.has(complement)) { // Check if complement exists in the map
            return [numMap.get(complement), i]; // Return the indices
        }
        // Store the current number and its index
        numMap.set(nums[i], i); 
    }
    // Return empty array if no solution is found
    return []; 
}

// Example usage
const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target)); // Output: [0, 1]
