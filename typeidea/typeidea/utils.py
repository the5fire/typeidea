# coding:utf-8

from django.core.cache import cache


def cache_it(func):
    def wrapper(self, *args, **kwargs):
        key = repr((func.__name__, args, kwargs))
        result = cache.get(key)
        if result:
            print('hit cache')
            return result
        print('hit db')
        result = func(self, *args, **kwargs)
        cache.set(key, result, 60 * 5)
        return result
    return wrapper
