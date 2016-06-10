""" Created by Jieyi on 4/18/16. """

# -*- coding: utf-8 -*-
import collections

import nltk

from nature_language import test_text


class AnalysisWord:
    """
    Analysis the part of speech of the word and separate each of the word of the content.
    """

    def __init__(self, text):
        self._original_text = text
        self._analysis_text = None
        self.__check_analysis_text = {}

    def analysis(self):
        """
        Separate the sentence by the each meaning words.
        """

        self._analysis_text = nltk.word_tokenize(self._original_text)

    def pos_tag(self):
        """
        Analysis the each of words and attach the Part Of Speech.

        :return: the list of pos.
        """

        return nltk.pos_tag(self._analysis_text)

    def tag_words_list(self):
        """
        Category the tag list and words are appeared.

        :return: dict or the tag and word.
        """

        tag_word_list = {}

        for w, t in self.pos_tag():
            self.is_word_in_check(w, t, tag_word_list)

        # Sort by dictionary's key.
        return collections.OrderedDict(sorted(tag_word_list.items()))

    def is_word_in_check(self, word, tag, tag_word_list=None):
        """
        Check the word has already added into the list.

        :param word: a word of the content.
        :param tag: a tag of a word of the content
        :param tag_word_list: checking list.
        :return: True, the word or the tag is in the list; otherwise, not.
        """

        inner_tag_word_list = tag_word_list if tag_word_list is not None else self.__check_analysis_text

        # Check the tag is in the list or not.
        if inner_tag_word_list.get(tag):
            # Check the word has been in the tag or not.
            if word not in inner_tag_word_list[tag]:
                inner_tag_word_list[tag].append(word)
                return False
        else:  # If not, add a new tag and word into dictionary.
            inner_tag_word_list[tag] = [word]
            return False
        return True


def main():
    # getter = HTMLContentGetter('https://en.wikipedia.org/wiki/Markov')
    # text = getter.obtain_content(WikiArticleParser())
    # text = markov_text
    text = test_text

    a = AnalysisWord(text)
    a.analysis()
    l = a.tag_words_list()
    for k, v in l.items():
        print(k, ': ', sorted(v))


if __name__ == '__main__':
    main()
