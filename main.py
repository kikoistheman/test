# using the sliding window technique
def length_of_longest_substring(s: str) -> int:
    # A set to keep track of characters in current window
    char_set = set()
    
    # Two pointers to define the sliding window
    start = 0
    # Variable to keep track of the maximum length of substring without repeating characters
    max_length = 0
    # Loop through each character in the string using 'end' as the end pointer of the sliding window
    for end in range(len(s)):
        # If the character at 'end' is already in the set, it means we have a repeating character
        # We need to shrink the window from the start until we remove the repeating character
        while s[end] in char_set:
            # Remove the character at 'start' pointer from the set
            char_set.remove(s[start])
            # Move the start pointer to the right
            start += 1
        # Add the current character at 'end' to the set
        char_set.add(s[end])
        # Calculate the length of the current window and update max_length if it's greater
        max_length = max(max_length, end - start + 1)
    
    # Return the maximum length found
    return max_length

# Example test cases
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3
print(length_of_longest_substring("bbbbb"))     # Expected output: 1
print(length_of_longest_substring("pwwkew"))    # Expected output: 3

"""
Documentation:

Problem: Longest Substring Without Repeating Characters

Approach:
We use the sliding window technique with two pointers (`start` and `end`) to keep track of the current window of characters without duplicates. We also use a set (`char_set`) to store characters in the current window. 

1. Initialize:
    - `char_set`: A set to keep track of unique characters in the current window.
    - `start`: A pointer to represent the start of the window.
    - `max_length`: A variable to store the maximum length of the substring found.

2. Iterate through the string using the `end` pointer:
    - If the character at the `end` pointer is not in `char_set`, add it to the set.
    - If the character is already in the set, move the `start` pointer to the right until the character at the `end` pointer can be added without duplicates.
    - Update `max_length` by calculating the current window size (`end - start + 1`) and comparing it with the previously recorded maximum.

3. Return the `max_length` after processing all characters.

Explanation:
- This approach ensures that we maintain a substring without repeating characters by dynamically adjusting the window size.
- By using a set, we can efficiently check for duplicates and manage the characters in the current window.
- The time complexity of this approach is O(n) because each character is processed at most twice (once by the `end` pointer and once by the `start` pointer).
- The space complexity is O(min(n, m)), where `n` is the length of the string and `m` is the character set size (e.g., for ASCII, `m` is 128).

Example Test Cases:
1. `s = "abcabcbb"`
    - Output: 3
    - Explanation: The longest substring without repeating characters is "abc" with length 3.

2. `s = "bbbbb"`
    - Output: 1
    - Explanation: The longest substring without repeating characters is "b" with length 1.

3. `s = "pwwkew"`
    - Output: 3
    - Explanation: The longest substring without repeating characters is "wke" with length 3.

Additional Test Cases:
1. `s = ""`
    - Output: 0
    - Explanation: An empty string has a length of 0.

2. `s = "a"`
    - Output: 1
    - Explanation: A single character string has a length of 1.

3. `s = "au"`
    - Output: 2
    - Explanation: The longest substring without repeating characters is "au" with length 2.

4. `s = "dvdf"`
    - Output: 3
    - Explanation: The longest substring without repeating characters is "vdf" with length 3.

5. `s = "anviaj"`
    - Output: 5
    - Explanation: The longest substring without repeating characters is "nviaj" with length 5.

Conclusion:
The sliding window approach is efficient and suitable for this problem, providing a clear and concise solution for finding the length of the longest substring without repeating characters.
"""

