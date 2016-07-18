#list1 = [1,1,1]
#list2 = [1,1,1]
inlis1 = []
inlis2 = []
on = True

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

def give_in():
    one = raw_input("First list please. Be sure to seperate with commas")
    two = raw_input("Second list please. SAME AS FIRST!")
    inlis1.append[one]
    inlis2.append[two]
    gal = len(inlis1 -1)
    guy = len(inlis2 -1)
    x = raw_input("First list: Type a number between 0 and " + str(gal) + "\n")
    if (x < gal):
        print(inlis1[x])
    elif (x != gal):
        print("Oops!!!!!!")
        print("Aaaahhhh!")
    else:
        print(str(gal) + " hee.")
    y = raw_input("Second list: Type a number between 0 and " + str(guy) + "\n")
    if (y < guy):
        print(inlis2[y])
    elif (x != guy):
        print





print(compare_list(None,None))
print(compare_list([1,2,3],[1,2,3]))
print(compare_list([1,2],[1,2,3]))
print(compare_list([1,[1,2]],[1,[1,2]]))
