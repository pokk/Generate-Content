""" Created by Jieyi on 4/18/16. """

# -*- coding: utf-8 -*-

import nltk
from nltk.probability import FreqDist


def main():
    text_str = """
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    And now for something completely different.
    """

    text = nltk.word_tokenize(text_str)
    # word_tokenize("And now for something completely different")
    print(text)
    tagged = nltk.pos_tag(text)
    print(tagged)
    # entities = nltk.chunk.ne_chunk(tagged)
    # print(entities)

    fdist = FreqDist(text)
    print(fdist)
    print(fdist.most_common(10))
    print(fdist.freq('And'))


if __name__ == '__main__':
    main()
