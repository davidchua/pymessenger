import json
import requests
from requests_toolbelt import MultipartEncoder

DEFAULT_API_VERSION = 2.6

class SendApiClient(object):
    def __init__(self, access_token, api_version=DEFAULT_API_VERSION):
        self.api_version = api_version
        self.access_token = access_token
        self.base_url = (
            "https://graph.facebook.com"
            "/v{0}/me/messages?access_token={1}"
        ).format(self.api_version, access_token)

    def send(self, recipient_id, message_type, **kwargs):
        if message_type == 'text':
            message_text = kwargs['text']
            response = self.send_text_message(recipient_id, message_text)
        elif message_type == 'button':
            message_text = kwargs['text']
            buttons = kwargs['buttons']
            response = self.send_button_message(recipient_id, message_text, buttons)
        else:
            response = "Message type {0} currently unsupported.".format(message_type)

        return response

    def send_text_message(self, recipient_id, message_text):
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                'text': message_text
            }
        }
        return self._send_payload(payload)

    def send_message(self, recipient_id, message):
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': message
        }
        return self._send_payload(payload)

    def send_generic_message(self, recipient_id, elements):
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                    }
                }
            }
        }
        return self._send_payload(payload)

    def send_button_message(self, recipient_id, text, buttons):
        payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": text,
                        "buttons": buttons
                    }
                }
            }
        }
        return self._send_payload(payload)

    def _send_payload(self, payload):
        result = requests.post(self.base_url, json=payload).json()
        return result

    def send_image(self, recipient_id, image_path):
        '''
            This sends an image to the specified recipient.
            Input:
              recipient_id: recipient id to send to
              image_path: path to image to be sent
            Output:
              Response from API as <dict>
        '''
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'image',
                        'payload': {}
                    }
                }
            ),
            'filedata': (image_path, open(image_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.base_url, data=multipart_data, headers=multipart_header).json()

    def send_image_url(self, recipient_id, image_url):
        payload = {
            'recipient': json.dumps(
                {
                    'id': recipient_id
                }
            ),
            'message': json.dumps(
                {
                    'attachment': {
                        'type': 'image',
                        'payload': {
                            'url': image_url
                        }
                    }
                }
            )
        }
        return self._send_payload(payload)
