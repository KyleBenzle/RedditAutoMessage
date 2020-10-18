# RedditAutoMessage
Automatically send a message to everyone who has posted in a given subReddit.

Reddit Auto Messager
Messages users that have posted to a given sub-Reddit Misuse of this script will probably lead to your account being banned.

Setup instructions
Instructions are for Linux.

Download Python 3.6 from the Python website here - https://www.python.org/downloads/

When installing, make sure you select "add python to PATH environment" or whatever that box is. I can't remember the exact wording, but it is something along those lines. You can just spam click "next" after checking that box.

After it is completed, open your command prompt and type in pip install praw and wait for it to install. Once it is installed you can close the command prompt.

Download this script by clicking on the green Clone or Download button, followed by Download ZIP. After it downloads, extract the Send New Message.py, Opt-in Comment Finder.py, config.py, and Subscriber List.db files anywhere you like. Make sure you keep them together in the same folder/directory.

If someone wishes to be removed from the messaging list, download DB Browser for SQLite here - http://sqlitebrowser.org/

Once downloaded and installed, open up Subscriber List.db using DB Browser. Once opened, click on Tables and there should be a dropdown menu just underneath the Tables tab. Select Subscribers in the dropdown menu. Next, start typing in the name of the person who wishes to be removed from the database in the Filter box that is directly underneath the Username column title, and they should appear. Click on their username and click Delete Record. Save the changes and then close the database.

If you cannot get the bot set up using these instructions or the bot crashes with an error message, head over to https://www.reddit.com/r/redditdev and make a text post there. Make sure you link this github page so that we can help you quicker and let us know what the problem is.
