""" Created by Jieyi on 4/15/16. """

from urllib import request

from content.html_parser import WikiArticleParser


class HTMLContentGetter:
    """
    Get the web html source content.
    """

    def __init__(self, url, html_parser=None, decoder='utf8'):
        self._url = url
        self._parser = html_parser
        self._decoder = decoder
        self._connection = None

    def obtain_origin_content(self):
        """
        Get the website content of assignment url.

        :return: HTML all content or None.
        """

        if not self.__access():
            return None

        return self._connection.read().decode(self._decoder)

    def obtain_parsed_content(self, html_parser=None):
        """
        Using the html parser parses the content.

        :return: parsed content.
        """

        parser = html_parser if html_parser else self._parser
        if not parser:
            print("You didn't set a html_parser!!")
            return None

        parser.feed(self.obtain_origin_content())
        return ''.join(parser.content)

    def __access(self):
        """
        Open the url website and set the connection.

        :return: True or False, because of the url link.
        """

        if not self._url:
            print('You must input a url link.')
            return False

        self._connection = request.urlopen(self._url)
        return True


def main():
    getter = HTMLContentGetter('https://en.wikipedia.org/wiki/Markov')
    print(getter.obtain_parsed_content(WikiArticleParser()))


if __name__ == '__main__':
    main()
