import json

from .bot import Bot

class Element(dict):
    __acceptable_keys = ['title', 'item_url', 'image_url', 'subtitle']
    def __init__(self, *args, **kwargs):
        kwargs = {k:v for k, v in kwargs.iteritems() if k in self.__acceptable_keys}
        super(Element, self).__init__(*args, **kwargs)

    def to_json(self):
        return json.dumps({k:v for k, v in self.iteritems() if k in self.__acceptable_keys})
