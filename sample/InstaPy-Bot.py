from instapy import InstaPy
import os

insta_user = os.environ['bot_insta_user']
insta_password = os.environ['bot_insta_pwd']

session = InstaPy(username=insta_user, password=insta_password, headless_browser=True)
session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.login()
session.set_use_clarifai(enabled=True, api_key='6169f55982c94286804d917f415aa670')
session.clarifai_check_img_for(['nsfw'])
session.set_relationship_bounds(enabled=True, max_followers=8500)
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
session.end()
