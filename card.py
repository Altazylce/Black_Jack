"""Black Jack ASCII Python Game"""


class InvalidColor(Exception):
    """Exception raised for invalid colors"""


class InvalidValue(Exception):
    """Exception raised for invalid values"""


class Card:
    """Card abstraction"""
    possible_colors = {
        'spades': '\u2660',
        'diamonds': '\u2666',
        'hearts': '\u2665',
        'clubs': '\u2663'
    }

    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, color, value) -> None:
        if color not in self.possible_colors:
            raise InvalidColor('Invalid card color')

        self.color = self.possible_colors[color]
        if value not in self.possible_values:
            raise InvalidValue('Invalid card value')

        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}{self.color}'
