def get_message_thread_id(user_message):
    print("== get_message_thread_id")

    if user_message.get("is_topic_message", False) and "message_thread_id" in user_message:
        message_thread_id: int = user_message["message_thread_id"]
    else:
        message_thread_id = 0

    return message_thread_id
