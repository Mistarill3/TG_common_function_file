import json
import requests



def send_message(token, chat_id, message_thread_id, message_text):
    print(f"== send_message, chat_id: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "text": message_text,
        "parse_mode": "HTML",
        "link_preview_options": {
            "is_disabled": True
        },
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def send_dice(token, chat_id, message_thread_id, dice_emoji):
    print(f"== send_dice, chat_id: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/sendDice"

    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "emoji": dice_emoji,
        "parse_mode": "HTML",
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def send_sticker(token, chat_id, message_thread_id, sticker_file_id):
    print(f"== send_sticker, chat_id: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/sendSticker"

    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "sticker": sticker_file_id,
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def send_photo(token, chat_id, message_thread_id, file_id):
    print(f"== send_photo, chat_id: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/sendPhoto"

    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "photo": file_id,
        "has_spoiler":True,
        "disable_notification": True,
        "protect_content": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def edit_message_text(token, chat_id, message_id, message_text):
    print(f"== edit_message_text, chat_id: {chat_id}, message_id: {message_id}")

    url = f"https://api.telegram.org/bot{token}/editMessageText"

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": message_text,
        "parse_mode": "HTML",
        "link_preview_options": {
            "is_disabled": True
        },
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def delete_message(token, chat_id, message_id):
    print(f"== delete_message, chat_id: {chat_id}, message_id: {message_id}")

    url = f"https://api.telegram.org/bot{token}/deleteMessage"

    payload = {
        "chat_id": str(chat_id),
        "message_id": str(message_id),
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def delete_messages(token, chat_id, message_ids):
    print(f"== delete_message, chat_id: {chat_id}, message_ids: {message_ids}")

    url = f"https://api.telegram.org/bot{token}/deleteMessages"

    payload = {
        "chat_id": chat_id,
        "message_ids": message_ids,
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def forward_message(token, chat_id, message_thread_id, from_chat_id, message_id):
    print(f"== forward_message, chatId: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/forwardMessage"

    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "from_chat_id": from_chat_id,
        "message_id": message_id,
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def pin_chat_message(token, chat_id, message_id):
    print(f"== pin_chat_message, chat_id: {chat_id}, message_id: {message_id}")

    url = f"https://api.telegram.org/bot{token}/pinChatMessage"

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def unpin_chat_message(token, chat_id, message_id):
    print(f"== unpin_chat_message, chat_id: {chat_id}, message_id: {message_id}")

    url = f"https://api.telegram.org/bot{token}/unpinChatMessage"

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def reopen_forum_topic(token, chat_id, message_thread_id):
    print(f"== reopen_forum_topic, chat_id: {chat_id}, message_thread_id: {message_thread_id}")

    url = f"https://api.telegram.org/bot{token}/reopenForumTopic"
    
    payload = {
        "chat_id": chat_id,
        "message_thread_id": message_thread_id,
        "disable_notification": True
    }

    try:
        response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
        if response.json() is None:
            print("response.json() is undefined")
            return None
        else:
            print("== response.data", response.json())
        return response.json()
    except requests.exceptions.RequestException as error:
        if error.response:
            print("== error.response:", error.response.json())
            return error.response.json()
        else:
            print("== error.message", str(error))
        print("== error.config:", response.request)
        return None



def open_url_json_response(url):
    print("== open_url_json_response")

    try:
        response = requests.get(url)
        response.raise_for_status()

        response_json = response.json()
        print(json.dumps(response_json))
        return response_json

    except requests.exceptions.HTTPError as e:
        print("== except")
        print(f"{response.status_code}: {response.reason}")
        
        if response.status_code in (400, 403, 404, 429):
            return
        else:
            raise Exception(f"HTTPError code: {response.status_code}, reason: {response.reason}")
