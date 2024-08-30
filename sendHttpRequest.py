import json
import urllib.parse
import urllib.request
import urllib.error


def sendMessage(token, chatId, messageThreadId, messageText):
    print("==startSendHttpRequest.py sendMessage")

    messageText_quote = urllib.parse.quote(messageText)
    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&text={text}&disable_notification=True".format(token=token, chatId=chatId, text=messageText_quote)
    else:
        url = "https://api.telegram.org/bot{token}/sendMessage?chat_id={chatId}&message_thread_id={messageThreadId}&text={text}&disable_notification=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, text=messageText_quote)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def sendDice(token, chatId, messageThreadId, diceEmoji):
    print("==startSendHttpRequest.pysSendDice")

    diceEmoji_quote = urllib.parse.quote(diceEmoji)
    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendDice?chat_id={chatId}&emoji={emoji}&disable_notification=True".format(token=token, chatId=chatId, emoji=diceEmoji_quote)
    else:
        url = "https://api.telegram.org/bot{token}/sendDice?chat_id={chatId}&message_thread_id={messageThreadId}&emoji={emoji}&disable_notification=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, emoji=diceEmoji_quote)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def sendSticker(token, chatId, messageThreadId, stickerFileId):
    print("==startSendHttpRequest.py sendSticker")

    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendSticker?chat_id={chatId}&sticker={sticker}&disable_notification=True".format(token=token, chatId=chatId, sticker=stickerFileId)
    else:
        url = "https://api.telegram.org/bot{token}/sendSticker?chat_id={chatId}&message_thread_id={messageThreadId}&sticker={sticker}&disable_notification=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, sticker=stickerFileId)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def sendPhoto(token, chatId, messageThreadId, fileId):
    print("==startSendHttpRequest.py sendPhoto")

    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendPhoto?chat_id={chatId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, fileId=fileId)
    else:
        url = "https://api.telegram.org/bot{token}/sendPhoto?chat_id={chatId}&message_thread_id={messageThreadId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, fileId=fileId)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def sendVideo(token, chatId, messageThreadId, fileId):
    print("==startSendHttpRequest.py sendVideo")

    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendVideo?chat_id={chatId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, fileId=fileId)
    else:
        url = "https://api.telegram.org/bot{token}/sendVideo?chat_id={chatId}&message_thread_id={messageThreadId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, fileId=fileId)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def sendAnimation(token, chatId, messageThreadId, fileId):
    print("==startSendHttpRequest.py sendAnimation")

    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/sendAnimation?chat_id={chatId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, fileId=fileId)
    else:
        url = "https://api.telegram.org/bot{token}/sendAnimation?chat_id={chatId}&message_thread_id={messageThreadId}&photo={fileId}&disable_notification=True&has_spoiler=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, fileId=fileId)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def editMessageText(token, chatId, messageThreadId, messageId, messageText):
    print("==startSendHttpRequest.py editMessage")

    messageText_quote = urllib.parse.quote(messageText)
    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/editMessageText?chat_id={chatId}&message_id={messageId}&text={text}&disable_notification=True".format(token=token, chatId=chatId, messageId=messageId, text=messageText_quote)
    else:
        url = "https://api.telegram.org/bot{token}/editMessageText?chat_id={chatId}&message_thread_id={messageThreadId}&message_id={messageId}&text={text}&disable_notification=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId, messageId=messageId, text=messageText_quote)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def deleteMessage(token, chatId, messageId):
    print("==startSendHttpRequest.py deleteMessage")

    url = "https://api.telegram.org/bot{token}/deleteMessage?chat_id={chatId}&message_id={messageId}&disable_notification=True".format(token=token, chatId=chatId, messageId=messageId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            print(resBody)
            return
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def forwardMessage(token, chatId, messageThreadId, fromChatId, messageId):
    print("==startSendHttpRequest.py forwardMessage")

    if messageThreadId is None:
        url = "https://api.telegram.org/bot{token}/forwardMessage?from_chat_id={fromChatId}&message_id={messageId}&chat_id={chatId}&disable_notification=True".format(token=token, fromChatId=fromChatId, messageId=messageId, chatId=chatId)
    else:
        url = "https://api.telegram.org/bot{token}/forwardMessage?from_chat_id={fromChatId}&message_id={messageId}&chat_id={chatId}&message_thread_id{messageThreadId}&disable_notification=True".format(token=token, fromChatId=fromChatId, messageId=messageId, chatId=chatId, messageThreadId=messageThreadId)

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def pinChatMessage(token, chatId, messageId):
    print("==startSendHttpRequest.py pinChatMessage")

    url = "https://api.telegram.org/bot{token}/pinChatMessage?chat_id={chatId}&message_id={messageId}&disable_notification=True".format(token=token, chatId=chatId, messageId=messageId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            print(resBody)
            return
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def unpinChatMessage(token, chatId, messageId):
    print("==startSendHttpRequest.py unpinChatMessage")

    url = "https://api.telegram.org/bot{token}/unpinChatMessage?chat_id={chatId}&message_id={messageId}&disable_notification=True".format(token=token, chatId=chatId, messageId=messageId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            print(resBody)
            return
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def reopenForumTopic(token, chatId, messageThreadId):
    print("==startSendHttpRequest.py reopenForumTopic")

    url = "https://api.telegram.org/bot{token}/reopenForumTopic?chat_id={chatId}&message_thread_id={messageThreadId}&disable_notification=True".format(token=token, chatId=chatId, messageThreadId=messageThreadId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            print(resBody)

    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def getChat(token, chatId):
    print("==startSendHttpRequest.py getChat")

    url = "https://api.telegram.org/bot{token}/getChat?chat_id={chatId}".format(token=token, chatId=chatId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def getChatMemberCount(token, chatId):
    print("==startSendHttpRequest.py getChatMemberCount")

    url = "https://api.telegram.org/bot{token}/getChatMemberCount?chat_id={chatId}".format(token=token, chatId=chatId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def getChatMember(token, chatId, userId):
    print("==startSendHttpRequest.py getChatMember")

    url = "https://api.telegram.org/bot{token}/getChatMember?chat_id={chatId}&user_id={userId}".format(token=token, chatId=chatId, userId=userId)
    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            resBody_json = {"ok":False,"error_code":e.code,"description":e.reason}
            return resBody_json
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)



def openUrlJsonResponse(url):
    print("==startSendHttpRequest.py openUrlJsonResponse")

    try:
        with urllib.request.urlopen(url) as response:
            resBody = response.read()
            resBody_json = json.loads(resBody)
            print(json.dumps(resBody_json))
            return resBody_json
        
    except urllib.error.HTTPError as e:
        print("==except")
        print(str(e.code) + ": " + e.reason)
        if e.code in (400, 403, 404, 429):
        #if e.code == 400 or e.code == 403 or e.code == 404 or e.code == 429:
            return
        else:
            raise Exception("HTTPError code: " + str(e.code) + ", reason: " + e.reason)
