
import random
import  numpy

# k=random.randint(1,10) ##########################################################################           mispar kvoutsot
# scale=random.randint(-1,20)  ####################################################                scale

k=5
scale =5

def find_leader(dic, element): # dic={group1:[group1, group2],...
    for leaders in dic:
        if(element in dic[leaders][0]):
            return leaders


### player_dic={player_id:[playerid, group_id, score, level],...}
### groups_dic={group_id9=([group3,group4,group9],[player1, player2,...]), group_id=[]...}
def union(player_dic,dic, group1, group2):
    leaders1=find_leader(dic,group1)
    leaders2=find_leader(dic,group2)
    new_group=dic[leaders2][0]+dic[leaders1][0]
    player1=dic[leaders1][1]
    player2 = dic[leaders2][1]
    players=player1+player2
    if(len(dic[leaders2][0])>len(dic[leaders1][0])):
        # for play in player_dic:
        #     if (player_dic[play[1]] == group1 or player_dic[play[1]] == group2 or player_dic[play[1]] == leaders1 or player_dic[play[1]] == leaders2):
        #         player_dic[play[1]]=leaders2
        dic[leaders2][0]=new_group
        dic[leaders2][1] = players
        dic.pop(leaders1)
    elif (len(dic[leaders2][0]) < len(dic[leaders1][0])):
        dic[leaders1][0] = new_group
        dic[leaders1][1] = players
        dic.pop(leaders2)
    elif(leaders1>leaders2):
        dic[leaders1][0]=new_group
        dic[leaders1][1] = players
        dic.pop(leaders2)
    elif (leaders1 < leaders2):

        dic[leaders2][0] = new_group
        dic[leaders2][1] = players
        dic.pop(leaders1)


### player_dic={player_id:[playerid, group_id, score, level],...}
### groups_dic={group_id9=([group3,group4,group9],[player1, player2,...]), group_id=[]...}
def addPlayer(dic_group,dic_player,player_id, group_id,score):
    if(group_id>k or group_id<=0 or player_id<=0 or score>scale or score<=0):
        return "INVALID_INPUT"
    if(player_id in dic_player):
            return "FAILURE"
    leader=find_leader(dic_group,group_id)
    dic_player[player_id] = [player_id,leader,score,0]
    (dic_group[leader])[1].append(player_id)
    return "SUCCESS"

def remove_player(dic_group,dic_player,player_id):
    if(player_id<=0):
        return "INVALID_INPUT"
    if(player_id not in dic_player):
        return "FAILURE"
    group=dic_player[player_id][1]
    group=find_leader(dic_group,group)
    dic_player.pop(player_id)
    ((dic_group[group])[1]).remove(player_id)
    return "SUCCESS"

def increase_level(dic_player, player_id,level_increase):
    if(player_id<=0 or level_increase <=0):
        return "INVALID_INPUT"
    if (player_id not in dic_player):
        return "FAILURE"
    (dic_player[player_id])[3]=(dic_player[player_id])[3]+level_increase
    return "SUCCESS"

def changePlayerIDScore(dic_player, player_id,NewScore):
    if(player_id<=0 or NewScore> scale or NewScore<=0):
        return "INVALID_INPUT"
    if(player_id not in dic_player):
        return "FAILURE"
    (dic_player[player_id])[2] = NewScore
    return "SUCCESS"


### player_dic={player_id:[playerid, group_id, score, level],...}
### groups_dic={group_id9=([group3,group4,group9],[player1, player2,...]), group_id=[]...}
def init(dic_groups):
    for i in range(1,k+1):
        dic_groups[i]=[[i]]
        dic_groups[i].append([])

### player_dic={player_id:[playerid, group_id, score, level],...}
### groups_dic={group_id9=([group3,group4,group9],[player1, player2,...]), group_id=[]...}
def merge(dic_group, dic_player,groupID1,groupID2):
    if(groupID1<=0 or groupID2<=0 or groupID1>k or groupID2>k):
        return "INVALID_INPUT"
    union(dic_player,dic_group,groupID1,groupID2)
    return "SUCCESS"


def averageHighestPlayerLevelByGroup(dic_group,dic_player, group_id, m, a):
    if group_id > k or group_id < k or m <= 0:
        return "INVALID_INPUT"
    if group_id == 0 and m > len(dic_player):
        return "FAILURE"
    group_leader = find_leader(dic_group,group_id)
    if len(dic_group[group_leader][1]) < m:
        return "FAILURE"
    if group_id == 0:
        lvls = []
        for x in dic_player:
            lvls.append(x[3])
        sorted_lvls = sorted(lvls)
        summ = 0
        for lvl in sorted_lvls[-m:]:
            summ += lvl
        a = [summ / m]
        return "SUCCESS"

    else:
        players = dic_group[group_leader][1]
        lvls = []
        for x in players:
            lvls.append(dic_player[x][3])
        sorted_lvls = sorted(lvls)
        summ = 0
        for lvl in sorted_lvls[-m:]:
                summ += lvl
        a = [summ / m]
        return "SUCCESS"


