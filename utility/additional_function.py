def check_contains(string : str, char_in_string : str) -> bool:
    for char in string:
        if char == char_in_string:
            return True
    return False
