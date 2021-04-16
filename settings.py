__author__ = "Luca Binotti"


# You must insert your API_ID, API_HASH.
# Visit https://my.telegram.org/apps and
# log in with your Telegram Account.
# SESSION can be left by default.
API_ID = 0
API_HASH = ""
SESSION = "pyrogram-session"

# You can chose on witch chat you want to send
# the media that you receive. You can set it
# with a chat id, or with "me" if you want to
# send it in your "Saved Messages".
# (chat_ids always start with -)
GROUPS = {"photo": "me",
          "video": "me"}

# You can chose to not save media from specific chats.
# In case, insert chat_ids in this list.
BANNED_GROUPS = []

# You can chose if you want a message printed on
# the screen every time a media is sent
PRINT_MESSAGES = False

# You can chose if you want error messages printed
# on the screen.
# Recommended option: True
ERROR_MESSAGES = True
