""" Created by Jieyi on 4/26/16. """


# -*- coding: utf-8 -*-


class WordNode:
    """
    The node of a word which in the content.
    """

    def __init__(self, word=None, pos=None):
        self._word = word  # a word of the content.
        self._pos = pos  # the word of pos.
        self._prev_count = 1  # the same previous word of the appearing times.
        self._score = 0  # the score of this word for calculating.

    def __str__(self):
        return 'word: %s, pos: %s, count: %d' % (self._word, self._pos, self._prev_count)

    def add_count(self):
        self._prev_count += 1

    @property
    def word(self):
        return self._word

    @property
    def pos(self):
        return self._pos

    @property
    def prev_count(self):
        return self._prev_count

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


def main():
    pass


if __name__ == '__main__':
    main()
