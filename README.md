# Instagram-Bot
A simple bot that is able to log into an instagram account. There is two approaches that achieve the same functionally:
<ul>
  <li>Selinium</li>
  <li>InstaPy</li>
</ul>

## Selinium Approach
A simple bot that is able to log into an instagram account.

### Prerequisites
The following must be installed for the selinium approach:
<ul>
  <li>Selinium</li>
  <li>Geckodriver</li>
</ul>

The login details must be mapped to the following variables in the unix bash profile (.bashrc):
<ul>
 <li>Username -> bot_insta_user</li>
 <li>Password -> bot_insta_pwd</li>
</ul>

### How to use
Run the Selinium-Bot.py file in the sample folder to run the Page Object Pattern test. This opens the browser and logs into the specified users account.

### Further improvements
This could be expanded further to include the following:
<ul>
 <li>Searching for posts on a users feed.</li>
 <li>Finding posts according to hashtags.</li>
 <li>Liking and commenting on posts.</li>
 <li>Posting on the users profile.</li>
 <li>Posting on the users story.</li>
</ul>

## InstaPy Approach
A simple bot that is able to do the following:
<ul>
 <li>Login to provided instagram account.</li>
 <li>Find posts according to hashtags.</li>
 <li>Filter posts out according to follower count, AI analysis of photos and description/ hashtag exclusion.</li>
 <li>Like and comment on posts.</li>
 <li>Follow accouts associated to these posts.</li>
</ul>

### Prerequisites
The following must be installed for the InstaPy approach:
<ul>
  <li>InstaPy</li>
</ul>

The login details must be mapped to the following variables in the unix bash profile (.bashrc):
<ul>
 <li>Username -> bot_insta_user</li>
 <li>Password -> bot_insta_pwd</li>
</ul>

### How to use
Run the InstaPy-Bot.py file in the sample folder to run script. This opens the a headless browser which doesn't display the UI aspect.

### Further improvements
This could be expanded further to include the following:
<ul>
 <li>Deeper analysis of posts</li>
 <li>Posting on the users profile</li>
 <li>Posting on the users story</li>
</ul>
