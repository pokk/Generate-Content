""" Created by Jieyi on 4/18/16. """

# -*- coding: utf-8 -*-
import collections

import nltk

from html_content.connection import HTMLContentGetter
from html_content.html_parser import WikiArticleParser


class AnalysisWord:
    def __init__(self, text):
        self._original_text = text
        self._analysis_text = None

    def analysis(self):
        self._analysis_text = nltk.word_tokenize(self._original_text)

    def pos_tag(self):
        return nltk.pos_tag(self._analysis_text)

    def tag_words_list(self):
        tag_list = self.pos_tag()
        tag_word_list = {}

        for w, t in tag_list:
            if tag_word_list.get(t):
                if w not in tag_word_list[t]:
                    tag_word_list[t].append(w)
            else:
                tag_word_list[t] = [w]

        # Sort by dictionary's key and print it.
        for k, v in collections.OrderedDict(sorted(tag_word_list.items())).items():
            # Sort by dictionary's value.
            print(k, ': ', sorted(v))

        # Sort by dictionary's key.
        return collections.OrderedDict(sorted(tag_word_list.items()))


def main():
    getter = HTMLContentGetter('https://en.wikipedia.org/wiki/Markov')
    text = getter.obtain_content(WikiArticleParser())

    a = AnalysisWord(text)
    a.analysis()
    a.tag_words_list()


if __name__ == '__main__':
    main()
