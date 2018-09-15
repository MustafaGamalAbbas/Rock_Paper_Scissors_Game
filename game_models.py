import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    player_name = None

    def move(self):
        """
         This function make the player choose the next move
        :return: The next move it's one of ['rock', 'paper', 'scissors']
        """
        print(f"{self.player_name} moved")
        return 'rock'

    def learn(self, my_move, their_move):
        """
         This function make the player know what's the another player move
        :param my_move: The player move
        :param their_move: The another player move
        :return:
        """
        pass

    def set_player_name(self, name):
        self.player_name = name


class RandomPlayer(Player):

    def move(self):
        """
         This function make the RandomPlayer choose the next move randomly
        :return: The next move it's one of ['rock', 'paper', 'scissors']
        """
        next_move = random.choice(moves)
        print(f"{self.player_name} moved")
        return next_move

    def learn(self, my_move, their_move):
        """
         This function make the player know what's the another player move
        :param my_move: The player move
        :param their_move: The another player move
        :return:
        """
        pass

    def set_player_name(self, name):
        self.player_name = name


class ReflectPlayer(Player):
    next_move = random.choice(moves)

    def move(self):
        """
        This function make the ReflectPlayer choose the next move base \
        on the move of the another player at the last
        round :return: The next move it's one of ['rock', 'paper', 'scissors']
        """
        print(f"{self.player_name} moved")
        return self.next_move

    def learn(self, my_move, their_move):
        """
         This function make the player know what's the another player \
         move and save it to be the next move
        :param my_move: The player move
        :param their_move: The another player move
        :return:
        """
        self.next_move = their_move


class CyclePlayer(Player):
    index_of_current_move = 0

    def move(self):
        """
        This function make the CyclePlayer choose the next move, \
        the chooses will be 'rock', 'paper', 'scissors',
        ' rock' ,'paper' ...etc
        :return: The next move it's one of ['rock', 'paper', 'scissors']
        """
        next_move = moves[self.index_of_current_move]
        self.index_of_current_move = \
            (self.index_of_current_move + 1) % len(moves)
        print(f"{self.player_name} moved")
        return next_move

    def learn(self, my_move, their_move):
        """
         This function make the player know what's the another player \
         move and save it to be the next move
        :param my_move: The player move
        :param their_move: The another player move
        :return:
        """
        pass


class HumanPlayer(Player):

    def move(self):
        """
        This function make the HumanPlayer choose the next move
        :return: The next move it's one of ['rock', 'paper', 'scissors']
        """
        humanInput = input(f"{self.player_name}Please,\
         Enter your next move it should one of {moves} :")
        if humanInput in moves:
            print(f"{self.player_name} moved")
            return humanInput
        else:
            print(f"you choose({humanInput}) is not in available \
            chooses, so try a gain.")
            return self.move()

    def learn(self, my_move, their_move):
        """
         This function make the player know what's the another player move \
          and save it to be the next move
        :param my_move: The player move
        :param their_move: The another player move
        :return:
        """
        pass


def beats(one, two):
    """
     beats function it's a judge function to judge between \
     the two players who is win?
    :param one: The move of player one
    :param two: The move of player two
    :return: return -1 if the player one win \
                else if return 1 if the player two win  \
                else return 0 if the round is draw
    """
    if ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')):
        return -1
    elif one == two:
        return 0
    return 1


class Game:
    number_of_wins_for_playerOne = 0
    number_of_wins_for_playerTwo = 0
    number_of_draw_rounds = 0

    def __init__(self, p1, p2):
        """
         init function to specific the players of game
        :param p1: player one
        :param p2: player two
        """
        p1.set_player_name("Player 1: ")
        p2.set_player_name("Player 2: ")
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        """
         play function that has the logic of game for one round.
        :return: nothing
        """
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.record_the_result_of_round(move1, move2)

    def record_the_result_of_round(self, player_one_movie, player_two_movie):
        """
         This function responsibility to record who is win
        :param player_one_movie: The player onw move
        :param player_two_movie: The player two move
        :return: nothing
        """
        who_is_win = beats(player_one_movie, player_two_movie)
        if who_is_win == -1:
            self.number_of_wins_for_playerOne += 1
        elif who_is_win == 1:
            self.number_of_wins_for_playerTwo += 1
        else:
            self.number_of_draw_rounds += 1
            self.number_of_wins_for_playerOne += 1
            self.number_of_wins_for_playerTwo += 1

    def play_game(self):
        """
         play function that has the logic of all game.
        :return: nothing
        """
        print("Game start!")
        for running_round in range(3):
            print(f"Round {running_round}:")
            self.play_round()
            self.tell_them_the_score()
        self.announce_the_winner()
        print("Game over!")

    def announce_the_winner(self):
        """
        announcement function to announce who the win the game\
         if there is a winner else announce that the game is
        draw. :return:
        """
        if self.number_of_wins_for_playerOne \
                > self.number_of_wins_for_playerTwo:
            print("Oh No, The Winner is player one")
        elif self.number_of_wins_for_playerOne \
                < self.number_of_wins_for_playerTwo:
            print("Oh No, The Winner is player two")
        else:
            print("Oh No,Draw! no one win")

    def tell_them_the_score(self):
        """
         this function just tell the player what's the score now.
        :return: nothing
        """
        print("        Score       ")
        print(" Player 1 | Player 2")
        print(f"    {self.number_of_wins_for_playerOne}\
          {self.number_of_wins_for_playerTwo} ")
        print("----------------------------------------")
