import requests
import json
import os

test_url = "https://httpbin.org/get"
payload = {'page': 2, 'count': 30}


def my_decorator(func):
    print("I'm a decorator. I'm going to be called only one time when you ask me to decorate your function.")
    def wrapped_func(url_str, pl):
        print("wrapped_func started")
        r = func(url_str, pl)
        print(r.json())
        return r
    print("I'm returning a decorated function now.")
    return wrapped_func


@my_decorator
def req1(url_str, pl):
    return requests.get(test_url, pl)

print("***************")

x = req1(test_url, payload)
print(x.text)

print(os.path.basename(__file__)[:-1])
