""" Created by Jieyi on 6/16/16. """

import twitter

from twitter_function import jieyi_consumer_key, jieyi_consumer_secret

api = twitter.Api(consumer_key=jieyi_consumer_key,
                  consumer_secret=jieyi_consumer_secret,
                  access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                  access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# users = api.GetFriends()
# print([u.screen_name for u in users])

# This is message, not post.
# p = api.PostDirectMessage("Hello! This is my first time to use twitter. It seems cool!", screen_name='pokkbaby')

# This is post to twitter.
p = api.PostUpdate("aaaaaaaaaaaaaaaaaaawesome!!!!")


# p = api.GetUser(screen_name='pokkbaby')
# 
# j = json.loads(p.AsJsonString())
# 
# print(j['status'])
# 
# print(j['status']['favorite_count'] if 'favorite_count' in j['status'].keys() else 'false')


def main():
    print()


if __name__ == '__main__':
    main()
