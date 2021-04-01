from instapy import InstaPy
import os

insta_user = os.environ['bot_insta_user']
insta_password = os.environ['bot_insta_pwd']

InstaPy(username=insta_user, password=insta_password).login()
