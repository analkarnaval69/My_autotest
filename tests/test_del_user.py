import requests

from used_data.api.api_urls import GET_USER_INFO_URL
from used_data.api.api_urls import POST_CREAT_USER_URL

def test_chek_user_active(post_creat_user, get_bearer_token):
    chek_user_active_url = f"{GET_USER_INFO_URL}{post_creat_user}"
    response = requests.get(url=chek_user_active_url, headers=get_bearer_token)
    assert response.status_code == 200
    assert response.json()["list"][0]["is_active"] == True

def test_del_user(post_creat_user, get_bearer_token):

    delete_url = f"{POST_CREAT_USER_URL}{post_creat_user}"
    response = requests.delete(url=delete_url, headers=get_bearer_token)
    assert response.status_code == 204

def test_chek_user_inactive(post_creat_user, get_bearer_token):

    chek_user_active_url = f"{GET_USER_INFO_URL}{post_creat_user}"
    response = requests.get(url=chek_user_active_url, headers=get_bearer_token)
    assert response.status_code == 200
    assert response.json()["list"][0]["is_active"] == False
