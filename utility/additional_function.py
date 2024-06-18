def get_number_of_chars(string : str, char_in_string : str) -> int:
    sum = 0
    for char in string:
        if char == char_in_string:
            sum +=1
    return sum
