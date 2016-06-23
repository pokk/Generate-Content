""" Created by wujieyi on 06/23/2016. """
import json

json_string = '''
{"created_at": "Sat Jan 11 16:17:12 +0000 2014", "default_profile": true, "default_profile_image": true, "favourites_count": 1, "followers_count": 4, "friends_count": 1, "id": 2286872491, "lang": "en", "name": "\u5433\u73a0\u5100", "profile_background_color": "C0DEED", "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", "profile_image_url": "http://abs.twimg.com/sticky/default_profile_images/default_profile_1_normal.png", "profile_link_color": "0084B4", "profile_sidebar_fill_color": "DDEEF6", "profile_text_color": "333333", "screen_name": "pokkbaby", "status": {"created_at": "Thu Jun 23 05:41:05 +0000 2016", "favorite_count": 1, "favorited": true, "hashtags": [], "id": 745854165516230657, "id_str": "745854165516230657", "lang": "en", "source": "<a href=\"https://github.com/pokk/Generate-Content\" rel=\"nofollow\">python-twitter-auto-generate</a>", "text": "This's awesome twitter!!!", "urls": [], "user_mentions": []}, "statuses_count": 2, "time_zone": "Taipei", "utc_offset": 28800}
'''

json_string2 = '{"first_name":"Guido","last_name":"Rossum"}'

j = json.loads(json_string)
print(j)


def main():
    print(json_string)


if __name__ == '__main__':
    main()
