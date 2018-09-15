import game_models as gm

""" The start point of the game."""


def choose_player(player_name):
    """
     choose the player function
    :param player_name: the name of player that you need to \
          select his characteristic
    :return: The type of player
    """
    print(f"Please choose the character of {player_name}")
    print("- Enter 0 to be PrimaryPlayer that moves rock only.")
    print("- Enter 1 to be RandomPlayer that moves randomly.")
    print("- Enter 2 to be ReflectPlayer that moves base on the opponent.")
    print("- Enter 3 to be CyclePlayer that moves cyclic \
    'rock', 'paper', 'scissors' ...etc.")
    print("- Enter 4 to be HumanPlayer that moves based of human choice.")
    choice = input("Enter Your choice : ")
    if int(choice) == 0:
        return gm.Player()
    elif int(choice) == 1:
        return gm.RandomPlayer()
    elif int(choice) == 2:
        return gm.ReflectPlayer()

    elif int(choice) == 3:
        return gm.CyclePlayer()

    elif int(choice) == 4:
        return gm.HumanPlayer()
    else:
        print("Wrong input, please try again ")
        return choose_player(player_name)


if __name__ == '__main__':
    game = gm.Game(choose_player("Player 1"), choose_player("Player 2"))
    game.play_game()
