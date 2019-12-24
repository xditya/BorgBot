.eval NO_OF_SCSS = 5
for I in range(NO_OF_SCSS):
  await event.client(functions.messages.SendScreenshotNotificationRequest(peer=event.chat_id, reply_to_msg_id=42))
await event.delete()
