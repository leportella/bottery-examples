from bottery.conf.patterns import DefaultPattern, Pattern
from bottery.message import render
from bottery.views import ping


def hello(message):
    return render(message, 'hello.md')


def not_found(message):
    return "Sorry, I didn't understand you :/"


patterns = [
    Pattern('ping', ping),
    Pattern('hello', hello),
    DefaultPattern(not_found),
]
