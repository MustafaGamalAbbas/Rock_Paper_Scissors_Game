import game_models as gm
""" The start point of the game."""
if __name__ == '__main__':
    game = gm.Game(gm.RandomPlayer(), gm.ReflectPlayer())
    game.play_game()
