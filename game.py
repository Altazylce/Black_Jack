"""Gameplay configuration"""
from deck import Deck
from player import Player
from exceptions import GameOverException, GameOverCroupierException, GameOverUserException


class Game:
    """Game class"""
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print('Co chcesz zrobić?')
        print('0 - dobieram kartę')
        print('1 - pasuje')

    def _croupier_play(self, user_points):
        croupier = Player()
        while croupier.calculate_points() < user_points:
            croupier.take_card(self.deck.hit())
            print(f'Krupier:\n{croupier.cards}\nposiada {croupier.calculate_points()} punktów! ')

        return croupier.calculate_points()

    def _user_play(self):
        user = Player()
        for _ in range(2):
            card = self.deck.hit()
            user.take_card(card)

        while True:
            print(f'Karty gracza:\n{user.cards}\nposiadasz {user.calculate_points()} punktów!')
            self._print_menu()
            choice = input('Wybierz 0 lub 1: ')
            if choice == '0':
                user.take_card(self.deck.hit())
            elif choice == '1':
                print('Spasowałeś')
                return user.calculate_points()
            else:
                print('Nieprawidłowa wartość!')

    def play(self):
        """Player play"""
        try:
            user_points = self._user_play()
        except GameOverException as error:
            raise GameOverUserException from error

        """Croupier play"""
        try:
            self._croupier_play(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error

        print('Koniec gry, wygrana krupiera!!')
