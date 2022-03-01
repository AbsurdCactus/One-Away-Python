def one_away(string_one, string_two):
    if len(string_one) == len(string_two):
        return one_edit_replace(string_one, string_two)

    if len(string_one) + 1 == len(string_two):
        return one_edit_insert(string_one, string_two)

    if len(string_one) - 1 == len(string_two):
        return one_edit_insert(string_two, string_one)

    return False


def one_edit_replace(string_one, string_two):

    found_difference = False
    for c1, c2 in zip(string_one, string_two):

        if c1 != c2:
            if found_difference:
                return False

            found_difference = True

    return True


def one_edit_insert(s1, s2):
    found_difference = False

    index_1 = 0
    index_2 = 0

    while index_1 < len(s1) and index_2 < len(s2):
        if s1[index_1] != s2[index_2]:

            if found_difference:
                return False
            found_difference = True
            index_2 += 1
        else:
            index_1 += 1
            index_2 += 1

    return True


# testing
