class my_class():
    def __init__(self, s):
        self.c = s
        self.s = s+s
    class my_class2():
        se = 23
    a = 1
    b = "mfksdkfs"
    d = 'hhh'
    def pr(self):
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)
        self.c = self.a
        self.a = self.s # a stanovitsa attributom
        print('a = ', self.a, ' b = ', self.b,  ' c = ', self.c)
def foo():
    return None

print(my_class.my_class2)
print('name = '+str(my_class.__name__))
print("just class ")
print('name = '+str(foo.__qualname__))
print("just func ")
print(my_class.pr)
asd = eval(str(my_class.pr.__qualname__))
print(asd)
print(eval('''foo'''))

##
# list serlzr & de_srlzr
# add type and str in return dict

# TODO ADD global local
# TODO Git
def make_lines_from_collection(collection):
    dump_obj = make_corrent_dumps(
                make_correct_and_str_dict(collection),
                collection)
    return dump_obj

def make_correct_and_str_dict(obj):
    # correct_values = []
    # str_values = []
    correct_and_str = {'correct_values': [], 'str_values': []}
    if type(obj).__name__ == 'dict':
        keys = obj.keys()
        values = obj.values()
        for i in keys:
            print(str(i) + '   ' + type(i).__name__)

            if type(i).__name__ == 'type':
                print('+++++++++++++++++++++TYPE+++++++++++')

                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            elif type(i).__name__ == 'function':
                print('+++++++++++++++++++++function+++++++++++')
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))
            if (type(i).__name__ == 'tuple'
            or type(i).__name__ == 'list'
            or type(i).__name__ == 'dict'
            or type(i).__name__ == 'set'):
                print('__________1111_________-to_str_objInObj(__________')
                tmp = make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']


        for i in values:
            print(type(i).__name__)

            if type(i).__name__ == 'type':
                print('+++++++++++++++++++++TYPE+++++++++++')
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if type(i).__name__ == 'function':
                print('+++++++++++++++++++++function+++++++++++')
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if (type(i).__name__ == 'tuple'
            or type(i).__name__ == 'list'
            or type(i).__name__ == 'dict'
            or type(i).__name__ == 'set'):
                print('___________________-222to_str_objInObj(__________')
                tmp = make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']



    else:
        for i in obj:
            print( type(i).__name__)

            if type(i).__name__ == 'type':
                print('+++++++++++++++++++++TYPE+++++++++++')
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))

            if type(i).__name__ == 'function':
                print('+++++++++++++++++++++function+++++++++++')
                correct_and_str['correct_values'].append(i.__qualname__)
                correct_and_str['str_values'].append(str(i))
            if (type(i).__name__ == 'tuple'
            or type(i).__name__ == 'list'
            or type(i).__name__ == 'dict'
            or type(i).__name__ == 'set'):
                print('___________________-to_str_objInObj(__________')
                tmp = make_correct_and_str_dict(i)
                correct_and_str['correct_values'] += tmp['correct_values']
                correct_and_str['str_values'] += tmp['str_values']
    return correct_and_str

def make_corrent_dumps(corrent_and_str, obj):
    str_values = corrent_and_str['str_values']
    correct_values = corrent_and_str['correct_values']
    lines = str(obj)

    print('str_ vall' + str(str_values))
    for i in range(len(str_values)):
        splt = lines.split(str_values[i], 1)
        if len(splt) > 1:
            lines = splt[0] + correct_values[i] + splt[1]
            print(type(lines))
    print(lines+'\n\n\n')
    return {'type': type(obj).__name__, 'lines': lines}

def dumps_listt(value):
    dump_obj = {'type': type(value).__name__, 'lines': str(value)}

    if (dump_obj['type'] == 'tuple'
    or dump_obj['type'] == 'list'
    or dump_obj['type'] == 'dict'
    or dump_obj['type'] == 'set'):
        dump_obj = make_lines_from_collection(value)

    return dump_obj

