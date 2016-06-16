""" Created by Jieyi on 6/16/16. """
import webbrowser

from requests_oauthlib import OAuth1Session

from twitter_function import REQUEST_TOKEN_URL, AUTHORIZATION_URL, ACCESS_TOKEN_URL, jieyi_consumer_key, jieyi_consumer_secret


class AccessToken:
    def __init__(self, consumer_key=None, consumer_secret=None):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret

    def get_token(self):
        oauth_client = OAuth1Session(self._consumer_key, client_secret=self._consumer_secret, callback_uri='oob')

        print('\nRequesting temp token from Twitter...\n')

        try:
            resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
        except ValueError as e:
            raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

        url = oauth_client.authorization_url(AUTHORIZATION_URL)

        print('I will try to start a browser to visit the following Twitter page '
              'if a browser will not start, copy the URL to your browser '
              'and retrieve the pincode to be used '
              'in the next step to obtaining an Authentication Token: \n'
              '\n\t{0}'.format(url))

        webbrowser.open(url)
        pincode = input('\nEnter your pincode? ')

        print('\nGenerating and signing request for an access token...\n')

        oauth_client = OAuth1Session(self._consumer_key, client_secret=self._consumer_secret,
                                     resource_owner_key=resp.get('oauth_token'),
                                     resource_owner_secret=resp.get('oauth_token_secret'),
                                     verifier=pincode)
        try:
            resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
        except ValueError as e:
            raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)

        print('''Your tokens/keys are as follows:
                consumer_key         = {ck}
                consumer_secret      = {cs}
                access_token_key     = {atk}
                access_token_secret  = {ats}'''.format(
            ck=self._consumer_key,
            cs=self._consumer_secret,
            atk=resp.get('oauth_token'),
            ats=resp.get('oauth_token_secret')))

        return resp.get('oauth_token'), resp.get('oauth_token_secret')


def main():
    at = AccessToken(jieyi_consumer_key, jieyi_consumer_secret)
    at.get_token()


if __name__ == '__main__':
    main()
