
class my_class():
    def __init__(self, s):
        self.c = s
        self.s = s+s


    a = 1
    b = "mfksdkfs"
    d = 'hhh'
    def aaa(self):
        return 'AZAZZAZAZAZA'
    def pr(self):
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)
        self.c = self.a
        self.a = self.s # a stanovitsa attributom
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)

lllll = ''

import inspect
def dumps_cls(obj):
    # attributes = obj.__dict__
    lines = inspect.getsourcelines(obj) # inspect.getsourcelines(obj.__class__)
    print('lines: ' + str(lines))
    if lines[0][0] == ' ':
        for c in lines[0]:
            if c != ' ':
                break
            lines[0] = lines[0][1:]
    return lines[0]

def loads_cl(lines):
    cl_name = lines[0]
    lines[0] = 'class amy_class():\n'
    cl_name = cl_name.split('(')[0]
    cl_name = str(cl_name.split()[-1])
    cl_name = 'a' + cl_name

    line = ''
    for l in lines:
        line += l
    print(line)
    lllll = lines
    cl = 'cl = ' + cl_name

    loc = {}  # need to add same func and variebles to exec????????
    exec(line + '\n' +cl, {}, loc)
    link = loc['cl']
    print('globals()')
    ww = (globals())
    return link
#
# c = loads_cl('''class my_class():
#     def __init__(self, s):
#         self.c = s
#         self.s = s+s
#     a = 1
#     b = "mfksdkfs"
#     d = 'hhh'
#     def aaa(self):
#         return 'AZAZZAZAZAZA'
#     def pr(self):
#         print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)
#         self.c = self.a
#         self.a = self.s # a stanovitsa attributom
#         print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)'''
# )
c = loads_cl(dumps_cls(my_class))
print(c)
print(c('a').aaa())

from dfdf import *

d = loads(dump_f(my_class.pr))
print(d)
print(d(my_class('))))))))')))




#
# f = loads(dump_f(my_class.pr))
# print(f)
# print(type(f))
# print(f(my_class()))
#
# def dumps_cls(obj):
#     attributes = obj.__dict__
#     lines = inspect.getsourcelines(obj) #inspect.getsourcelines(obj.__class__)
#     print('lines: ' + str(lines))
#     print('atrrti: ' + attributes)
#     return dict(lines=lines, attributes=attributes)

# def loads_cl(dumped):
#     exec()
#
# dumps_cls(my_class)

# import pickle
#
# d = pickle.dumps(my_class)
# print(d)
# print(type(d))
# u = pickle.loads(d)
# print(type(u))
# print(u)