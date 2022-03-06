import random
from itertools import chain
import string

LETTERS = string.ascii_lowercase


def list_maker(n, l=5):
    return [("".join(random.choice(LETTERS) for _l in range(l))) for _n in range(n)]


def rightpos_check(a, b):
    return [_i for _i in range(max(len(a), len(b))) if ord(a[_i]) ^ ord(b[_i]) == 0]


def position_check(guess, answer):
    rightpos = rightpos_check(guess, answer)
    answer_remain = "".join(l for _i, l in enumerate(answer) if _i not in rightpos)
    wrongpos = []
    for _i, _gl in enumerate(guess):
        if _gl in answer_remain:
            answer_remain = answer_remain.replace(_gl, "", 1)
            wrongpos.append(
                [_i for _al in answer if (_gl == _al) and (_i not in rightpos)]
            )
    return rightpos, sorted(list(set(chain(*wrongpos))))


def eliminated_letters(currlist, guess, rightpos, wrongpos):
    return set(currlist) | new_eliminated_letters(guess, rightpos, wrongpos)


def new_eliminated_letters(guess, rightpos, wrongpos):
    allrightpos = set(chain(wrongpos,rightpos))
    rightletters = set([guess[i] for i in allrightpos])
    wrongletters = set(guess) - rightletters
    return wrongletters


def remaining(guess, wordlist, rightpos=None, wrongpos=None):
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
