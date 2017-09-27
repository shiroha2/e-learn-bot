# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/mipvEmv6xQI4Lbq6mlpnzkWAoHhQ1Pz0oJbAuEMHvVERFIR9hoHnT9nB1s0kFGSGiFuFnB4arklqboD6RwaaGNXecEUFxgukTMIN5S6NU7Pg5QESAhkJjqM5R/2ir98qWdaVkA6tBAW07FdXcPBmAdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('e8d5d48138452b28f8b1001c2d9c1bbb') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
