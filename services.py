import json

from telegram import user

from mebel_site.settings import DEFAULT_URL
import requests as rq

API_URL = DEFAULT_URL + "api/v1/"


def create_user(user_id):
    url = API_URL + "user/"
    data = {
        "user_id": user_id
    }
    response = rq.post(url, data).json()

    return response


def create_log(user_id):
    url = API_URL + "log/"
    data = {
        "user_id": user_id
    }
    response = rq.post(url, data).json()

    return response


def get_user(user_id):
    url = API_URL + f"user/{user_id}"
    response = rq.get(url)

    try:
        response = response.json()
    except:
        response = False

    return response


def get_log(user_id):
    url = API_URL + f"log/{user_id}"
    response = rq.get(url)

    try:
        response = response.json()
    except:
        response = False

    return response


def change_log(user_id, message):
    url = API_URL + f'log/{user_id}/'
    data = {
        "user_id": user_id,
        'message': json.dumps(message)
    }
    response = rq.put(url, data=data).json()
    return response


def update_user(user, log):
    url = API_URL + f"user/{user.id}/"
    data = {
        'user_id': user.id,
        "first_name": log.get('ism', None),
        "last_name": log.get('familiya', None),
        "phone": log.get('phone', None),
        'user_name': user.username
    }
    response = rq.put(url, data=data).json()
    return response


def get_ctgs():
    url = API_URL + "ctg/"
    response = rq.get(url).json()

    return response
