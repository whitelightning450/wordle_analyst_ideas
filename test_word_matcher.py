import pytest
from word_matcher import (
    list_maker,
    remaining,
    new_eliminated_letters,
    new_double_letter_check,
    eliminated_letters,
    position_check,
    possible_matches,
)


def test_list_maker():
    assert isinstance(list_maker(0), list)


def test_position_check():
    guess = "guers"
    answer = "answe"
    assert position_check(guess, answer) == ("guers", [], [2, 4])

    guess = "segus"
    answer = "ansse"
    assert position_check(guess, answer) == ("segus", [], [0, 1, 4])

    guess = "gsuse"
    answer = "ansse"
    assert position_check(guess, answer) == ("gsuse", [3, 4], [1])

    guess = "answe"
    answer = "answe"
    assert position_check(guess, answer) == ("answe", [0, 1, 2, 3, 4], [])

    guess = "gusse"
    answer = "answe"
    # Omit the second 's' and do not report any wrong positions
    assert position_check(guess, answer) == ("gusse", [2, 4], [])

    guess = "gsuse"
    answer = "answe"
    # Only report one wrong-position 's'
    assert position_check(guess, answer) == ("gsuse", [4], [1])

    guess = "guess"
    answer = "answe"
    # Only report first wrong-position 's'
    assert position_check(guess, answer) == ("guess", [], [2, 3])


def test_new_double_letter_check():
    guess = "gusse"
    answer = "answe"
    (rightpos, wrongpos) = position_check(guess, answer)
    assert new_double_letter_check(guess, rightpos, wrongpos) == {"s": 1}


def test_eliminated_letters():
    currset = {"z", "b", "r"}  # The answer is 'answe' and we guessed 'zebra' before
    guess = "guess"
    rightpos, wrongpos = ([], [2, 3])
    _new_set_of_eliminated_letters = {"z", "b", "r", "g", "u"}
    test_result = eliminated_letters(currset, guess, rightpos, wrongpos)
    assert test_result ^ _new_set_of_eliminated_letters == set()


def test_new_eliminated_letters():
    guess = "guess"
    rightpos, wrongpos = ([], [2, 3])
    _new_set_of_eliminated_letters = {"g", "u"}
    test_result = new_eliminated_letters(guess, rightpos, wrongpos)
    assert test_result ^ _new_set_of_eliminated_letters == set()


def test_possible_matches():
    guess = "wards"
    wordlist = [
        "rides",
        "drive",
        "snort",
        "green",
        "trove",
        "zebra",
        "couch",
        "adieu",
        "sport",
        "bicep",
        "quick",
    ]
    _possible_matches = [
        "rides",
        "drive",
        "snort",
        "green",
        "trove",
        "zebra",
        "adieu",
        "sport",
    ]
    test_result = possible_matches(guess, wordlist)
    assert test_result == _possible_matches


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
    assert orig_rigwron == ("guess", [], [2, 3])
