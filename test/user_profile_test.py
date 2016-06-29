import json

from pymessenger.user_profile import UserProfileApi
from test_env import *

upa = UserProfileApi(PAGE_ACCESS_TOKEN, app_secret=APP_SECRET)

def test_fields_blank():
    user_profile = upa.get(TEST_USER_ID)
    assert user_profile is not None

def test_fields():
    fields = ['first_name', 'last_name']
    user_profile = upa.get(TEST_USER_ID, fields=fields)
    assert user_profile is not None
    assert len(user_profile.keys()) == len(fields)
