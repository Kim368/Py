import inspect


def dump(obj, path, *args):
    dumps_obj = dumps(obj)
    if len(args) == 1:
        import factory
        dumps_obj = factory.create_serializer(args[0], dumps_obj)
        if path.find('.') != -1:
            path = str(path.split('.')[0]) + '.' + args[0]
        # print('path ' + path)

    f = open(path, 'w')
    f.writelines(str(dumps_obj))
    f.close()
    return path
    # print(f"Dumping was successful: {path} ")


def load(path, globl):
    if path.find('.') != -1:
        find_in_types = 'picklejsonyamltoml'
        ftype = str(path.split('.')[-1])
        if find_in_types.find(ftype) != -1:
            f = open(path, 'r')
            line = f.read()
            f.close()
            import factory
            dump_obj = factory.create_deserializer(ftype, line)
            if len(globl) == 0:
                return loads(dump_obj, globl)
            else:
                return loads(dump_obj, globl)



# def convert(path, type, globl):
#     find_in_types = 'picklejsonyamltoml'
#     ftype = str(path.split('.')[-1])
#     if find_in_types.find(ftype) != -1:
#         if ftype != type:
#             obj = load(path, globl)
#             return dump(obj, path, type)
def convert(path, type):
    find_in_types = 'picklejsonyamltoml'
    ftype = str(path.split('.')[-1])
    if find_in_types.find(ftype) != -1:
        if ftype != type:
            f = open(path, 'r')
            line = f.read()
            f.close()
            import factory
            dumps_obj = factory.create_deserializer(ftype, line)
            dumps_obj = factory.create_serializer(type, dumps_obj)

            path = str(path.split('.')[0]) + '.' + type
            f = open(path, 'w')
            f.writelines(str(dumps_obj))
            f.close()

def loads(dumps_obj, globl):
    # print(globl)
    if dumps_obj['type'] == 'type':
        obj = __loads_class(dumps_obj['lines'], globl)
    elif dumps_obj['type'] == 'function':
        obj = __loads_func(dumps_obj['lines'], globl)
    else:
        obj = __loads_other(dumps_obj, globl)
    return obj


def __loads_class(lines, globl):


    if type(lines).__name__ == 'str':
        lines = eval(lines)

    cl_name = lines[0]
    # lines[0] = 'class amy_class():\n'
    cl_name = cl_name.split('(')[0]
    cl_name = str(cl_name.split()[-1])
    # cl_name = 'a' + cl_name

    line = ''
    for l in lines:
        line += l
    lllll = lines
    cl = 'cl = ' + cl_name


    loc = {}  # need to add same func and variebles to exec????????
    exec(line + '\n' + cl, globl, loc)
    link = loc['cl']
    # ww = (globals())
    return link


def __loads_func(lines, globl):
    if type(lines).__name__ == 'str':
        lines = eval(lines)
    def_name = lines[0]
    def_name = def_name.split('(')[0]
    def_name = str(def_name.split()[-1])

    line = ''
    for l in lines:
        line += l

    func = 'func = ' + def_name

    loc = {}  # need to add same func and variebles to exec????????
    exec(line + func, globl, loc)
    link = loc['func']
    return link


def __loads_other(dump_obj, globl):
    # print(dump_obj)
    if dump_obj['type'] == 'str':
        return dump_obj['lines']
    else:
        return eval(dump_obj['lines'], globl)


def dumps(obj):
    if type(obj).__name__ == 'type':
        dump_obj = __dumps_class(obj)
    elif type(obj).__name__ == 'function':
        dump_obj = __dumps_func(obj)
    else:
        dump_obj = __dumps_other(obj)
    return dump_obj


def __dumps_class(obj):
    # print(obj.__dict__)
    # print(obj)
    lines = inspect.getsourcelines(obj)  # inspect.getsourcelines(obj.__class__)
    # print('lines: ' + str(lines))  # list
    if lines[0][0][0] == ' ':
        for c in lines[0][0]:
            if c != ' ':
                break
            lines[0][0] = lines[0][0][1:]
    return {'type': type(obj).__name__, 'lines': lines[0]}


def __dumps_func(obj):
    lines = inspect.getsourcelines(obj)[0] # list
    if lines[0][0] == ' ':
        for c in lines[0]:
            if c != ' ':
                break
            lines[0] = lines[0][1:]

    # (['def foo(c):\n', '    a = 1234\n', "    b = 'asdf'\n", '    return b + c\n'], 5)
    # list return
    return {'type': type(obj).__name__, 'lines': lines}


def __dumps_other(value):
    dump_obj = {'type': type(value).__name__, 'lines': str(value)}

    if (dump_obj['type'] == 'tuple'
        or dump_obj['type'] == 'list'
        or dump_obj['type'] == 'dict'
            or dump_obj['type'] == 'set'):
        dump_obj = __make_lines_from_collection(value)

    return dump_obj


def __make_lines_from_collection(collection):
    dump_obj = __make_corrent_dumps(
                __make_correct_and_str_dict(collection),
                collection)
    return dump_obj


def __make_correct_and_str_dict(obj):
    # correct_values = []
    # str_values = []
    correct_and_str = {'correct_values': [], 'str_values': []}
    if type(obj).__name__ == 'dict':
        keys = obj.keys()
        values = obj.values()
        for i in keys:
            if type(i).__name__ == 'type':
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            elif type(i).__name__ == 'function':
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if (type(i).__name__ == 'tuple'
                or type(i).__name__ == 'list'
                or type(i).__name__ == 'dict'
                    or type(i).__name__ == 'set'):
                # print('__________1111_________-to_str_objInObj(__________')
                tmp = __make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']


        for i in values:
            # print(type(i).__name__)
            # print('eeeeeeee', type(i).__name__)
            if type(i).__name__ == 'type':
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if type(i).__name__ == 'function':
            #     print(i.__name__)
            #     print(i.__qualname__)
            #     print(type(i))
            #     print(str(i))
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if (type(i).__name__ == 'tuple'
                or type(i).__name__ == 'list'
                or type(i).__name__ == 'dict'
                    or type(i).__name__ == 'set'):
                tmp = __make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']



    else:
        for i in obj:
            # print( type(i).__name__)

            if type(i).__name__ == 'type':
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if type(i).__name__ == 'function':
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))
            if (type(i).__name__ == 'tuple'
                or type(i).__name__ == 'list'
                or type(i).__name__ == 'dict'
                    or type(i).__name__ == 'set'):
                tmp = __make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']
    return correct_and_str


def __make_corrent_dumps(corrent_and_str, obj):
    str_values = corrent_and_str['str_values']
    correct_values = corrent_and_str['correct_values']
    lines = str(obj)

    for i in range(len(str_values)):
        splt = lines.split(str_values[i], 1)
        if len(splt) > 1:
            lines = splt[0] + correct_values[i] + splt[1]
    return {'type': type(obj).__name__, 'lines': lines}


class m():
    a = 1

if __name__ == "__main__":
    dump(dump, 'D:\\work\\lab2\\txt.txt', 'pickle')
    a = load('D:\\work\\lab2\\txt.pickle', {})
    print(a)