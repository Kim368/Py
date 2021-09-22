class my_class():
    def __init__(self, s):
        self.c = s
        self.s = s+s
    a = 1
    b = "mfksdkfs"
    def gg(self):
        print('1020')


def foo():
    a = 1234
    b = 'asdf'
    return b

import inspect

lines = inspect.getsource(foo)
print(type(lines))
print('Source code:\n' + lines)
print()

lines = inspect.getsourcelines(foo)
print(type(lines))
print('Source code lines:')
print(lines)
for line in lines[0]:
    print(line)
print()

print('type of obj = ' + str(type(foo)))

print('Getmembers:\n' + str(inspect.getmembers(foo)))

import pickle
print('pickle: ')
ps = pickle.dumps(foo)
ls = pickle.loads(ps)
print(ps)
print(ls)

print()
print()
lines = inspect.getsourcelines(foo)
d = dict(f = foo()) #serialize foo as d =  {'f': 'asdf'}
print('d = ')
print(d)

import json
print(json.loads(json.dumps(lines[0])))
    # ['def foo():\n', '    a = 1234\n', "    b = 'asdf'\n", '    return b\n']
print(json.loads(json.dumps(inspect.getsource(foo))))
    # def foo():
    # a = 1234
    # b = 'asdf'
    # return b
print(json.dumps(foo()))
    # serialize foo as "asdf"

cl = my_class('asdasd')
print(cl.c)
print(type(cl.__class__))
cl.gg()
print(inspect.getmodule(my_class))
print(inspect.getmodule(cl))
a = str(type(cl))
print(a.find('.'))
print(a)
print(inspect.getsource(cl.__class__))
print(cl.__dict__)
print(cl.__class__)

pick = pickle.dumps(cl)
print(pick)
print(pickle.loads(pick))

def dumps_cls(obj):
    attributes = obj.__dict__
    lines = inspect.getsourcelines(obj.__class__)
    return dict(lines=lines, attributes=attributes)


def loads_cls(lines, attributes):

    obj = eval('my_class()')
    type(obj)

obj = eval('my_class("asd")')
print(type(obj))
print(obj.s)