def getPercentOfPlayersWithScoreInBounds(dic_players,dic_groups,groupID,score, lowerLevel,higherLevel,a):
    if groupID > k or groupID<0:
        return -1
    group_leader = find_leader(dic_groups, groupID)
    if(groupID>0):
        group_leader = find_leader(dic_groups, groupID)
        players=dic_groups[group_leader][1]
        arr=[]
        for play in players:
            if(dic_players[play][2]==score):
                arr.append(dic_players[play][3])
        arr.sort()
        for element in arr:
            if(element<lowerLevel or element>higherLevel):
                arr.remove(element)
    if(groupID==0):
        for players in dic_players:
            if(dic_players[players][2]==score):
                arr.append(dic_players[players][3])
        arr.sort()
        for element in arr:
            if (element < lowerLevel or element > higherLevel):
                arr.remove(element)

    if(len(arr)==0):
        return -2
    counter=0
    for element in arr:
        if(element==score):
            counter+=1
    a=(counter/len(arr))*100
    return a
########################################################################################################################

def main():
    outfile=open("test.txt","w")
    str_main= """
    #include "DS.h"
    #include <cassert>
    int main()
    {\n
    """
    outfile.write(str_main)
    string_init="PlayerManager player("+str(k)+","+str(scale)+");\n"
    outfile.write(string_init)
    dic_grp={}
    dic_player={}
    player_in_game=[]
    init(dic_grp)

    number_of_functions=800##random.randint(1,800)##############################################the num of functions calls
    for i in range(number_of_functions):
        func= numpy.random.choice(numpy.arange(1, 6), p=[0.4, 0.1, 0.25, 0.05, 0.2])
        num_of_player=random.randint(1,700)##############################################the num of players


        if(func==1):
            player=random.randint(1,num_of_player)  ###can change here this is the parameters of add players
            group=random.randint(1,k+1) ###can change here this is the parameters of add players
            score=random.randint(-1,scale+1) ###can change here this is the parameters of add players
            res=addPlayer(dic_grp, dic_player, player, group, score)
            if(res=="SUCCESS"):
                player_in_game.append(player)
            str_func="assert(player.addPlayer("+str(player)+","+ str(group)+ ","+str(score)+")=="+res+");\n" ##TODO:write the DS



        if (func == 2):
            if(len(dic_player)==0):
                player=random.randint(1,num_of_player)
            else:
                player = random.choice(player_in_game)###can change here this is the parameters of add players
                player_in_game.remove(player)
            str_func = "assert(player.removePlayer(" + str(player) + ")==" + remove_player(dic_grp,dic_player,player) + ");\n"  ##TODO:write the DS


        if (func == 3):
            if(len(player_in_game)==0):
                player=random.randint(1,num_of_player)
            else:
                player = random.choice(player_in_game)
            lvl_increase=1
            str_func = "assert(player.increasePlayerIDLevel(" + str(player) +","+ str(lvl_increase) + ")==" + increase_level(dic_player,player,lvl_increase) + ");\n"  ##TODO:write the DS


        if(func == 4):
            if(len(player_in_game)==0):
                player=random.randint(1,num_of_player)
            else:
                player = random.choice(player_in_game)  ###can change here this is the parameters of add players
            score= random.randint(1,scale+1)###can change here this is the parameters of add players
            str_func = "assert(changePlayerIDScore("+str(player)+","+str(score)+")==" + changePlayerIDScore(dic_player,player,score) + ");\n"


        if(func==5):

            group = random.randint(1, k)  ###can change here this is the parameters of add players
            score_in_grp=[]
            for element in (dic_grp[find_leader(dic_grp,group)])[1]:
                    if((dic_player[element])[2] not in score_in_grp):
                        score_in_grp.append(dic_player[element][2])




            score = random.randint(1, scale + 1)  ###can change here this is the parameters of add players
            low =0
            high=9
            a=0
            a=getPercentOfPlayersWithScoreInBounds(dic_player,dic_grp,group,score,low,high,a)
            str_func="double res=0;\n"
            if(a==-1):
                res="INVALID_INPUT"
            if(a==-2):
                res="FAILURE"
            else:
                res="SUCCESS"
            str_func = str_func + "assert(player.getPercentOfPlayersWithScoreInBounds("+str(group)+","+str(score)+","+str(low)+","+str(high)+",&res)=="+res+");\n"  ##TODO:write the DS
            str_func=str_func+"assert(res=="+str(a)+");\n"
        if(func==6):
            group = random.randint(1, k + 20)  ###can change here this is the parameters of add players
            m=random.randint(1, num_of_player + 20)
            lstres = []
            str_func = "double res=-1;\n"
            string_res = averageHighestPlayerLevelByGroup(dic_grp,dic_player,group,m,lstres)
            str_func = str_func + "assert(AverageHighestPlayerLevelByGroup(,"+"data structure"+str(group)+","+str(m)+",&res)=="+string_res+ ");\n"  ##TODO:write the DS
            if(string_res !="SUCCESS"):
                str_func=str_func+ "assert(res==-1);\n"
            else:
                str_func = str_func + "assert(res==" + str(lstres[0]) + ");\n"
        if(func==7):
            group1 = random.randint(1, k + 20)  ###can change here this is the parameters of add players
            group2 = random.randint(1, k + 20)  ###can change here this is the parameters of add players
            str_func = "assert(mergeGroups(" + "data structure" + "," + str(group1) + ","+ str(group2)  + ")==" + merge(dic_grp,dic_player,group1,group2) + ");\n"  ##TODO:write the DS
        outfile.write(str_func)
    str_end="player.Quit();\n}"
    outfile.write(str_end)

    outfile.close()


main()




