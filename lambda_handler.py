import os
import json
import urllib.parse

import ypsilon_function
import sendHttpRequest

token = os.environ["TELEGRAM_BOT_TOKEN"] #合いの手Bot


def lambda_handler(event, context):
    print("==startLambdaHandler")

    #BotがWebHookで呼ばれるときはアクティブにする
    #print("==event")
    #print(json.dumps(event))
    #body = event["body"]
    #print("==body")
    #print(json.dumps(json.loads(body)))
    
    returnData =  {
        "statusCode": 200
    }

    try:
        ypsilon_function.ypsilon_handler(event, context, token)
        
    except Exception:
        import traceback
        traceback.print_exc()
        
        #エラー通知を投げる
        chatId = os.environ["TELEGRAM_CHAT_ID_FOR_ERRORMESSAGE"]
        messageText = "XXX-functionがエラー吐いてまーす"
        
        sendHttpRequest.sendMessage(token, chatId, messageText)

    print("==endLamdaHandler")
    print(returnData)
    return returnData
