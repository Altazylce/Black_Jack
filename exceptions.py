"""Exceptions"""


class GameOverException(Exception):
    """Exception raised when points are more than 21"""
    pass


class GameOverUserException(Exception):
    """Exception raised when user lose"""
    pass


class GameOverCroupierException(Exception):
    """Exception raised when croupier lose"""
    pass
