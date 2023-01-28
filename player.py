"""Player"""
from card import Card
from exceptions import GameOverException


class Player:
    """Player class and scoring"""
    def __init__(self):
        self.cards = []

    def take_card(self, card: Card):
        """Take card from deck"""
        self.cards.append(card)

    def calculate_points(self):
        """Calculate points from cards"""
        score = 0
        number_of_aces = len([card for card in self.cards if card.value == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            score = 10

        for card in self.cards:
            if card.value == 'Ace':
                score += 1
            elif card.value in ['Jack', 'Queen', 'King']:
                score += 10
            else:
                score += card.value

        if score > 21:
            print(f'{score} punktów! Trochę za dużo :)')
            raise GameOverException('Number of points is greater than 21!! You Loss!!')

        return score
