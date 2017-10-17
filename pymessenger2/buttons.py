import attr


@attr.s
class PostbackButton(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/postback-button
    """
    title = attr.ib()
    payload = attr.ib(default=None)
    type = attr.ib(default='postback')

    def __attrs_post_init__(self):
        assert self.type == 'postback', 'Type of a button can\'t be set ' \
                                        'manually.'
        if not self.payload:
            self.payload = self.title

@attr.s
class CallButton(object):
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
class URLButton(object):
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
class ShareButton(object):
    """
    See https://developers.facebook.com/docs/messenger-platform/send-api-reference/share-button
    """
    type = attr.ib(default='element_share')

    def __attrs_post_init__(self):
        assert self.type == 'element_share', 'Type of a button can\'t be set ' \
                                             'manually.'
