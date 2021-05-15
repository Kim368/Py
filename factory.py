from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def same_operation(self):
        parser = self.factory_method()

        result = parser.operation()

        return result

class ParserCreatorPickle(Creator):
    def __init__(self, obj):
        self.obj = obj

    def factory_method(self):
        return ParserPickle(self.obj)

class ParserCreatorDePickle(Creator):
    def __init__(self, dump_obj):
        self.dump_obj = dump_obj

    def factory_method(self):
        return ParserDePickle(self.dump_obj)

class ParserCreatorJson(Creator):
    def __init__(self, obj):
        self.obj = obj
    def factory_method(self):
        return ParserJson(self.obj)

class ParserCreatorDeJson(Creator):
    def __init__(self, obj):
        self.dump_obj = dump_obj

    def factory_method(self):
        return ParserPickle(self.dump_obj)

class ParserCreatorYaml(Creator):
    def __init__(self, obj):
        self.obj = obj
    def factory_method(self):
        return ParserYaml(self.obj)

class ParserCreatorDeYaml(Creator):
    def __init__(self, obj):
        self.dump_obj = dump_obj

    def factory_method(self):
        return ParserPickle(self.dump_obj)

class ParserCreatorToml(Creator):
    def __init__(self, obj):
        self.obj = obj
    def factory_method(self):
        return ParserToml(self.obj)

class ParserCreatorDeToml(Creator):
    def __init__(self, obj):
        self.dump_obj = dump_obj

    def factory_method(self):
        return ParserPickle(self.dump_obj)

class Parser(ABC):

    @abstractmethod
    def operation(self):
        pass

import pickle

class ParserPickle(Parser):
    def __init__(self, obj):
        self.obj = obj

    def pick(self):
        return pickle.dumps(self.obj)

    def operation(self):
        pick = self.pick()
        return str(pick)

class ParserDePickle(Parser):
    def __init__(self, dump_obj):
        self.dump_obj = dump_obj

    def pick(self):
        print('asdasdas' + self.dump_obj)
        return pickle.loads(self.dump_obj)
    # TODO str to byte

    def operation(self):
        pick = self.pick()
        return pick


class ParserJson(Parser):
    def __init__(self, obj):
        self.obj = obj

    def json(self):
        jstr = '{\n'
        jstr += '\'' + 'type' + '\': ' \
                + '\'' + self.obj['type'] + '\'\n'
        jstr += '\'' + 'lines' + '\': ' \
                + '\'' + self.obj['lines'] + '\'\n'
        jstr += '}'
        return jstr

    def operation(self):
        j = self.json()
        return j

class ParserYaml(Parser):
    def __init__(self, obj):
        self.obj = obj

    def yaml(self):
        ystr = 'type' + ': ' \
                + self.obj['type'] + '\n'
        ystr += 'lines' + ': ' \
                + self.obj['lines'] + '\n'

        return ystr
    def operation(self):
        y = self.yaml()
        return y

class ParserToml(Parser):
    def __init__(self, obj):
        self.obj = obj

    def toml(self):
        tstr = 'type' + ' = ' \
                + self.obj['type'] + '\n'
        tstr += 'lines' + ' = ' \
                + self.obj['lines'] + '\n'

        return tstr
    def operation(self):
        t = self.toml()
        return t


def client_code(creator: Creator):

    # print(f"Client work with {creator.same_operation()}")
    return creator.same_operation()
# TODO add return

def create_serializer(type, obj):
    d = {'pickle': ParserCreatorPickle, 'json': ParserCreatorJson, 'yaml': ParserCreatorYaml, 'toml': ParserCreatorToml}
    return client_code(d[type](obj))


def create_deserializer(type, dump_obj):
    d = {'pickle': ParserCreatorDePickle, 'json': ParserCreatorDeJson, 'yaml': ParserCreatorDeYaml, 'toml': ParserCreatorDeToml}
    return client_code(d[type](dump_obj))


if __name__ == "__main__":

    create_serializer('pickle', '1231231231')
    client_code(ParserCreatorPickle('1234'))
    client_code(ParserCreatorYaml({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))
    client_code(ParserCreatorJson({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))
    client_code(ParserCreatorToml({'type': 'dict', 'lines': "{'asds': 1, 3: {'a': 4, 333: dump}}"}))