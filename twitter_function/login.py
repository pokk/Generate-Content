""" Created by Jieyi on 6/16/16. """

import twitter


class Login:
    def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token_key = access_token_key
        self._access_token_secret = access_token_secret

    def login(self):
        return twitter.Api(consumer_key=self._consumer_key,
                           consumer_secret=self._consumer_secret,
                           access_token_key=self._access_token_key,
                           access_token_secret=self._access_token_secret)


def main():
    print()


if __name__ == '__main__':
    main()
