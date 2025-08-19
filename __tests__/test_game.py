import pytest

from Game import Game

def roll_many(game, rolls, pins_down):
    for _ in range(rolls):
        game.roll(pins_down)

def roll_spare(game):
    game.roll(6)
    game.roll(4)

def roll_strike(game):
    game.roll(10)

def test_roll_ball(game):
    game.roll(0)

def test_game_initialization(game):
    assert game is not None
    assert isinstance(game, Game)

def test_gutter_game(game):
    roll_many(game, 20, 0)
    assert game.score() == 0;

def test_all_ones(game):
    roll_many(game, 20, 1)
    assert game.score() == 20

def test_one_spare_followed_by_three(game):
    roll_spare(game)
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 10 + 3 + 3

def test_one_strike_followed_by_three_and_four(game):
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 10 + 3 + 4 + 3 + 4

def test_one_strike_followed_by_two(game):
    roll_strike(game)
    game.roll(2)
    roll_many(game, 17, 0)
    assert game.score() == 10 + 2 + 2

def test_perfect_game(game):
    roll_many(game, 12, 10)
    assert game.score() == 300