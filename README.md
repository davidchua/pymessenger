## Python Wrapper for Facebook Send/Receive API

Wrapper for [Facebook's Messenger Platform](https://developers.facebook.com/docs/messenger-platform).

__Disclaimer__: This wrapper is __NOT__ an official wrapper and do not attempt to represent Facebook in anyway.

### About

This wrapper has the following functions:

* send_text_message(recipient_id, message)

The functions return the full JSON body of the actual API call to Facebook.

### Register for an Access Token

You'll need to setup a Facebook App, Facebook Page, get the Page Access Token and link the App to the Page before you can really start to use the Send/Receive service.

[This quickstart guide should help](https://developers.facebook.com/docs/messenger-platform/quickstart)

### Installation

```bash
$ pip install pymessenger
```

### Usage

```python
from pymessenger import Bot

bot = Bot(<access_token>)
bot.send_text_message(recipient_id, message)
```

### Todo

* Structured Messages
* Receipt Messages

### Example

You can find an example of a Facebook Bot in ```examples/```
