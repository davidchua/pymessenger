# pymessenger [![Build Status](https://travis-ci.org/davidchua/pymessenger.svg?branch=master)](https://travis-ci.org/davidchua/pymessenger)

Python Wrapper for [Facebook Messenger Platform](https://developers.facebook.com/docs/messenger-platform).

__Disclaimer__: This wrapper is __NOT__ an official wrapper and do not attempt to represent Facebook in anyway.

### About

This wrapper has the following functions:

* send_text_message(recipient_id, message)
* send_message(recipient_id, message)
* send_generic_message(recipient_id, elements)
* send_button_message(recipient_id, text, buttons)
* send_attachment(recipient_id, attachment_type, attachment_path)
* send_attachment_url(recipient_id, attachment_type, attachment_url)
* send_image(recipient_id, image_path)
* send_image_url(recipient_id, image_url)
* send_audio(recipient_id, audio_path)
* send_audio_url(recipient_id, audio_url)
* send_video(recipient_id, video_path)
* send_video_url(recipient_id, video_url)
* send_file(recipient_id, file_path)
* send_file_url(recipient_id, file_url)
* send_action(recipient_id, action)
* send_raw(payload)
* get_user_info(recipient_id)
* set_get_started(gs_obj)
* set_persistent_menu(pm_obj)
* remove_get_started()
* remove_persistent_menu()

You can see the code/documentation for there in [bot.py](pymessenger/bot.py).

The functions return the full JSON body of the actual API call to Facebook.

### Register for an Access Token

You'll need to setup a [Facebook App](https://developers.facebook.com/apps/), Facebook Page, get the Page Access Token and link the App to the Page before you can really start to use the Send/Receive service.

[This quickstart guide should help](https://developers.facebook.com/docs/messenger-platform/quickstart)

### Installation

```bash
pip install pymessenger
```

### Usage

```python
from pymessenger.bot import Bot

bot = Bot(<access_token>, [optional: app_secret])
bot.send_text_message(recipient_id, message)
```

__Note__: From Facebook regarding User IDs

> These ids are page-scoped. These ids differ from those returned from Facebook Login apps which are app-scoped. You must use ids retrieved from a Messenger integration for this page in order to function properly.

> If `app_secret` is initialized, an app_secret_proof will be generated and send with every request.
> Appsecret Proofs helps further secure your client access tokens. You can find out more on the [Facebook Docs](https://developers.facebook.com/docs/graph-api/securing-requests#appsecret_proof)


##### Sending a generic template message:

> [Generic Template Messages](https://developers.facebook.com/docs/messenger-platform/implementation#receive_message) allows you to add cool elements like images, text all in a single bubble.


```python
from pymessenger.bot import Bot
bot = Bot(<access_token>)
elements = []
element = Element(title="test", image_url="<arsenal_logo.png>", subtitle="subtitle", item_url="http://arsenal.com")
elements.append(element)

bot.send_generic_message(recipient_id, elements)
```

Output:

![Generic Bot Output](https://cloud.githubusercontent.com/assets/68039/14519266/4c7033b2-0250-11e6-81a3-f85f3809d86c.png)

##### Sending an image/video/file using an URL:

```python
from pymessenger.bot import Bot
bot = Bot(<access_token>)
image_url = "http://url/to/image.png"
bot.send_image_url(recipient_id, image_url)
```

### Todo

* Structured Messages
* Receipt Messages
* Quick Replies
* Airlines
* Tests!

### Example

![Screenshot of Echo Facebook Bot](https://cloud.githubusercontent.com/assets/68039/14516627/905c84ae-0237-11e6-918e-2c2ae9352f7d.png)

You can find an example of an Echo Facebook Bot in ```examples/```


