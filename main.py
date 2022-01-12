# tic tac toe
"""
[x]: draw a board
[x]: input player Name
[x]: put sign to each player
[x]: if they don't input between (1,9), direct them to previous state
[X]: put sign to exact spot
[X]: print board after each input
[x]: calculate and show result
"""
instructions = """
This will be our tic tac toe board

 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 

*instructions:
1. Insert the spot number(1-9) to put your sign,
2. You must fill all 9 spots to get result,
3. Player 1 will go first.
"""

sign_dict = [[], [], [], [], [], [], [], [], []]


def len_check(x):
    if len(x) == 1:
        return x[0]
    else:
        return " "


def print_board(sign_dict):
    board = f"""

   {len_check(sign_dict[0])} | {len_check(sign_dict[1])} | {len_check(sign_dict[2])}
  ---|---|---
   {len_check(sign_dict[3])} | {len_check(sign_dict[4])} | {len_check(sign_dict[5])}
  ---|---|---
   {len_check(sign_dict[6])} | {len_check(sign_dict[7])} | {len_check(sign_dict[8])}

  """
    print(board)


index_list = []


def take_input(player_name):
    while True:
        x = int(input(f'{player_name}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print('This spot is blocked.')
                continue
            index_list.append(x)
            return x
        print('Please Enter number between 1-9')


def result_calculation(sign_dict, player_one, player_two):
    if sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'X' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'X' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'X' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'X' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'X' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'X' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'X' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'X':
        print(f'Congratulations {player_one}. You WON.!!')
    elif sign_dict[0][0] == sign_dict[1][0] == sign_dict[2][0] == 'O' or sign_dict[1][0] == sign_dict[4][0] == \
            sign_dict[7][0] == 'O' or sign_dict[0][0] == sign_dict[4][0] == sign_dict[8][0] == 'O' or sign_dict[2][0] == \
            sign_dict[5][0] == sign_dict[8][0] == 'O' or sign_dict[3][0] == sign_dict[4][0] == sign_dict[5][0] == 'O' or \
            sign_dict[2][0] == sign_dict[4][0] == sign_dict[6][0] == 'O' or sign_dict[6][0] == sign_dict[7][0] == \
            sign_dict[8][0] == 'O' or sign_dict[0][0] == sign_dict[3][0] == sign_dict[6][0] == 'O':
        print(f'Congratulations {player_two}. You WON.!!')
    else:
        print("This is a tie..!! Nobody won. Play Again.")


def main():
    print("Welcome to sunny's tic tac toe game.!!")
    player_one = input("Enter player 1 name: ")
    player_two = input("Enter player 2 name: ")
    print(f"Thank you for joining Mr. {player_one} and Mr. {player_two}")
    print(instructions)
    print(f"Mr. {player_one}'s sign is - X")
    print(f"Mr. {player_two}'s sign is - O")
    input("Enter any key to start the game: ")
    print_board(sign_dict)
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dict[index].append('X')
        else:
            index = take_input(player_two)
            sign_dict[index].append('O')
        print_board(sign_dict)
    result_calculation(sign_dict, player_one, player_two)


main()
