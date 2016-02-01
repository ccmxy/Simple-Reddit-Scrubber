import sys, re, praw, pprint

REDDIT_NAME = "yourRedditUsername"
REDDIT_PASSWORD = "yourRedditPassword"
COMMENT_DELETE_LIMIT = 1000

user_agent = ("Reddit scrubber 1.0 by /u/ccmxy")
r = praw.Reddit(user_agent=user_agent)
r.login(REDDIT_NAME, REDDIT_PASSWORD, disable_warning=True)

user_name = REDDIT_NAME
user = r.get_redditor(user_name)
commentsGen = user.get_comments(limit=COMMENT_DELETE_LIMIT)
for comment in commentsGen:
    comment.delete()
