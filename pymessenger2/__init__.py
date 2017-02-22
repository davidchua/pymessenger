from .bot import Bot
from .utils import ToJsonMixin

from .buttons import *


@attr.s
class Element(ToJsonMixin):
    title = attr.ib()
    item_url = attr.ib(default=None)
    image_url = attr.ib(default=None)
    subtitle = attr.ib(default=None)
    buttons = attr.ib(default=None)


@attr.s
class QuickReply(ToJsonMixin):
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
