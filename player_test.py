"""Test player"""
from player import Player
from card import Card

def test_calculate_player_points():
    """Test calculate player points"""
    card = Card('spades', 2)
    card2 = Card('hearts', 5)

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 7

def test_calculate_player_points_two_aces():
    """Test two Aces points on hand"""
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 21

def test_calculate_player_points_one_aces():
    """Test one Ace points and one regular on hand"""
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 2)

    player = Player()
    player.take_card(card)
    player.take_card(card2)

    assert player.calculate_points() == 13

def test_calculate_player_points_three_aces():
    """Test three Aces points on hand"""
    card = Card('spades', 'Ace')
    card2 = Card('hearts', 'Ace')
    card3 = Card('diamonds', 'Ace')

    player = Player()
    player.take_card(card)
    player.take_card(card2)
    player.take_card(card3)

    assert player.calculate_points() == 3
