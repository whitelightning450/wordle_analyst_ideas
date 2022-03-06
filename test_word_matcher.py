import pytest
from word_matcher import list_maker, remaining, new_eliminated_letters, eliminated_letters, position_check
from word_matcher import possible_matches


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
    assert orig_rigwron == ([], [2, 3])
