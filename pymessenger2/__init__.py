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
