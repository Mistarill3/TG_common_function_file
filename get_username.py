def get_username(user_message):
    print("== get_username")

    if "username" in user_message["from"]:
        username: str = user_message["from"]["username"]
    elif "username" not in user_message["from"] and "first_name" in user_message["from"]:
        username = "'" + user_message["from"]["first_name"] + "'"
    elif "username" not in user_message["from"] and "first_name" not in user_message["from"] and "last_name" in user_message["from"]:
        username = "'" + user_message["from"]["last_name"] + "'"
    else:
        username = ""

    return username
