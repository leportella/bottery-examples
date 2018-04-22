import re

from bottery.message import render
from bottery.platform import telegram

def pong(message):
    return 'pong'

# add message return that is case sensitive
def sensitive_message(message):
    return 'Hello!'

# message to reply any message starting with hi
def hi(message):
    return 'Hello, there!'

# add reply to last message
@telegram.reply()
def reply_message(message):
    return 'This is a reply response'

# add reply to previous message
@telegram.reply(lambda message: message.id - 1)
def reply_previous_message(message):
    return 'This is reply to another message'
