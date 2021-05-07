##

class my_class():
    def __init__(self, s):
        self.c = s
        self.s = s+s
    a = 1
    b = "mfksdkfs"
    d = 'hhh'
    def pr(self):
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)
        self.c = self.a
        self.a = self.s # a stanovitsa attributom
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)


print({my_class: my_class})

##


def foo():
    a = 1234
    b = 'asdf'
    return b

##

import inspect
def dumps_cls(obj):
    attributes = obj.__dict__
    lines = inspect.getsoulinesrcelines(obj.__class__)
    return dict(lines=lines, attributes=attributes)


def loads_cls(lines, attributes):
    obj = eval('my_class()')
    type(obj)
##
dump = dumps_cls(my_class('asd'))
print(dump)

# obj = my_class('asd')
name = dump['lines'][0][0]
name = name[5:-4].split()[0]
print(name)
attributes = dump['attributes']


print(attributes)
cl = my_class('qwe')
cl.c = attributes['c']
cl.s = attributes['s']
print(cl.c)
print(my_class.__dict__['__init__'])
cl.pr()
dump = dumps_cls(cl)
print(dump)


# for line in dump['lines'][0]:
#     if line.find('def __init__(self') != -1:
#
#         line = line.strip()
#         print(line)
#         line = line.split(',')
#         print('Ha BxoD B my_class self i eshe ' + str(len(line)-1) + ' paremetr/a/oB')
#         break
# if
