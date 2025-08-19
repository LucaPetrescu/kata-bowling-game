import pytest

from Game import Game

@pytest.fixture(scope="function")
def game():
    return Game()

