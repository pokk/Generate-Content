""" Created by Jieyi on 4/15/16. """
from enum import Enum
from html.parser import HTMLParser


class HtmlTag(Enum):
    """
    HTML tag enumerator.
    """

    DIV = 'div'
    ID = 'id'


class HtmlTagClass(Enum):
    """
    Class name of the HTML tag.
    """

    ID_WIKI_CONTENT = 'mw-content-text'


class WikiArticleParser(HTMLParser):
    """
    HTML parser for wiki article.  After parse the html_content, you
    can get the article from wiki.
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self._is_content_tag = False
        self._div_count = 0
        self._content = []

    def handle_starttag(self, tag, attrs):
        """
        The action of this parser parses each tags of beginning.

        :param tag: HTML tag.
        :param attrs: tag's attributes.
        :return: none
        """

        if tag == HtmlTag.DIV.value:
            if (HtmlTag.ID.value, HtmlTagClass.ID_WIKI_CONTENT.value) in attrs:
                self._is_content_tag = True
            # Count the number of tag div inside div we want to parse.
            if self._is_content_tag:
                self._div_count += 1

    def handle_endtag(self, tag):
        """
        The action of this parser parses each tags of ending.

        :param tag: HTML tag.
        :return: none
        """

        if tag == HtmlTag.DIV.value:
            # Catch the tag ending.
            if self._is_content_tag and self._div_count > 0:
                self._div_count -= 1
            if self._div_count == 0:
                self._is_content_tag = False

    def handle_data(self, data):
        """
        The action of this parser parsed the tag.

        :param data: inside of the tag's data.
        :return: none
        """

        if self._is_content_tag:
            self._content.append(data)

    def error(self, message):
        print('Error happened:', message)

    @property
    def content(self):
        # Tuple of ('', '\n', '\n\n', '\n\n\n'). They are redundant string in the article.
        new_line_set = tuple('\n' * times for times in range(4))

        while True:
            # Delete the front of article.
            if self._content[0] in new_line_set:
                del self._content[0]
            # Delete the back of article.
            if self._content[-1] in new_line_set:
                del self._content[-1]
            if all(s != new_line for s in (self._content[0], self._content[-1]) for new_line in new_line_set):
                break

        return self._content


def main():
    content = ''

    parser = WikiArticleParser()
    parser.feed(content)
    print(parser.content)
    # print(''.join(parser.html_content))
    parser.close()


if __name__ == '__main__':
    main()
