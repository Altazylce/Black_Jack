"""Game Run"""
from game import Game
from exceptions import GameOverCroupierException, GameOverUserException


try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print('Wygrał gracz!!')
except GameOverUserException:
    print('Wygrał krupier!!')
