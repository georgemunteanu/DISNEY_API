import requests

def post_method(url, data = None):
    return requests.post(url, data)

def get_method(url, data = None):
    return requests.get(url, data)
