""" Created by Jieyi on 4/15/16. """

from urllib import request


class HTMLContentGetter:
    """
    Get the web html source content.
    """

    def __init__(self, url, decoder='utf8'):
        self._url = url
        self._decoder = decoder
        self._connection = None

    def obtain_content(self):
        self.__access()
        return self._connection.read().decode(self._decoder)

    def __access(self):
        """
        Open the url website and set the connection.
        """

        self._connection = request.urlopen(self._url)


def main():
    getter = HTMLContentGetter('https://en.wikipedia.org/wiki/Reinforcement_learning?oldformat=true')
    print(getter.obtain_content())


if __name__ == '__main__':
    main()
