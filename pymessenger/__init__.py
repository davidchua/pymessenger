import json

from .bot import Bot

class Element(object):

    __acceptable_keys = ['title', 'item_url', 'image_url', 'subtitle']
    def __init__(self, **kwargs):
        for key in self.__acceptable_keys:
            setattr(self, key, kwargs.get(key))

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        data = {}
        for key in self.__acceptable_keys:
            data[key] = getattr(self, key)
        return data

    def __repr__(self):
        return self.to_json()
