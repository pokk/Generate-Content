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

    def show_posts(self, user_name, count=20):
        return self._api.GetUserTimeline(screen_name=user_name, count=count)

    def show_specific_post(self, user_name, post_id):
        res = [list_post for list_post in self.show_posts(user_name, count=200) if list_post.AsDict()['id'] == post_id]
        return res[0] if len(res) > 0 else None


def main():
    p = Post(Login(jieyi_consumer_key, jieyi_consumer_secret, jieyi_access_token_key, jieyi_access_token_secret).login())
    # p.post_plain_text("Now is a good time!")

    for s in p.show_posts('pokkbaby'):
        print(s.AsDict()['id'])

    print(p.show_specific_post('pokkbaby', 745868719369388032))

if __name__ == '__main__':
    main()
