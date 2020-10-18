# Imports
import random
import sqlite3
from datetime import datetime
from time import sleep

import praw

from keys import keys

# Database stuff...
sql_config = sqlite3.connect('database.db')
sql_con = sql_config.cursor()
sql_con.execute("CREATE TABLE IF NOT EXISTS 'users' (id INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT)")

# Users who got messaged already
users = []
for tempResult in sql_con.execute("SELECT `userName` FROM `users`"):
    users.append(tempResult[0])

# Calculation per 24h
messageEvery = 86400 / keys['messagesPerDay']  # Seconds in a day / Messages per day
print(f"Im gonna message a user every {messageEvery} seconds.")

# REST API connection
reddit = praw.Reddit(client_id=keys['client_id'],
                     client_secret=keys['client_secret'],
                     user_agent=keys['user_agent'],
                     username=keys['username'],
                     password=keys['password'])

# subreddit = reddit.subreddit("anxiety+mentalhealth+socialanxiety+Askpsychology")
subreddit = reddit.subreddit(keys['subreddit'])

for submission in subreddit.stream.submissions():
    if submission.author is not None and submission.selftext is not None:
        if submission.selftext != "[removed]" or submission.selftext != "[deleted]":
            if submission.author.name not in users:
                if "me" in submission.title.lower():
                    secondsOld = (datetime.utcnow() - datetime.fromtimestamp(
                        submission.created_utc)).total_seconds() / 60
                    pauseSeconds = random.randint(keys['pauseMinutes'][0] * 60, keys['pauseMinutes'][1] * 60)

                    if secondsOld > pauseSeconds:
                        print(f'{submission.author.name} made a new post.\n\tNot waiting since post is already old.')
                    else:
                        pauseSeconds -= secondsOld
                        print(
                            f'{submission.author.name} made a new post.\n\tWaiting for {pauseSeconds / 60} minutes to message.')

                    print(
                        f'{submission.author.name} made a new post.\n\tWaiting for {pauseSeconds / 60} minutes to message.')
                    sleep(pauseSeconds)
                    sql_con.execute(f"INSERT INTO users (userName) VALUES ('{submission.author.name}')")
                    users.append(submission.author_fullname)

                    submission.author.message(keys['title'], keys['message'])

                    print("Message Sent")
                    sql_config.commit()
                    print(f'Waiting another {(messageEvery - pauseSeconds) / 60} minutes to message and scan again.')
                    sleep(messageEvery - pauseSeconds)
