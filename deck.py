"""Deck of cards"""
from random import shuffle
from card import Card


class Deck:
    """A deck of cards"""
    def __init__(self) -> None:
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(Card(color=color, value=value))

    def shuffle(self) -> None:
        """Shuffle the deck"""
        shuffle(self.cards)

    def hit(self):
        """Hitting a card from the deck"""
        return self.cards.pop()
