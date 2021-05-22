import argparse
import inspect
from abc import ABC, abstractmethod

parser = argparse.ArgumentParser(description='Convert one file to another')
parser.add_argument('fpath', type=str, help='File path')
parser.add_argument('type_of_new', type=str, help='Converted file type')
args = parser.parse_args()

print(args.fpath)
print(args.type_of_new)

import clean

clean.convert(args.fpath, args.type_of_new)