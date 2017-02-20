import json
import six

from .bot import Bot


class Element(dict):
    __acceptable_keys = ['title', 'item_url', 'image_url', 'subtitle', 'buttons']

    def __init__(self, *args, **kwargs):
        if six.PY2:
            kwargs = {k: v for k, v in kwargs.iteritems() if k in self.__acceptable_keys}
        else:
            kwargs = {k: v for k, v in kwargs.items() if k in self.__acceptable_keys}
        super(Element, self).__init__(*args, **kwargs)

    def to_json(self):
        return json.dumps({k: v for k, v in self.iteritems() if k in self.__acceptable_keys})


class Button(dict):
    # TODO: Decide if this should do more
    pass

# class Receipt:
#     pass
