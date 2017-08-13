import os
import json
from enum import Enum

import requests
from requests_toolbelt import MultipartEncoder

from pymessenger import utils

DEFAULT_API_VERSION = 2.6


class NotificationType(Enum):
    regular = "REGULAR"
    silent_push = "SILENT_PUSH"
    no_push = "NO_PUSH"


class Bot:
    def __init__(self, access_token, **kwargs):
        """
            @required:
                access_token
            @optional:
                api_version
                app_secret
        """

        self.api_version = kwargs.get('api_version') or DEFAULT_API_VERSION
        self.app_secret = kwargs.get('app_secret')
        self.graph_url = 'https://graph.facebook.com/v{0}'.format(self.api_version)
        self.access_token = access_token

    @property
    def auth_args(self):
        if not hasattr(self, '_auth_args'):
            auth = {
                'access_token': self.access_token
            }
            if self.app_secret is not None:
                appsecret_proof = utils.generate_appsecret_proof(self.access_token, self.app_secret)
                auth['appsecret_proof'] = appsecret_proof
            self._auth_args = auth
        return self._auth_args

    def send_recipient(self, recipient_id, payload, notification_type=NotificationType.regular):
        payload['recipient'] = {
            'id': recipient_id
        }
        payload['notification_type'] = notification_type.value
        return self.send_raw(payload)

    def send_message(self, recipient_id, message, notification_type=NotificationType.regular):
        return self.send_recipient(recipient_id, {
            'message': message
        }, notification_type)

    def send_attachment(self, recipient_id, attachment_type, attachment_path,
                        notification_type=NotificationType.regular):
        """Send an attachment to the specified recipient using local path.
        Input:
            recipient_id: recipient id to send to
            attachment_type: type of attachment (image, video, audio, file)
            attachment_path: Path of attachment
        Output:
            Response from API as <dict>
        """
        payload = {
            'recipient': {
                {
                    'id': recipient_id
                }
            },
            'notification_type': notification_type,
            'message': {
                {
                    'attachment': {
                        'type': attachment_type,
                        'payload': {}
                    }
                }
            },
            'filedata': (os.path.basename(attachment_path), open(attachment_path, 'rb'))
        }
        multipart_data = MultipartEncoder(payload)
        multipart_header = {
            'Content-Type': multipart_data.content_type
        }
        return requests.post(self.graph_url, data=multipart_data,
                             params=self.auth_args, headers=multipart_header).json()

    def send_attachment_url(self, recipient_id, attachment_type, attachment_url,
                            notification_type=NotificationType.regular):
        """Send an attachment to the specified recipient using URL.
        Input:
            recipient_id: recipient id to send to
            attachment_type: type of attachment (image, video, audio, file)
            attachment_url: URL of attachment
        Output:
            Response from API as <dict>
        """
        return self.send_message(recipient_id, {
            'attachment': {
                'type': attachment_type,
                'payload': {
                    'url': attachment_url
                }
            }
        }, notification_type)

    def send_text_message(self, recipient_id, message, notification_type=NotificationType.regular):
        """Send text messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/text-message
        Input:
            recipient_id: recipient id to send to
            message: message to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(recipient_id, {
            'text': message
        }, notification_type)

    def send_generic_message(self, recipient_id, elements, notification_type=NotificationType.regular):
        """Send generic messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/generic-template
        Input:
            recipient_id: recipient id to send to
            elements: generic message elements to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(recipient_id, {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }, notification_type)

    def send_button_message(self, recipient_id, text, buttons, notification_type=NotificationType.regular):
        """Send text messages to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/button-template
        Input:
            recipient_id: recipient id to send to
            text: text of message to send
            buttons: buttons to send
        Output:
            Response from API as <dict>
        """
        return self.send_message(recipient_id, {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": text,
                    "buttons": buttons
                }
            }
        }, notification_type)

    def send_action(self, recipient_id, action, notification_type=NotificationType.regular):
        """Send typing indicators or send read receipts to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/sender-actions

        Input:
            recipient_id: recipient id to send to
            action: action type (mark_seen, typing_on, typing_off)
        Output:
            Response from API as <dict>
        """
        return self.send_recipient(recipient_id, {
            'sender_action': action
        }, notification_type)

    def send_image(self, recipient_id, image_path, notification_type=NotificationType.regular):
        """Send an image to the specified recipient.
        Image must be PNG or JPEG or GIF (more might be supported).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
        Input:
            recipient_id: recipient id to send to
            image_path: path to image to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(recipient_id, "image", image_path, notification_type)

    def send_image_url(self, recipient_id, image_url, notification_type=NotificationType.regular):
        """Send an image to specified recipient using URL.
        Image must be PNG or JPEG or GIF (more might be supported).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/image-attachment
        Input:
            recipient_id: recipient id to send to
            image_url: url of image to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(recipient_id, "image", image_url, notification_type)

    def send_audio(self, recipient_id, audio_path, notification_type=NotificationType.regular):
        """Send audio to the specified recipient.
        Audio must be MP3 or WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment
        Input:
            recipient_id: recipient id to send to
            audio_path: path to audio to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(recipient_id, "image", audio_path, notification_type)

    def send_audio_url(self, recipient_id, audio_url, notification_type=NotificationType.regular):
        """Send audio to specified recipient using URL.
        Audio must be MP3 or WAV
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/audio-attachment
        Input:
            recipient_id: recipient id to send to
            audio_url: url of audio to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(recipient_id, "audio", audio_url, notification_type)

    def send_video(self, recipient_id, video_path, notification_type=NotificationType.regular):
        """Send video to the specified recipient.
        Video should be MP4 or MOV, but supports more (https://www.facebook.com/help/218673814818907).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment
        Input:
            recipient_id: recipient id to send to
            video_path: path to video to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(recipient_id, "video", video_path, notification_type)

    def send_video_url(self, recipient_id, video_url, notification_type=NotificationType.regular):
        """Send video to specified recipient using URL.
        Video should be MP4 or MOV, but supports more (https://www.facebook.com/help/218673814818907).
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/video-attachment
        Input:
            recipient_id: recipient id to send to
            video_url: url of video to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(recipient_id, "video", video_url, notification_type)

    def send_file(self, recipient_id, file_path, notification_type=NotificationType.regular):
        """Send file to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment
        Input:
            recipient_id: recipient id to send to
            file_path: path to file to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment(recipient_id, "file", file_path, notification_type)

    def send_file_url(self, recipient_id, file_url, notification_type=NotificationType.regular):
        """Send file to the specified recipient.
        https://developers.facebook.com/docs/messenger-platform/send-api-reference/file-attachment
        Input:
            recipient_id: recipient id to send to
            file_url: url of file to be sent
        Output:
            Response from API as <dict>
        """
        return self.send_attachment_url(recipient_id, "file", file_url, notification_type)

    def get_user_info(self, recipient_id, fields=None):
        """Getting information about the user
        https://developers.facebook.com/docs/messenger-platform/user-profile
        Input:
          recipient_id: recipient id to send to
        Output:
          Response from API as <dict>
        """
        params = {}
        if fields is not None and isinstance(fields, (list, tuple)):
            params['fields'] = ",".join(fields)

        params.update(self.auth_args)

        request_endpoint = '{0}/{1}'.format(self.graph_url, recipient_id)
        response = requests.get(request_endpoint, params=params)
        if response.status_code == 200:
            return response.json()

        return None

    def send_raw(self, payload):
        request_endpoint = '{0}/me/messages'.format(self.graph_url)
        response = requests.post(
            request_endpoint,
            params=self.auth_args,
            json=payload
        )
        result = response.json()
        return result

    def _send_payload(self, payload):
        """ Deprecated, use send_raw instead """
        return self.send_raw(payload)

#quick_replies stuff
    def QuickReply_Send(self,user_id,text,reply_payload):
        # quick reply for messenger
        # this method sends the request to fb
        params = {
            "access_token":self.access_token,
        }
        payload = {
          "recipient":{"id":user_id,},
          "message":{
            "text":"{}".format(text),
            "quick_replies":reply_payload,
          }
        }
        requests.post(
            "https://graph.facebook.com/v2.6/me/messages",
            params=params,
            data=payload,
            headers={
                'Content-type': 'application/json'
            }
        )

    # quick replies
    def QuickReply_CreatePayload(self,qk_payload):
        # this function constructs and returns a payload for the the quick reply button payload
        # pass in a tuple-of-list / list-of-lists
        # example : (['title1','payload'],['title2','payload'])
        quick_btns = []
        # constructs the payload 
        for i in range(len(qk_payload)):
            quick_btns.append(
                {
                    "content_type":"text",
                    "title":qk_payload[i][0],
                    "payload":qk_payload[i][1],
                }
            )
        return quick_btns

    def send_quickreply(self,recipient_id,quick_reply_message,reply_options):
        # use this method to send quick replies
        # this method puts everything together
        # automatically constructs the payload for the buttons from the list
        reply_payload = QuickReply_CreatePayload(reply_options)
        QuickReply_Send(token = token,
            user_id = recipient_id,
            text = "{}".format(quick_reply_message),
            reply_payload = reply_payload,
        )
        
        # show the `get started` button
    def GetStartedButton_createBtn(self):
        params = {
            "access_token":self.access_token,
        }
        payload = json.dumps({
                "get_started":{
                            "payload":"@get_started"
                }
        })

        requests.post(
                        "https://graph.facebook.com/v2.6/me/messenger_profile",
                        params=params,
                        data=payload,
                        headers={
                            'Content-type': 'application/json'
                        }
        )



    # get the payload from the get started button
    def GetStartedButton_getPayload(self):
        params = {
            "access_token":self.access_token,
        }
        requests.get("https://graph.facebook.com/v2.6/me/messenger_profile?fields=get_started",params=params)

    # delete the `get started` button
    def GetStartedButton_deleteBtn(self):
        params = {
            "access_token":self.access_token,
        }
        payload = {
                "fields":[
                        "get_started"
                ]
        }
        requests.delete(
                        "https://graph.facebook.com/v2.6/me/messenger_profile",
                        params=params,data=payload,
                        headers={'Content-type':'application/json'}
        )
        
        
def build_generic_elements(self,elements):
    """ arg format :({
                        "element_data":[{"data":[title,img_url,sub_title,action_url]},]
                        "button_data":[{"data":[url,title]}]
                    })

    """
    element_list = []
    button_list = []
    len_element = len(elements['element_data'])
    len_button = len(elements['button_data'])
    
    # constructs the button payload
    for i in range(len_button):
        button_list.append({
            "type":"web_url",
            "url":elements['button_data'][i]['data'][0],
            "title":elements['button_data'][i]['data'][1],
        })

    # constructs the generic elements payload
    for x in range(len_element):
        element_list.append({
            "title":elements['element_data'][x]['data'][0],
            "image_url":elements['element_data'][x]['data'][1],
            "subtitle":elements['element_data'][x]['data'][2],
            "default_action":{
                "type": "web_url",
                "url": elements['element_data'][x]['data'][3],
                "webview_height_ratio": "tall",
            },
            "buttons": button_list,
        })
    return element_list

def generic_button_send(self,user_id,element_payload):
    params = {
        "access_token":self.access_token,

    }

    # builds the payload for elements in JSON format
    elements = build_generic_elements(element_payload)
    data=json.dumps({
      "recipient":{
        "id":user_id
      },
      "message":{
        "attachment":{
          "type":"template",
          "payload":{
            "template_type":"generic",
            "elements": elements,
          }
        }
      }
    })

    requests.post(
        "https://graph.facebook.com/v2.6/me/messages",
        params=params,
        data=data,
        headers={
            'Content-type': 'application/json'
        }
    )


