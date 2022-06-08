from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


client = APIClient()


def __get_auth_token(user):
    return f'Bearer {RefreshToken.for_user(user).access_token}'


def make_request(url, expected_status, data=None, user=None, method='GET'):
    if user:
        client.credentials(HTTP_AUTHORIZATION=__get_auth_token(user))
    else:
        client.credentials(HTTP_AUTHORIZATION=None)

    method = method.upper()
    if method == 'GET':
        response = client.get(url, data, format='json')
    elif method == 'POST':
        response = client.post(url, data, format='json')
    else:
        raise ValueError(f'Method {method} is not available. GET or POST are accepted.')

    error_msg  = f'response {response.status_code}, expect {expected_status}'
    assert response.status_code == expected_status, error_msg
    return response.json()
