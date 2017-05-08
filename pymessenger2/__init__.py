from .bot import Bot

from .buttons import *
from .airline import *


@attr.s
class Template(object):
    payload = attr.ib()
    type = attr.ib(default='template')


@attr.s
class Element(object):
    title = attr.ib()
    item_url = attr.ib(default=None)
    image_url = attr.ib(default=None)
    subtitle = attr.ib(default=None)
    buttons = attr.ib(default=None)


@attr.s
class QuickReply(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/quick-replies

    You may not give the payload and it'll be set to your title automatically.
    """
    content_type = attr.ib()
    title = attr.ib(default=None)
    payload = attr.ib(default=None)
    image_url = attr.ib(default=None)

    def __attrs_post_init__(self):
        assert self.content_type in {'text', 'location'}
        assert self.content_type == 'location' or self.title

        if not self.payload:
            self.payload = self.title


@attr.s
class ListElement(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/list-template
    """
    title = attr.ib()
    subtitle = attr.ib(default=None)
    image_url = attr.ib(default=None)
    default_action = attr.ib(default=None)
    buttons = attr.ib(default=None)  # Only one button allowed though
