#list1 = [1,1,1]
#list2 = [1,1,1]
inlis1 = []
inlis2 = []
on = True
list_on1 = False
list_on2 = False
pos_x = False
pos_y = False

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
    list_on1 = True
    while list_on1 == True:
        one = raw_input("Add an item to your first list.\n")
        inlis1.append(one)
        contuno = raw_input("Add another item to the  1st list? Type yes or no.\n")
        if (contuno == "yes"):
            list_on1 = True
        elif (contuno == "no"):
            list_on1 = False
            list_on2 = True
        else:
            for d in range(50):
                print("Error 401")
            on = False
    while list_on2 == True:
        two = raw_input("Add an item to your second list.\n")
        inlis2.append(two)
        contdos = raw_input("Add another item to your second list? Type yes or no.\n")
        #print(contdos)
        if (contdos == "yes"):
            list_on2 = True
        elif (contdos == "no"):
            list_on2 = False
        else:
            for g in range(50):
                print("Error 402")
            on = False
        #print_pos()

def print_pos():
    gal = len(inlis1) -1
    guy = len(inlis2) -1
    pos_x = True
    while pos_x == True:
        x = raw_input("First list: Type a number between 0 and " + str(gal) + "\n")
        if (x <= gal):
            print(inlis1[x])
        #elif (x != gal):
            #print("Oops!!!!!!")
            #print("Aaaahhhh!")
            #on = False
        else:
            #print(str(gal) + " hee.")
            pass
        againi = raw_input("Wanna type another position to print for the first list? Answer yes or no.\n")
        if (againi == "yes"):
            pos_x = True
        elif (againi == "no"):
            pos_x = False
            pos_y = True
        else:
            on = False
    while pos_y == True:
        pass
        y = raw_input("Second list: Type a number between 0 and " + str(guy) + "\n")
        if (y <= guy):
            print(inlis2[y])
        #elif (x != guy):
            #print("Oops!!!!!!")
            #print("Aaaahhhh!")
            #on = False
        else:
            #print(str(guy) + " hee.")
            pass
        iniaga = raw_input("Wanna type another position to print for the second list? Answer yes or no.\n")
        if (iniaga == "yes"):
            pos_y = True
        elif (iniaga == "no"):
            pos_y = False
        else:
            on = False

while on == True:
    aski = raw_input("Type input to input two lists, pos to print an item at a certain position, compare to compare them, reset to reset your lists, or whatever else you want to just simply quit.")
    if (aski == "input"):
        give_in()
    elif (aski == "pos"):
        print_pos()
    elif (aski == "compare"):
        compare_list(inlis1,inlis2)
    elif (aski == "reset"):
        inlis1 = []
        inlis2 = []
    else:
        on = False
#print(compare_list(None,None))
#print(compare_list([1,2,3],[1,2,3]))
#print(compare_list([1,2],[1,2,3]))
#print(compare_list([1,[1,2]],[1,[1,2]]))
