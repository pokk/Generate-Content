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
        """
        Get the website content of assignment url.

        :return: HTML all content or None.
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
    getter = HTMLContentGetter(None)
    print(getter.obtain_content())


if __name__ == '__main__':
    main()
