"""Card tests"""

import pytest
from card import Card, InvalidValue, InvalidColor


def test_creation():
    """Test creation of a valid card"""
    card = Card('diamonds', 'Ace')
    assert card.color == '♦'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    """Test creating wrong value of a card"""
    with pytest.raises(InvalidValue) as message:
        Card('diamonds', 'A')
        assert message == 'Invalid card value'


def test_creation_wrong_color():
    """Test creating wrong color of a card"""
    with pytest.raises(InvalidColor) as message:
        Card('dddd', 'Ace')
        assert message == 'Invalid card key'


def test_card_representation():
    """Test card representation is correct"""
    assert repr(Card('spades', 'Ace')) == 'Ace♠'
    assert repr(Card('diamonds', 'Ace')) == 'Ace♦'
    assert repr(Card('hearts', 'Ace')) == 'Ace♥'
    assert repr(Card('clubs', 'Ace')) == 'Ace♣'
