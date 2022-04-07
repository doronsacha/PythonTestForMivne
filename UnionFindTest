import  random

def is_in(lst,id,data):
    for elem in lst:
        if(elem[1]==id and elem[0]==data):
            return True
    return False


def print_dic(dictionarie):
    sry="//{"
    for element in dictionarie:
        sry=sry+str(element)+"->"+str(dictionarie[element])+","
    return sry+"}\n"
##milon={rosh kvoutsa: [1,2,3,4,5,rosh kvoutsa],}

def find_leader(dic, element):
    for leaders in dic:
        if(element in dic[leaders]):
            return leaders

def union(dic, group1, group2):
    leaders1=find_leader(dic,group1)
    leaders2=find_leader(dic,group2)
    new_group=dic[leaders2]+dic[leaders1]
    if(len(dic[leaders2])>len(dic[leaders1])):
        dic[leaders2]=new_group
        dic.pop(leaders1)
    elif (len(dic[leaders2]) < len(dic[leaders1])):
        dic[leaders1] = new_group
        dic.pop(leaders2)
    elif(leaders1>leaders2):
        dic[leaders1]=new_group
        dic.pop(leaders2)
    elif (leaders1 < leaders2):
        dic[leaders2] = new_group
        dic.pop(leaders1)

def main():
    outfile = open('test.txt', 'w')
    str_main="""
    #include "unionfind.h"
#include <iostream>
#include "cassert"
using namespace std;


class Box{
    int group_id;
public:
    int size;
    Node<Box>* head;
    Box(int id): group_id(id), size(1){}
    int getID()
    {
        return group_id;
    }
};

int main()
{\n"""
    outfile.write(str_main)
    number_of_group=100
    groups={}
    for i in range(number_of_group):
        groups[i]=[i]


    number_of_test=600
    outfile.write("UnionFind<Box> uni("+str(number_of_group)+");\n")
    for i in range(number_of_test):
        groups1=random.randint(0,number_of_group-1)
        groups2 = random.randint(0, number_of_group-1)
        to_find=random.randint(0, number_of_group-1)
        str_union="uni.union_groups(" +str(groups1)+ ","+str(groups2)+");\n"
        union(groups,groups1,groups2)
        outfile.write(str_union)
        a = find_leader(groups, to_find)
        comment=print_dic(groups)
        outfile.write(comment)
        find="assert(uni.find("+str(to_find)+")=="+str(a)+");\n"
        outfile.write(find)

    # number_of_test = 2000
    # outfile.write("UnionFind<Box> uni(" + str(number_of_group) + ");\n")
    # for i in range(number_of_test):
    #     groups1 = random.randint(0, number_of_group - 1)
    #     groups2 = random.randint(0, number_of_group - 1)
    #     to_find = random.randint(0, number_of_group - 1)
    #     func=random.randint(1,2)
    #     a = find_leader(groups, to_find)
    #     comment = print_dic(groups)
    #     if(func==1):
    #         str_union = "uni.union_groups(" + str(groups1) + "," + str(groups2) + ");\n"
    #         union(groups, groups1, groups2)
    #         outfile.write(str_union)
    #         outfile.write(comment)
    #     if(func==2):
    #         find = "assert(uni.find(" + str(to_find) + ")==" + str(a) + ");\n"
    #         outfile.write(find)
    #         outfile.write(comment)




    # number_of_test = 100
    # outfile.write("UnionFind<Box> uni(" + str(number_of_group) + ");\n")
    # for i in range(number_of_test):
    #     groups1 = random.randint(0, number_of_group - 1)
    #     groups2 = random.randint(0, number_of_group - 1)
    #     to_find = random.randint(0, number_of_group - 1)
    #     str_union = "uni.union_groups(" + str(groups1) + "," + str(groups2) + ");\n"
    #     union(groups, groups1, groups2)
    #     outfile.write(str_union)
    #     comment = print_dic(groups)
    #     outfile.write(comment)
    #
    # for i in range(number_of_test):
    #     a = find_leader(groups, to_find)
    #     comment = print_dic(groups)
    #     outfile.write(comment)
    #     find = "assert(uni.find(" + str(to_find) + ")==" + str(a) + ");\n"
    #     outfile.write(find)

    str_end=""" cout << "done";\n}\n"""
    outfile.write(str_end)
    outfile.close()
main()
