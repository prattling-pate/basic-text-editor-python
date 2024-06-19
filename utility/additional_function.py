def get_number_of_chars(string : str, char_in_string : str) -> int:
    sum = 0
    for char in string:
        if char == char_in_string:
            sum +=1
    return sum

def is_list_non_zero(list):
        for row in list:
            if len(row) > 0:
                return False
        return True
