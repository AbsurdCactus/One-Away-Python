def one_away(string_one, string_two):
    if len(string_one) == len(string_two):
        return one_edit_replace(string_one, string_two)

    elif len(string_one) + 1 == len(string_two):
        return one_edit_insert(string_one,string_two)

    elif len(string_one) - 1 == len(string_two):
        return one_edit_insert(string_two, string_one)

    
    return False


def one_edit_replace(string_one, string_two):
    
    for i in range(0,len(string_one)):
        
        found_difference = False
        
        if string_one[i] != string_two[i]:
            return found_difference
        
        found_difference = True
        
        return True

def one_edit_insert(s1, s2):

    index_1 = 0
    index_2 = 0

    while index_2 < len(s1) and index_1 < len(s2):
        if s1[index_1] != s2[index_2]:
            index_2 += 1
            if index_1 != index_2:
                return False
                
            else:
                index_1 += 1
                index_2 += 1

        return True





# testing
