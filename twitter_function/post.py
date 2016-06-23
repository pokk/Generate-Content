""" Created by wujieyi on 06/23/2016. """

from twitter_function.login import Login


class Post:
    """
    Twitter's vary post function.
    """

    def __init__(self, twitter_holder):
        self._api = twitter_holder

    def post_plain_text(self, text):
        return self._api.PostUpdate(text)

    def show_posts(self, user_name):
        return self._api.GetUserTimeline(screen_name=user_name)

    def show_assign_post(self, id):
        pass


def main():
    p = Post(Login(jieyi_consumer_key, jieyi_consumer_secret, jieyi_access_token_key, jieyi_access_token_secret).login())
    # p.post_plain_text("Now is a good time!")

    print(p.show_posts('pokkbaby'))

    # Login(jieyi_consumer_key, jieyi_consumer_secret, jieyi_access_token_key, jieyi_access_token_secret).login()


if __name__ == '__main__':
    main()
