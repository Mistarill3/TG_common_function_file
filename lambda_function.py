import os

import ypsilon_function
import send_http_request

token = os.environ["TELEGRAM_BOT_TOKEN"]


def lambda_handler(event, context):
    print("== startLambdaHandler")

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
        chat_id = os.environ["TELEGRAM_CHAT_ID_FOR_ERRORMESSAGE"]
        message_text = "XXX-functionがエラー出してます"
        
        send_http_request.send_message(token, chat_id, message_text)

    print("== endLamdaHandler")
    print(returnData)
    return returnData
