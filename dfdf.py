##

##
def foo(c):
    aaaa = 1234
    b = 'asdf'
    return b + c

def foo2(c,d):
    aaaa = 1234
    b = 'asdf'
    return b + c + str(d)

import clean

# print(clean.dumps(foo))

clean.convert('/home/jke/txt.toml', 'json')


import inspect

def dump_f(fun):
    lines = inspect.getsourcelines(fun)[0]
    if lines[0][0] == ' ':
        for c in lines[0]:
            if c != ' ':
                break
            lines[0] = lines[0][1:]
    # (['def foo(c):\n', '    a = 1234\n', "    b = 'asdf'\n", '    return b + c\n'], 5)
    # list return
    return lines


def loads_and_start(*params, **lines):
    def_name = lines['lines'][0]
    def_name = def_name.split('(')[0]
    def_name = str(def_name.split()[-1])

    line = ''
    for l in lines['lines']:
        line += l

    if len(params) == 0:
        rett = 'q = ' + def_name + '()'
    elif len(params) == 1:
        p = params[0]
        rett = 'q = ' + def_name + '(\'' + str(p) + '\')'
    else:
        rett = 'q = ' + def_name + '('
        for param in params:
            if type(param) == type(''):
                rett = rett + '\'' + param + '\','
            else:
                rett = rett + str(param) + ','
        rett = rett[:-1] + ')'

    loc = {} # need to add same func and variebles to exec????????
    exec(line + rett, globals(), loc)
    answer = loc['q']
    return answer


def loads(lines):

    def_name = lines[0]
    def_name = def_name.split('(')[0]
    def_name = str(def_name.split()[-1])

    line = ''
    for l in lines:
        line += l

    func = 'func = ' + def_name

    loc = {} # need to add same func and variebles to exec????????
    exec(line + func, globals(), loc)
    link = loc['func']
    return link



# import pickle
#
# d = pickle.dumps(foo)
# print(d)
# print(type(pickle.loads(d)))
#
#
# print('\t\t\t\t\tLoads_and_start:')
# f = loads_and_start('111111111QQQQQQQQQQQ', lines=dump_f(foo))
# print(type(f))
# print(f)
# f = loads_and_start('MMMMMMMMMMMMMMM', 34511, lines=dump_f(foo2))
# print(type(f))
# print(f)
#
# print('\n\n\t\t\t\t\tLoads:')
# f = loads(dump_f(foo))
# print(type(f))
# print(f('IIIIIIIIOOOOOO'))
# f = loads(dump_f(foo2))
# print(type(f))
# print(f('qww__________', 8888))