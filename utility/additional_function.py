def get_number_of_chars(string : str, char_in_string : str) -> int:
    sum = 0
    for char in string:
        if char == char_in_string:
            sum +=1
    return sum

def is_2d_list_empty(array : list[list]):
    for row in array:
        if len(row) > 0:
            return False
    return True

def is_list_ascending(array : list[int]):
    """
    Returns True if the list given is ascending, False otherwise
    """
    prev_item = float('-inf')
    for item in array:
        if item < prev_item:
            return False
        prev_item = item
    return True