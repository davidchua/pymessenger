import json
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from pymessenger.user_profile import UserProfileApi

TOKEN = os.environ.get('TOKEN')
APP_SECRET = os.environ.get('APP_SECRET')
TEST_USER_ID = os.environ.get('RECIPIENT_ID')

upa = UserProfileApi(TOKEN, app_secret=APP_SECRET)

def test_fields_blank():
    user_profile = upa.get(TEST_USER_ID)
    assert user_profile is not None

def test_fields():
    fields = ['first_name', 'last_name']
    user_profile = upa.get(TEST_USER_ID, fields=fields)
    assert user_profile is not None
    assert len(user_profile.keys()) == len(fields)
