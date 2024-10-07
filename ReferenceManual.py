from ColorCode import get_color_from_pair_number
from ColorCode import MAJOR_COLORS_LIST, MINOR_COLORS_LIST

def print_color_code():
    number_of_combinations = len(MAJOR_COLORS_LIST) * len(MINOR_COLORS_LIST)
    for pair_number in range(1,number_of_combinations+1):
        print(f"{pair_number} -----> {get_color_from_pair_number(pair_number)}")


