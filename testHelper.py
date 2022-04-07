
import  random

def is_in(lst,id,data):
    for elem in lst:
        if(elem[1]==id and elem[0]==data):
            return True
    return False


def main():
    outfile = open('numbersmake.txt', 'w')
    id_in_game=[]
    id_lst=[]
    for i in range(1,300):
        id_lst.append(i)
    for i in range(1, 300):
        id = random.choice(id_lst)
        id_lst.remove(id)
        data = random.randint(-501, 0)
        stri = "Player player" + str(i) + "(" + str(id) + "," + str(data) + ");" + "\n"
        outfile.write(stri)
        id_in_game.append([i,id])

    # after_insert=[]
    # for j in range(1,300):
    #     func=1
    #     lst=random.choice(id_in_game)
    #     if(func==1):
    #         str2 = "assert(table.insert(player" + str(lst[0]) + ".getID(), &player" + str(lst[0]) + ")=="
    #         if (is_in(after_insert,lst[1],lst[0])):
    #             str2=str2+"ALREADY_EXIST);\n"
    #         else:
    #             str2 = str2 + "SUCCESS);\n"
    #             after_insert.append(lst)
    #         outfile.write(str2)
    #     if(func==2):
    #         str3="assert(table.remove(player"+str(lst[0])+".getID())=="
    #         if (is_in(after_insert,lst[1],lst[0])):
    #             after_insert.remove(lst)
    #             str3 = str3 + "SUCCESS);\n"
    #         else:
    #             str3 = str3 + "NOT_FOUND);\n"
    #         outfile.write(str3)
    #     if(func==3):
    #         str4="assert(table.find(player"+str(lst[0])+".getID())"
    #         if (is_in(after_insert,lst[1],lst[0])):
    #             str4 = str4 + "!=-1);\n"
    #         else:
    #             str4 = str4 + "==-1);\n"
    #         outfile.write(str4)


    for i in range(1,300):
        str2 = "assert(table.insert(player" + str(i) + ".getID(), &player" + str(i) + ")==";
        str2 = str2 + "SUCCESS);\n"
        outfile.write(str2)

    for i in range(1,300):
        str2 = "assert(table.find(player" + str(i) + ".getID())!=-1)\n";
        outfile.write(str2)

#Call the main function


main()
