from bottery import handlers

import views


msghandlers = [
    handlers.message('ping', views.pong),
    handlers.startswith('hi', views.hi),
    handlers.message('Hello', views.sensitive_message, case_sensitive=True),
    handlers.message('reply', views.reply_message),
    handlers.message('another_reply', views.reply_previous_message),
]
