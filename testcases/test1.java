import java.util.HashMap;

public class TwoSum {
    /**
     * Finds two numbers in the array `nums` that add up to the `target`.
     * Returns their indices.
     *
     * @param nums Array of integers
     * @param target Target sum
     * @return Array of two indices
     */
    public static int[] twoSum(int[] nums, int target) {
        // Map to store numbers and their indices
        HashMap<Integer, Integer> numMap = new HashMap<>(); 
        for (int i = 0; i < nums.length; i++) {
            // Find the complement
            int complement = target - nums[i]; 
            if (numMap.containsKey(complement)) { // Check if complement exists in the map
                return new int[] { numMap.get(complement), i }; // Return the indices
            }
            // Store the current number and its index
            numMap.put(nums[i], i); 
        }
        // Return empty array if no solution is found
        return new int[] {}; 
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]"); // Output: [0, 1]
    }
}
