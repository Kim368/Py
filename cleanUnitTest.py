import unittest
from clean import *
from diffTypesForTest import *

class MyTestCase(unittest.TestCase):
    def test_loads(self):
        self.assertEqual('qwerty', loads(dumps('qwerty'), {}))
        c = Collections()
        self.assertEqual(c.list_list, loads(dumps(c.list_list), {}))
        self.assertEqual(c.list_int, loads(dumps(c.list_int), {}))
        self.assertEqual(c.list_str, loads(dumps(c.list_str), {}))
        self.assertEqual(c.list_bool, loads(dumps(c.list_bool), {}))
        self.assertEqual(c.list_float, loads(dumps(c.list_float), {}))
        self.assertEqual(c.set_bool, loads(dumps(c.set_bool), {}))
        self.assertEqual(c.dictionary, loads(dumps(c.dictionary), {'my_class': my_class}))
        self.assertEqual(c.tupl, loads(dumps(c.tupl), {'my_class': my_class}))

        self.assertEqual(my_class.__dict__.keys(), loads(dumps(my_class),{}).__dict__.keys())
        self.assertEqual(my_class.my_class2.__dict__.keys(), loads(dumps(my_class.my_class2), {'my_class': my_class}).__dict__.keys())
        self.assertEqual(my_class.pr.__dict__.keys(), loads(dumps(my_class.pr), {}).__dict__.keys())
        self.assertEqual(my_class.pr(my_class('a')), loads(dumps(my_class.pr), {})(my_class('a')))
        self.assertEqual(my_class.aaa(my_class('a')), loads(dumps(my_class.aaa), {})(my_class('a')))



    def test_load(self):
        c = Collections()
        self.assertEqual(c.list_list, load(dump(c.list_list, '/home/jke/txt.json', 'pickle'), {}))
        self.assertEqual(c.list_int, load(dump(c.list_int, '/home/jke/txt.json', 'json'), {}))
        self.assertEqual(c.list_str, load(dump(c.list_str, '/home/jke/txt.json', 'toml'), {}))
        self.assertEqual(c.list_bool, load(dump(c.list_bool, '/home/jke/txt.json', 'pickle'), {}))
        self.assertEqual(c.list_float, load(dump(c.list_float, '/home/jke/txt.json', 'yaml'), {}))
        self.assertEqual(c.set_bool, load(dump(c.set_bool, '/home/jke/txt.json', 'toml'), {}))
        self.assertEqual(c.dictionary, load(dump(c.dictionary, '/home/jke/txt.json', 'json'), {'my_class': my_class}))
        self.assertEqual(c.tupl, load(dump(c.tupl, '/home/jke/txt.json', 'pickle'), {'my_class': my_class}))

        self.assertEqual(my_class.__dict__.keys(), load(dump(my_class, '/home/jke/txt.json', 'json'),{}).__dict__.keys())
        self.assertEqual(my_class.my_class2.__dict__.keys(), load(dump(my_class.my_class2, '/home/jke/txt.json', 'toml'), {'my_class': my_class}).__dict__.keys())
        self.assertEqual(my_class.pr.__dict__.keys(), load(dump(my_class.pr, '/home/jke/txt.json', 'yaml'), {}).__dict__.keys())
        self.assertEqual(my_class.pr(my_class('a')), load(dump(my_class.pr, '/home/jke/txt.json', 'toml'), {})(my_class('a')))
        self.assertEqual(my_class.aaa(my_class('a')), load(dump(my_class.aaa, '/home/jke/txt.json', 'json'), {})(my_class('a')))



    def test_conv(self):
        dump(my_class, '/home/jke/txt.json', 'yaml')
        convert('/home/jke/txt.yaml', 'json')
        self.assertEqual(my_class.__dict__.keys(),  load(dump(my_class, '/home/jke/txt.json', 'json'),{}).__dict__.keys())

        dump(my_class, '/home/jke/txt.json', 'pickle')
        convert('/home/jke/txt.yaml', 'yaml')
        self.assertEqual(my_class.__dict__.keys(),
                         load(dump(my_class, '/home/jke/txt.json', 'yaml'), {}).__dict__.keys())

        dump(my_class, '/home/jke/txt.json', 'toml')
        convert('/home/jke/txt.yaml', 'pickle')
        self.assertEqual(my_class.__dict__.keys(),
                         load(dump(my_class, '/home/jke/txt.json', 'pickle'), {}).__dict__.keys())


if __name__ == '__main__':
    unittest.main()
