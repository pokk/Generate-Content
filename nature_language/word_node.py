""" Created by Jieyi on 4/26/16. """


# -*- coding: utf-8 -*-


class WordNode:
    """
    The node of a word which in the content.
    """

    def __init__(self, word=None, pos=None):
        self._word = word  # a word of the content.
        self._pos = pos  # the word of pos.

    def __str__(self):
        return 'word: %s, pos: %s' % (self._word, self._pos)

    @property
    def word(self):
        return self._word

    @property
    def pos(self):
        return self._pos


def main():
    pass


if __name__ == '__main__':
    main()
