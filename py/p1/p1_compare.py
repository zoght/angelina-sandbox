list1 = [1,1,1]
list2 = [1,1,1]


def compare_list(param_1,param_2):
    if (param_1 == None and param_2 == None ):
        return True
    elif (len(param_1) < len(param_2)) or (len(param_2) < len(param_1)):
        return False
    elif (len(param_1) == len(param_2)):
        i = 0
        while (i < len(param_1)):
            if (param_1[i] == param_2[i]):
                i = i +1
            else:
                return False
        return True



print(compare_list(None,None))
print(compare_list([1,2,3],[1,2,3]))
print(compare_list([1,2],[1,2,3]))
print(compare_list([1,[1,2]],[1,[1,2]]))
