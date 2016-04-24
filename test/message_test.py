import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from pymessenger.bot import Bot as PyBot
from pymessenger import Element

TOKEN = os.environ.get('TOKEN')
bot = PyBot(TOKEN)
recipient_id = os.environ.get('RECIPIENT_ID')

def test_wrong_format_message():
    result = bot.send_text_message(recipient_id, {'text': "its a test"})
    assert type(result) is dict
    assert result.get('message_id') is None

def test_text_message():
    result = bot.send_text_message(recipient_id, "test")
    assert type(result) is dict
    assert result.get('message_id') is not None
    assert result.get('recipient_id') is not None
