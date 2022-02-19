import pytest
from match import list_maker, remaining, position_check


def test_list_maker():
    assert isinstance(list_maker(0), list)


def test_position_check():
    guess = "guers"
    answer = "answe"
    assert position_check(guess, answer) == ([], [2, 4])
    guess = "segus"
    answer = "ansse"
    assert position_check(guess, answer) == ([], [0, 1, 4])
    guess = "gsuse"
    answer = "ansse"
    assert position_check(guess, answer) == ([3, 4], [1])
    guess = "answe"
    answer = "answe"
    assert position_check(guess, answer) == ([0, 1, 2, 3, 4], [])
    guess = "gusse"
    answer = "answe"
    assert position_check(guess, answer) == (
        [2, 4],
        [],
    )  # Omit the second 's' and do not report any wrong positions
    guess = "gsuse"
    answer = "answe"
    assert position_check(guess, answer) == (
        [4],
        [1],
    )  # Only report one wrong-position 's'
    guess = "guess"
    answer = "answe"
    assert position_check(guess, answer) == (
        [],
        [2, 3],
    )  # Only report first wrong-position 's'


def test_remaining():
    assert isinstance(remaining("guess", list_maker(10)), list)
    guess = "guess"
    wordlist = [
        "answe",
        "asnwe",
        "anwes",
        "anwse",
        "ansew",
        "naswe",
        "nsawe",
    ]
    orig_rigwron = position_check(guess, wordlist[4])
    assert orig_rigwron == ([], [2, 3])
