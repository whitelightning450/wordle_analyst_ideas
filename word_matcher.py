import random
from itertools import chain
import string

LETTERS = string.ascii_lowercase


def list_maker(n, l=5):
    return [("".join(random.choice(LETTERS) for _l in range(l))) for _n in range(n)]


def rightpos_check(guess, answer):
    return [
        _i
        for _i in range(max(len(guess), len(answer)))
        if ord(guess[_i]) ^ ord(answer[_i]) == 0
    ]


def wrongpos_check(guess, answer, rightpos=None):
    if not rightpos:
        rightpos = rightpos_check(guess, answer)
    answer_remain = "".join(l for _i, l in enumerate(answer) if _i not in rightpos)
    wrongpos = []
    for _i, _gl in enumerate(guess):
        if _gl in answer_remain:
            answer_remain = answer_remain.replace(_gl, "", 1)
            wrongpos.append(
                [_i for _al in answer if (_gl == _al) and (_i not in rightpos)]
            )
    return sorted(list(set(chain(*wrongpos))))


def new_double_letter_check(guess, rightpos, wrongpos):
    allrightpos = set(chain(wrongpos, rightpos))
    rightletters = list([guess[i] for i in allrightpos])
    max_repeat_letters = {}
    for _i, _l in enumerate(rightletters):
        _c = guess.count(_l)
        _c2 = rightletters.count(_l)
        if _c > _c2:
            max_repeat_letters[_l] = _c2
    return max_repeat_letters


def double_letter_aggregate(new, prev={}):
    return prev.update(new)


def position_check(guess, answer):
    rightpos = rightpos_check(guess, answer)
    wrongpos = wrongpos_check(guess, answer, rightpos)
    return guess, rightpos, wrongpos


def eliminated_letters(currlist, guess, rightpos, wrongpos):
    return set(currlist) | new_eliminated_letters(guess, rightpos, wrongpos)


def new_eliminated_letters(guess, rightpos, wrongpos):
    allrightpos = set(chain(wrongpos, rightpos))
    rightletters = set([guess[i] for i in allrightpos])
    wrongletters = set(guess) - rightletters
    return wrongletters


def check_all(guess, answer):
    rightpos, wrongpos = position_check(guess, answer)
    double_letters = new_double_letter_check(guess, rightpos, wrongpos)
    eliminated_letters = new_eliminated_letters(guess, rightpos, wrongpos)
    return rightpos, wrongpos, double_letters, eliminated_letters


def guess_game(guess, answer, double_letters=None, eliminated_letters=None):
    if not double_letters:
        double_letters = {}
    if not eliminated_letters:
        eliminated_letters = set()
    _r, _w, _d, _e = check_all(guess, answer)
    _d.update(double_letters)  # _d |= would be the best way
    _e = _e | eliminated_letters  # |= would be the best way
    return guess, answer, _r, _w, _d, _e


def remaining(guess, wordlist, rightpos=None, wrongpos=None, x_letters=None):
    if not rightpos:
        rightpos = []
    if not wrongpos:
        wrongpos = []

    remains = []
    # for word in wordlist:
    # if
    # remains.append(word)

    return remains


def possible_matches(guess, wordlist):
    s_g = set(guess)
    r = []
    for w in wordlist:
        if not (set() == (set(w) & s_g)):
            r.append(w)
    return r


if __name__ == "__main__":
    wl = list_maker(10)
    print(wl)

    print(xor_two_str(wl[1], wl[2]))
    print(position_check(wl[1], wl[2]))
