def inputValues(values):
    replace_new_line = values.replace('\n', ',')     # replace new line with comma
    input_to_list = replace_new_line.split(',')       # input values to list
    remove_space = [x for x in input_to_list if x]      # remove empty space in list
    result = [eval(i) for i in remove_space]        # convert list from string to integer
    return result