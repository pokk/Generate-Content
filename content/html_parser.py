""" Created by Jieyi on 4/15/16. """
from html.parser import HTMLParser

from content.connection import HTMLContentGetter


class WikiHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    def error(self, message):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            print("Encountered a start tag:", tag)
            print('attrs', attrs)
            if ('role', 'note') in attrs:
                print('goooooooooooooood')
                # if tag == 'i':
                #     for (var, value) in attrs:
                #         if 'dp48' in value:
                #             self.divFound = True

                # def handle_endtag(self, tag):
                # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        # print(data)
        pass


def main():
    getter = HTMLContentGetter('https://en.wikipedia.org/wiki/Reinforcement_learning?oldformat=true')

    parser = WikiHTMLParser()
    parser.feed(getter.obtain_content())


if __name__ == '__main__':
    main()
