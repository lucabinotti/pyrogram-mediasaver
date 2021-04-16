import time
import threading
from pyrogram import Client,filters
from settings import *

app = Client(session_name=SESSION, api_id=API_ID, api_hash=API_HASH)

def send():
	total = 0
	while True:
		media = 0
		try:
			p = photo_ids.copy()
			v = video_ids.copy()
			for chat in p:
				for id in p[chat]:
					try:
						app.forward_messages(chat_id=GROUPS["photo"], from_chat_id=chat, message_ids=id)
						media += 1
					except:
						if ERROR_MESSAGES:
							print(f"The chat_id {GROUPS['photo']} is invalid. Check it and retry.")
					finally:
						photo_ids[chat].remove(id)
			for chat in v:
				for id in v[chat]:
					try:
						app.forward_messages(chat_id=GROUPS["video"], from_chat_id=chat, message_ids=video_ids[chat])
						media += 1
					except:
						if ERROR_MESSAGES:
							print(f"The chat_id {GROUPS['video']} is invalid. Check it and retry.")
					finally:
						video_ids[chat].remove(id)
			if media > 0:
				total += media
				if PRINT_MESSAGES:
					print(f"[SENT {media}. TOTAL {total}]")
			time.sleep(2)
		except BaseException as e:
			if ERROR_MESSAGES:
				print(e)


@app.on_message(filters.photo & ~filters.me)
async def save_photo(client, message):
	if not message.chat.id in BANNED_GROUPS:
		if message.chat.id in photo_ids:
			photo_ids[message.chat.id].append(message.message_id)
		else:
			photo_ids.update({message.chat.id: [message.message_id]})


@app.on_message(filters.video & ~filters.me)
async def save_video(client, message):
	if not message.chat.id in BANNED_GROUPS:
		if message.chat.id in video_ids:
			video_ids[message.chat.id].append(message.message_id)
		else:
			video_ids.update({message.chat.id: [message.message_id]})


if __name__ == "__main__":
	photo_ids = {}
	video_ids = {}
	thread = threading.Thread(target=send)
	thread.start()
	try:
		app.run()
		if PRINT_MESSAGES:
			print("[STARTING]")
	except:
		if ERROR_MESSAGES:
			print("Error on loading your Telegram account. Check your api_id and hash_id and retry.")
		exit()