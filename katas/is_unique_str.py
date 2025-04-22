def is_unique(string):
    """
    Checks if a string has all unique characters (case-insensitive).

    Args:
        string: the input string

    Returns:
        True if all characters are unique, False otherwise
    """
    string = string.lower()  # Make it case-insensitive (so 'A' == 'a')
    seen = set()
    for char in string:
        if char in seen:  # If we saw the character before, it's not unique
            return False # so we return false otherwise trueeee
        seen.add(char)  # If not, we add it to the set

    return True  # Also if we went through the whole string with no repeats, it's unique


if __name__ == '__main__':
    test1 = "Hello"
    test2 = "World"
    test3 = "Python"
    test4 = "Unique"
    test5 = "Aiman"
    test6 = "Rame"

    print(f'"{test1}" has all unique characters: {is_unique(test1)}')  # Should be False (has repeated 'l')
    print(f'"{test2}" has all unique characters: {is_unique(test2)}')  # Should be True
    print(f'"{test3}" has all unique characters: {is_unique(test3)}')  # Should be True
    print(f'"{test4}" has all unique characters: {is_unique(test4)}')  # Should be True
    print(f'"{test5}" has all unique characters: {is_unique(test5)}')  # Should be True
    print(f'"{test6}" has all unique characters: {is_unique(test6)}')  # Should be True