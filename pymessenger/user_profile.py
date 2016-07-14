import requests

from pymessenger.graph_api import FacebookGraphApi
    
class UserProfileApi(FacebookGraphApi):
    def get(self, user_id, fields=None):
        params = {}
        if fields is not None and isinstance(fields, (list, tuple)):
            params['fields'] = ",".join(fields)

        params.update(self.auth_args)

        request_endpoint = '{0}/{1}'.format(self.graph_url, user_id)
        response = requests.get(request_endpoint, params=params)
        if response.status_code == 200:
            user_profile = response.json()
            return user_profile
        return None
