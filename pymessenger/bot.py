import requests
import json

class Bot:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/v2.6/me/messages?access_token={0}".format(access_token)

    def send_text_message(self, recipient_id, message):
        recipient = {
                "id": recipient_id
                }
        message = {
                "text": message
                }
        payload ={}
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.base_url, data=(payload)).json()

    def send_message(self, recipient_id, message):
        recipient = {
                "id": recipient_id
                }
        payload ={}
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        return requests.post(self.base_url, data=(payload)).json()

    def send_generic_message(self, recipient_id, elements):
        recipient = {
                "id": recipient_id
                }
        message = {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": elements
                        }
                    }
                }
        payload = {}
        payload['recipient'] = "{0}".format(recipient)
        payload['message'] = "{0}".format(message)
        json_payload = {
                'recipient': recipient,
                'message': message
                }
        return requests.post(self.base_url, json=json_payload).json()

