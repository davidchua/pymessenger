import os

from pymessenger.bot import Bot
from pymessenger import Element, Button

TOKEN = os.environ.get('TOKEN')
APP_SECRET = os.environ.get('APP_SECRET')

bot = Bot(TOKEN, app_secret=APP_SECRET)

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


def test_elements():
    image_url = 'https://lh4.googleusercontent.com/-dZ2LhrpNpxs/AAAAAAAAAAI/AAAAAAAA1os/qrf-VeTVJrg/s0-c-k-no-ns/photo.jpg'
    elements = []
    element = Element(title="Arsenal", image_url=image_url, subtitle="Click to go to Arsenal website.",
                      item_url="http://arsenal.com")
    elements.append(element)
    result = bot.send_generic_message(recipient_id, elements)
    assert type(result) is dict
    assert result.get('message_id') is not None
    assert result.get('recipient_id') is not None


def test_image_url():
    image_url = 'https://lh4.googleusercontent.com/-dZ2LhrpNpxs/AAAAAAAAAAI/AAAAAAAA1os/qrf-VeTVJrg/s0-c-k-no-ns/photo.jpg'
    result = bot.send_image_url(recipient_id, image_url)
    assert type(result) is dict
    assert result.get('message_id') is not None
    assert result.get('recipient_id') is not None
    
def test_image_gif_url():
    image_url = 'https://media.giphy.com/media/rl0FOxdz7CcxO/giphy.gif'
    result = bot.send_image_url(recipient_id, image_url)
    assert type(result) is dict
    assert result.get('message_id') is not None
    assert result.get('recipient_id') is not None


def test_button_message():
    buttons = []
    button = Button(title='Arsenal', type='web_url', url='http://arsenal.com')
    buttons.append(button)
    button = Button(title='Other', type='postback', payload='other')
    buttons.append(button)
    text = 'Select'
    result = bot.send_button_message(recipient_id, text, buttons)
    assert type(result) is dict
    assert result.get('message_id') is not None
    assert result.get('recipient_id') is not None


def test_fields_blank():
    user_profile = bot.get_user_info(recipient_id)
    assert user_profile is not None


def test_fields():
    fields = ['first_name', 'last_name']
    user_profile = bot.get_user_info(recipient_id, fields=fields)
    assert user_profile is not None
    assert len(user_profile.keys()) == len(fields)
