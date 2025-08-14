import pytest

from Game import Game

def roll_many(game, rolls, pins):
    for _ in range(rolls):
        game.roll(pins)

def test_game_initialization(game):
    assert game is not None
    assert isinstance(game, Game)

def test_gutter_game(game):
    roll_many(game, 20, 0)
    assert game.score() == 0;
    

def test_all_ones(game):
    roll_many(game, 20, 1)
    assert game.score() == 20

def test_one_spare(game):
    game.roll(5)