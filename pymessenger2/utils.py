import hashlib
import hmac
import six
import attr
import json


def validate_hub_signature(app_secret, request_payload, hub_signature_header):
    """
        @inputs:
            app_secret: Secret Key for application
            request_payload: request body
            hub_signature_header: X-Hub-Signature header sent with request
        @outputs:
            boolean indicated that hub signature is validated
    """
    try:
        hash_method, hub_signature = hub_signature_header.split('=')
    except:
        pass
    else:
        digest_module = getattr(hashlib, hash_method)
        hmac_object = hmac.new(
            str(app_secret), str(request_payload), digest_module)
        generated_hash = hmac_object.hexdigest()
        if hub_signature == generated_hash:
            return True
    return False


def generate_appsecret_proof(access_token, app_secret):
    """
        @inputs:
            access_token: page access token
            app_secret_token: app secret key
        @outputs:
            appsecret_proof: HMAC-SHA256 hash of page access token
                using app_secret as the key
    """
    if six.PY2:
        hmac_object = hmac.new(
            str(app_secret), str(access_token), hashlib.sha256)
    else:
        hmac_object = hmac.new(
            bytearray(app_secret, 'utf8'),
            str(access_token).encode('utf8'), hashlib.sha256)
    generated_hash = hmac_object.hexdigest()
    return generated_hash


class AttrsEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__attrs_attrs__'):
            items_iterator = (attr.asdict(obj).items()
                              if six.PY3 else
                              attr.asdict(obj).iteritems())
            return {k: v for k, v in items_iterator if v is not None}
        return json.JSONEncoder.default(self, obj)
