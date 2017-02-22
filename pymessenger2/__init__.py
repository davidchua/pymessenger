import json

import six

import attr

from .bot import Bot


class ToJsonMixin:
    """
    Derive from this with an `.asdict` member to get a working `to_json` 
    function!
    """
    def to_json(self):
        items_iterator = (attr.asdict(self).items()
                          if six.PY3 else
                          attr.asdict(self).iteritems())
        return json.dumps({k: v for k, v in items_iterator if v is not None})


@attr.s
class Element(ToJsonMixin):
    title = attr.ib()
    item_url = attr.ib(default=None)
    image_url = attr.ib(default=None)
    subtitle = attr.ib(default=None)
    buttons = attr.ib(default=None)


@attr.s
class PostbackButton(ToJsonMixin):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/postback-button
    """
    title = attr.ib()
    payload = attr.ib()
    type = attr.ib(default='postback')

    def __attrs_post_init__(self):
        assert self.type == 'postback', 'Type of a button can\'t be set ' \
                                        'manually.'


@attr.s
class CallButton(ToJsonMixin):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/postback-button
    """
    title = attr.ib()
    payload = attr.ib(convert=str)
    type = attr.ib(default='phone_number')

    def __attrs_post_init__(self):
        assert self.type == 'phone_number', 'Type of a button can\'t be set ' \
                                            'manually.'

        self.payload = self.payload.replace(' ', '')
        assert self.payload.startswith('+'), 'Payload must be a phone number ' \
                                             'with a valid country code.'
        assert self.payload[1:].isnumeric(), \
            'Payload must be a phone number.'


@attr.s
class URLButton(ToJsonMixin):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/url-button
    """
    title = attr.ib()
    url = attr.ib()
    webview_height_ratio = attr.ib(default='full')
    messenger_extensions = attr.ib(default=None)
    fallback_url = attr.ib(default=None)
    type = attr.ib(default='web_url')

    def __attrs_post_init__(self):
        assert self.type == 'web_url', 'Type of a button can\'t be set ' \
                                       'manually.'


@attr.s
class ShareButton(ToJsonMixin):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/share-button
    """
    type = attr.ib(default='element_share')

    def __attrs_post_init__(self):
        assert self.type == 'element_share', 'Type of a button can\'t be set ' \
                                             'manually.'
