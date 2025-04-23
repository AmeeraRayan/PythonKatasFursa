def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    if not strs:
        return ""

    # Start with the first word as the prefix
    prefix = strs[0]

    # Go through each string in the list
    for word in strs[1:]:
        # Shrink the prefix until it matches the start of the word
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # Remove the last letter from prefix
            if not prefix:
                return ""  # No common prefix at all

    return prefix


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]
    test5 = ["ameera", "asma", "aiman"]

    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"
    print(f"Longest Common Prefix: {longest_common_prefix(test5)}")  # Output: "a"