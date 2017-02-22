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


class Button(ToJsonMixin):
    # TODO: Decide if this should do more
    pass


# class Receipt:
#     pass
