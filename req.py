import requests
import json

test_url = "https://httpbin.org/get"
payload = {'page': 2, 'count': 30}


def my_external_func(url_str, pl):
    print("I'm a decorators maker. I'm going to be called only one time when you ask me to create a decorator.")
    def my_decorator(func):
        print("I'm a decorator. I'm going to be called only one time when you ask me to decorate your function.")
        def wrapped_func(url_str, pl):
            print("wrapped_func started")
            r = func(url_str, pl)
            print(r.json())
            return r
        print("I'm returning a decorated function now.")
        return wrapped_func
    print("I'm returning a decorator now.")
    return my_decorator

@my_external_func(test_url, payload)
def req1(url_str, pl):
    return requests.get(test_url, pl)

print("***************")

x = req1(test_url, payload)
print(x.text)