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
