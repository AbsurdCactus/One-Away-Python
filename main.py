
def palindrome_detector(string_one, string_two):

    string_list = [string_one, string_two]
    longest = max(string_list)
    shortest = min(string_list)

    char_change_counter = 0

    if len(longest) - len(shortest) > 1:

        char_change_counter += 1

    

    for i in longest:

        if i not in shortest:

            char_change_counter += 1

    for i in shortest:

        if i not in longest:

            char_change_counter += 1

    if char_change_counter > 1:

        return False

    else:

        return True
# testing