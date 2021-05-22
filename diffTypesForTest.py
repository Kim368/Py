class my_class():
    def __init__(self, s):
        self.c = s
        self.s = s+s

    class my_class2():
        se = 23
        a = 1
        b = "mfksdkfs"
        d = 'hhh'

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




import random
from string import printable


class Collections():
    list_int = []
    list_str = []
    list_float = []
    list_bool = []
    set_bool = ()
    list_list = []
    dictionary = {my_class: 123, 'asdas': 234, 6:1, my_class.pr: 'funk', 'abc': ['a', 'b', 'c']}
    tupl = (1, 2, 'asdd', my_class, my_class.aaa)

    def __init__(self):
        self.list_int = self.get_list_int()
        self.list_str = self.get_list_str()
        self.list_float = self.get_list_float()
        self.list_bool = self.get_list_bool()
        self.set_bool = self.get_set()
        self.list_list = self.get_list_list()
        #self.dictionary = self.get_dict()


    def get_list_int(self):
        for i in range(50):
            self.list_int.append(random.randint(-999999999, 999999999))
        return self.list_int


    def get_list_float(self):
        for i in range(50):
            num = random.randint(-999999999, 999999999)
            self.list_float.append(num * 0.001)
        return self.list_float


    def get_list_bool(self):
        for i in range(50):
            num = random.random()
            if num == 1:
                bl = True
            else:
                bl = False
            self.list_bool.append(bl)
        return self.list_bool


    def get_list_str(self):
        s = ''
        for i in range(50):
            for j in range(20):
                s += random.choice(printable)
            self.list_str.append(s)
        return self.list_str


    def get_set(self):
        self.set_bool = set(self.get_list_bool())
        return self.set_bool


    def get_list_list(self):
        l = self.get_list_str()
        l.append(self.get_list_bool())
        l.append(self.get_list_int())
        l.append(self.get_list_float())
        return l


    def get_dict(self):
        keys = self.get_list_int() + self.get_list_str()
        values = self.get_list_str() + self.get_list_float()
        d = dict(zip(keys, values))
        d[my_class] = my_class.my_class2
        d[my_class] = my_class.pr
        d[my_class.pr] = my_class.my_class2
        return d

# import clean
# Collections()
# clean.dump(Collections, '/home/jke/txt.json', 'pickle')
# clean.dump(Collections, '/home/jke/txt.json', 'json')
# clean.dump(Collections, '/home/jke/txt.json', 'yaml')
# clean.dump(Collections, '/home/jke/txt.json', 'toml')
#
# # a = clean.load('/home/jke/txt.json', {'my_class': my_class})
# clean.convert('/home/jke/txt.pickle', 'json')
# clean.convert('/home/jke/txt.pickle', 'json')
# a = clean.load('/home/jke/txt.json', {'my_class': my_class})
# clean.load('/home/jke/txt.yaml', {'my_class': my_class})
# print(a)