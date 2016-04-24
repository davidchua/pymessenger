import requests
import json

class Bot:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v2.6/me/messages?access_token={0}".format(access_token)

    def send_text_message(self, recipient_id, message):
        payload = {'recipient': {'id': recipient_id},
                   'message': {'text': message}
                  }
        return requests.post(self.base_url, json=payload).json()

    def send_message(self, recipient_id, message):
        payload ={'recipient': {'id': recipient_id},
                  'message': message
                 }
        return requests.post(self.base_url, json=payload).json()

    def send_generic_message(self, recipient_id, elements):
        payload = {'recipient': {'id': recipient_id},
                   'message': { "attachment": {
                                "type": "template",
                                "payload": {
                                    "template_type": "generic",
                                    "elements": elements
                                    }
                                }
                              }
                   }
        return requests.post(self.base_url, json=payload).json()
