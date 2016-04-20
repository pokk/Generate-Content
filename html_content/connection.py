""" Created by Jieyi on 4/15/16. """

from urllib import request

from html_content.html_parser import WikiArticleParser


class HTMLContentGetter:
    """
    Get the web html source html_content.
    """

    def __init__(self, url, decoder='utf8'):
        self._url = url
        self._decoder = decoder
        self._connection = None

    def obtain_content(self, html_parser=None):
        """
        Using the html parser parses the html_content.

        :return: parsed html_content.
        """

        if html_parser:
            html_parser.feed(self.__get_content())
            return ''.join(html_parser.content)
        else:
            return self.__get_content()

    def __get_content(self):
        """
        Get the website html_content of assignment url.

        :return: HTML all html_content or None.
        """

        if not self.__access():
            return None

        return self._connection.read().decode(self._decoder)

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
    print(getter.obtain_content(WikiArticleParser()))


if __name__ == '__main__':
    main()
