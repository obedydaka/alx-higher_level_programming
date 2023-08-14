#!/usr/bin/python3


def multiple_returns(sentence):

    s_ln = len(sentence)

    if s_ln == 0:
        f_char = None
    else:
        f_char = sentence[0]

    return ((s_ln, f_char))
