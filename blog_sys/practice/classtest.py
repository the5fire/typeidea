# coding: utf-8

class base(object):
    a = 'test'


class new(base):
    c = 'm'
    #a = 'b'


qwe = new()
print(qwe.a)
