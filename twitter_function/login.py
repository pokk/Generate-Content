""" Created by Jieyi on 6/16/16. """
import twitter

api = twitter.Api(consumer_key='45NS2K27oAtydjlGbjwTt5TPB',
                  consumer_secret='EjXg23xzZpdV5RH3XTd2V1RAxmZj51zxiJEsPk3UGcyRaOkQBA',
                  access_token_key='2286872491-F6d3ve84M4CAg1vAQWu52yhqWwVPGbqtkRNYYIP',
                  access_token_secret='3RWGJ8ZaotvBPrCrnM0ZMxB37bmddM4uZA0CI4u7dQR4O')

users = api.GetFriends()

print([u.screen_name for u in users])


def main():
    print("Hello Python!")


if __name__ == '__main__':
    main()
