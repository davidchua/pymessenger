import json
class Element:

    __acceptable_keys_list = ['title', 'item_url', 'image_url', 'subtitle']
    def __init__(self, **kwargs):
#        ipdb.set_trace()
        [self.__setattr__(key, kwargs.get(key)) for key in self.__acceptable_keys_list]

    def to_json(self):
        data = {
                "title": self.title,
                "item_url": self.item_url,
                "image_url": self.image_url,
                "subtitle": self.subtitle
                }
        return json.dumps(data)

