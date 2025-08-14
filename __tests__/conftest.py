import pytest

from Game import Game

@pytest.fixture
def game():
    return Game()

