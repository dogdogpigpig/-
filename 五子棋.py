import random
def menu():
    print('-'*7,'welcome to the game','-'*7)
    print('         | 1 | 2 | 3 |')
    print('         | 4 | 5 | 6 |')
    print('         | 7 | 8 | 9 |')
    print('-'*36)
def player(player_list,computer_list):
    while True:
        try:
            a=int(input('please input where you want:'))
            if (a<=9 and a>=1) and a not in computer_list and a not in player_list:
                print('move successfully')
                player_list.append(a)
                break
            else:
                print('input error!please input again')
        except:
            print('not 1-9 number')
def computer(player_list,computer_list):
    while True:
        b=random.randint(1,9)
        if b not in player_list and b not in computer_list :
            print(b)
            computer_list.append(b)
            break
def condition(player_list,computer_list):
    win=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in win:
        if  all(j in player_list for j in i):
            return True
        if all(j in computer_list for j in i):
            return True
    return False
def main():
    player_wins=0
    computer_wins=0
    ties=0
    while True:
        menu()
        player_list=[]
        computer_list=[]
        while True:
            player(player_list,computer_list)
            if condition(player_list,computer_list):
                print('player win')
                player_wins+=1
                break
            if len(player_list)+len(computer_list)==9:
                print('It is a tie')
                ties+=1
                break
            computer(player_list,computer_list)
            print('player:', player_list)
            print('computer:', computer_list)
            if condition(player_list,computer_list):
                print('computer win')
                computer_wins+=1
                break
            if len(player_list)+len(computer_list)==9:
                print('It is a tie')
                ties+=1
                break
            print('         | 1 | 2 | 3 |')
            print('         | 4 | 5 | 6 |')
            print('         | 7 | 8 | 9 |')
        while True:
            choice=input('play again?  yes/no:\n')
            if choice=='yes':
                break
            elif choice=='no':
                print('player wins:',player_wins)
                print('computer wins',computer_wins)
                print('ties:',ties)
                return
            else:
                print('input again:yes/no')
if __name__ == '__main__':
    main()