def loads_listt(dump_obj):
    # if dump_obj['type'] == 'tuple' \
    #         or dump_obj['type'] == 'list' \
    #         or dump_obj['type'] == 'dict':
    #     obj
    print(dump_obj)
    if dump_obj['type'] == 'str':
        return str(eval(dump_obj['lines']))
    else:
        return eval(dump_obj['lines'])




##
a = ['9999', "5555", 123, {'o': 'ok', 's': 1233}]

ev = loads_listt(dumps_listt(a))

for i in range(len(ev)):
    print(type(a[i]).__name__ + ' . ' + type(ev[i]).__name__ + ' = ' + str(ev[i]))

q = ev[3]
q = loads_listt(dumps_listt(q))
print(type(q).__name__+str(q))
print(type(q['o']).__name__ + str(q['o']))
print(type(q['s']).__name__ + str(q['s']))
print('all is ok\n')

##

sett = {1, 2, 3, 1, 2, 4}
a = 1
aa = 1.1
s = '2'
d = {'3': 3, '4': {'1': [1, 2, 3]}, foo: my_class}
f = [my_class, 'www', [12, 34]]
g = ('asdasd', my_class, 33.3, {1, 2, 3, 1, 2, 4, my_class})

fff = loads_listt(dumps_listt(a))
print(type(fff).__name__ + '  ' + str(fff))

fff = loads_listt(dumps_listt(aa))
print(type(fff).__name__ + '  ' + str(fff))

fff = loads_listt(dumps_listt(s))
print(type(fff).__name__ + '  ' + str(fff))

fff = loads_listt(dumps_listt(g))
print(type(fff).__name__ + '  ' + str(fff))

fff = loads_listt(dumps_listt(f))
print(type(fff).__name__ + '  ' + str(fff))

fff = loads_listt(dumps_listt(d))
print(type(fff).__name__ + '  ' + str(fff))














##

def dumps_int(obj):
    return str(obj)
def dumps_float(obj):
    return str(obj)
def dumps_list(obj):
    d = {}
    for l in obj:
        type_l = type(l).__name__
        if type_l != 'str':
            l = funk[type_l](l)
        d.update(type_l)
    # str = '{'
    # for l in obj:
    #     str = str + 'type: ' + type(l).__name__
    #     if type(l).__name__!= 'str':
    #         l = funk[type(l).__name__](l)
    #     str = str + l + ', '
    # str = str[:-2] + '}'
    return str



def dumps_dict(obj):
    keys = []
    for key in obj:
        if type(key).__name__ == 'int':
            key = dumps_int(key)
        keys.append({'type': type(key).__name__, 'key': key})
    print(keys)
    values = []
    for key in keys:
        values.append(obj[key])
    print(values)


funk = {'int': dumps_int, 'float': dumps_float, 'list': dumps_list}

print(dumps_list(f))

# dumps_dict(d)
#
# def dumps_a(obj):
#     print(type(obj))
#
#     tp = type(obj).__name__
#     # s = str['str']
#     if tp == 'int':
#         s = str(obj)
#     elif tp == 'float':
#         s = str(obj)
#     elif tp == 'str':
#         s = obj
#     elif tp == 'dict':
#         dump_dict(obj)
#
#         return 'DOpis dict'
#     elif tp == 'list':
#
#     elif tp == 'tuple':
#     elif tp == 'byte':
#     elif tp == 'NoneType':
#
#
#     dump = {'type':type(obj).__name__,'str':str(obj)}
#     print(dump)
#     return dump
#
# def loads_a(str):
#     print(str)
#     tp = str['type']
#     s = str['str']
#     if tp == 'int':
#         return int(s)
#     elif tp == 'float':
#         return float(s)
#     elif tp == 'str':
#         return s
#     elif tp == 'dict':
#         return 'DOpis dict'
#     elif tp == 'list':
#
#     elif tp == 'tuple':
#     elif tp == 'byte':
#     elif tp == 'NoneType':