MAJOR_COLORS_LIST = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS_LIST = ["Blue", "Orange", "Green", "Brown", "Slate"]


def check_if_valid_pair_number(major_color_index):
  if major_color_index >= len(MAJOR_COLORS_LIST):
    raise Exception('Major color index out of range.')
  
def check_if_valid_colors(major_color, minor_color):
  try:
    major_color_index = MAJOR_COLORS_LIST.index(major_color)
  except ValueError:
    raise Exception(f'{major_color} is not in list')
  try:
    minor_color_index = MINOR_COLORS_LIST.index(minor_color)
  except ValueError:
    raise Exception(f'{minor_color} is not in list')
  return major_color_index, minor_color_index

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_color_index = zero_based_pair_number // len(MINOR_COLORS_LIST)
  check_if_valid_pair_number(major_color_index)
  minor_color_index = zero_based_pair_number % len(MINOR_COLORS_LIST)
  return MAJOR_COLORS_LIST[major_color_index], MINOR_COLORS_LIST[minor_color_index]

def get_pair_number_from_color(major_color, minor_color):
  major_color_index, minor_color_index = check_if_valid_colors(major_color, minor_color)
  return major_color_index * len(MINOR_COLORS_LIST) + minor_color_index + 1
