from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method (self):
        pass

    def same_operation (self):
        parser = self.factory_method()

        result = parser.operation()

        return result


##
class ParserCreatorPickle(Creator):
    def __init__ (self, obj):
        self.obj = obj

    def factory_method (self):
        return ParserPickle(self.obj)


class ParserCreatorDePickle(Creator):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def factory_method (self):
        return ParserDePickle(self.dump_obj)


##
class ParserCreatorJson(Creator):
    def __init__ (self, obj):
        self.obj = obj

    def factory_method (self):
        return ParserJson(self.obj)


class ParserCreatorDeJson(Creator):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def factory_method (self):
        return ParserDeJson(self.dump_obj)


##
class ParserCreatorYaml(Creator):
    def __init__ (self, obj):
        self.obj = obj

    def factory_method (self):
        return ParserYaml(self.obj)


class ParserCreatorDeYaml(Creator):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def factory_method (self):
        return ParserDeYaml(self.dump_obj)


##
class ParserCreatorToml(Creator):
    def __init__ (self, obj):
        self.obj = obj

    def factory_method (self):
        return ParserToml(self.obj)


class ParserCreatorDeToml(Creator):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def factory_method (self):
        return ParserDeToml(self.dump_obj)


##
class Parser(ABC):

    @abstractmethod
    def operation (self):
        pass


##
import pickle


class ParserPickle(Parser):
    def __init__ (self, obj):
        self.obj = obj

    def pick (self):
        import codecs
        # return pickle.dumps(self.obj)
        return codecs.encode(pickle.dumps(self.obj), "base64").decode()

    def operation (self):
        pick = self.pick()
        return str(pick)


class ParserDePickle(Parser):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def pick (self):
        import codecs
        return pickle.loads(codecs.decode(self.dump_obj.encode(), "base64"))
        # return pickle.loads(self.dump_obj, encoding="ASCII")

    def operation (self):
        pick = self.pick()
        return pick


##
class ParserJson(Parser):
    def __init__ (self, obj):
        self.obj = obj

    def json (self):
        strlines = ''
        jstr = '{\n'
        jstr += '\'' + 'type' + '\': ' \
                + '\'' + str(self.obj['type']) + '\'\n'
        jstr += '\'' + 'lines' + '\': ' \
                + '\'' + str(self.obj['lines']) + '\'\n'
        # jstr += '\'' + 'lines' + '\': ' \
        #             + '\'' + self.obj['lines'] + '\'\n'
        jstr += '}'
        return jstr

    def operation (self):
        j = self.json()
        return j


class ParserDeJson(Parser):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def json (self):
        dump_obj_type = None
        dump_obj_lines = None
        lines = self.dump_obj.split('\n')
        # print(lines)
        for line in lines:
            if line.find("'type': ") != -1:
                dump_obj_type = line.split("'type': ")[-1][1:-1]
            if line.find("'lines': ") != -1:
                dump_obj_lines = line.split("'lines': ")[-1][1:-1]
        # print(type(dump_obj_lines).__name__)        print(type(dump_obj_lines).__name__)
        print(dump_obj_lines)

        # print(dump_obj_lines)

        if (dump_obj_type is not None) and (dump_obj_lines is not None):
            dump_obj = {'type': dump_obj_type, 'lines': dump_obj_lines}
            return dump_obj
        pass
        # return pickle.loads(self.dump_obj, encoding="ASCII")

    def operation (self):
        j = self.json()
        return j


##
class ParserYaml(Parser):
    def __init__ (self, obj):
        self.obj = obj

    def yaml (self):
        ystr = 'type' + ': ' \
               + str(self.obj['type']) + '\n'
        ystr += 'lines' + ': ' \
                + str(self.obj['lines']) + '\n'

        return ystr

    def operation (self):
        y = self.yaml()
        return y


class ParserDeYaml(Parser):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def yaml (self):
        dump_obj_type = None
        dump_obj_lines = None
        lines = self.dump_obj.split('\n')
        for line in lines:
            if line.find('type: ') != -1:
                dump_obj_type = line.split('type: ')[-1]
            if line.find('lines: ') != -1:
                dump_obj_lines = line.split('lines: ')[-1]
                print(type(dump_obj_lines).__name__)
                print(dump_obj_lines)
                # dump_obj_lines = dump_obj_lines[1:-1].split('\', \'')
                # print(dump_obj_lines)
        if (dump_obj_type is not None) and (dump_obj_lines is not None):
            dump_obj = {'type': dump_obj_type, 'lines': dump_obj_lines}
            return dump_obj


    def operation (self):
        y = self.yaml()
        return y


##
class ParserDeToml(Parser):
    def __init__ (self, dump_obj):
        self.dump_obj = dump_obj

    def toml (self):
        dump_obj_type = None
        dump_obj_lines = None
        lines = self.dump_obj.split('\n')
        for line in lines:
            if line.find('type = ') != -1:
                dump_obj_type = line.split('type = ')[-1]
            if line.find('lines = ') != -1:
                dump_obj_lines = line.split('lines = ')[-1]
        if (dump_obj_type is not None) and (dump_obj_lines is not None):
            dump_obj = {'type': dump_obj_type, 'lines': dump_obj_lines}
            return dump_obj


    def operation (self):
        y = self.toml()
        return y


class ParserToml(Parser):
    def __init__ (self, obj):
        self.obj = obj

    def toml (self):
        tstr = 'type' + ' = ' \
               + str(self.obj['type']) + '\n'
        tstr += 'lines' + ' = ' \
                + str(self.obj['lines']) + '\n'

        return tstr

    def operation (self):
        t = self.toml()
        return t


##
def client_code(creator: Creator):
    # print(f"Client work with {creator.same_operation()}")
    return creator.same_operation()


def create_serializer(ftype, obj):
    d = {'pickle': ParserCreatorPickle, 'json': ParserCreatorJson, 'yaml': ParserCreatorYaml, 'toml': ParserCreatorToml}
    return client_code(d[ftype](obj))


def create_deserializer(ftype, dump_obj):
    d = {'pickle': ParserCreatorDePickle, 'json': ParserCreatorDeJson, 'yaml': ParserCreatorDeYaml,
         'toml': ParserCreatorDeToml}
    return client_code(d[ftype](dump_obj))




##
# if __name__ == "__main__":
#     create_serializer('pickle', '1231231231')
#     client_code(ParserCreatorPickle('1234'))
#     client_code(ParserCreatorYaml({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))
#     client_code(ParserCreatorJson({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))
#     client_code(ParserCreatorToml({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))
